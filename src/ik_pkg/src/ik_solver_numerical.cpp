#include <iostream>
#include <rclcpp/rclcpp.hpp>
#include <ament_index_cpp/get_package_share_directory.hpp>
#include <kdl_parser/kdl_parser.hpp>
#include <urdf/model.h>
#include <kdl/tree.hpp>
#include <kdl/chain.hpp>
#include <kdl/chainfksolverpos_recursive.hpp>
#include <kdl/chainiksolvervel_pinv.hpp>
#include <kdl/chainiksolverpos_lma.hpp>
#include <kdl/jntarray.hpp>
#include <std_msgs/msg/float32_multi_array.hpp>

class IKSolverNode : public rclcpp::Node
{
public:
    IKSolverNode() : Node("ik_solver_node")
    {
        std::string package_path = ament_index_cpp::get_package_share_directory("description");
        std::string urdf_path = package_path + "/model/urdf/spot_mini/model.urdf";
        RCLCPP_INFO(this->get_logger(), "URDF path: %s", urdf_path.c_str());

        if (!loadURDFModel(urdf_path)) {
            RCLCPP_ERROR(this->get_logger(), "Failed to parse URDF file.");
            rclcpp::shutdown();
        }

        leg_names_ = {"fl", "fr", "hl", "hr"};
        std::vector<std::string> base_links = {"base", "base", "base", "base"};
        std::vector<std::string> end_links = {"FL_foot", "FR_foot", "RL_foot", "RR_foot"};

        for (size_t i = 0; i < leg_names_.size(); ++i) {
            if (!createKDLChain(base_links[i], end_links[i], kdl_chains_[leg_names_[i]])) {
                RCLCPP_ERROR(this->get_logger(), "Failed to extract chain for leg: %s", leg_names_[i].c_str());
                rclcpp::shutdown();
            }
            solvers_[leg_names_[i]] = std::make_shared<KDL::ChainIkSolverPos_LMA>(kdl_chains_[leg_names_[i]]);
            fk_solvers_[leg_names_[i]] = std::make_shared<KDL::ChainFkSolverPos_recursive>(kdl_chains_[leg_names_[i]]);
        }

        subscription_ = this->create_subscription<std_msgs::msg::Float32MultiArray>(
            "foot_pose", 10, std::bind(&IKSolverNode::footPoseCallback, this, std::placeholders::_1));
    }

private:
    KDL::Tree kdl_tree_;
    std::vector<std::string> leg_names_;
    std::map<std::string, KDL::Chain> kdl_chains_;
    std::map<std::string, std::shared_ptr<KDL::ChainIkSolverPos_LMA>> solvers_;
    std::map<std::string, std::shared_ptr<KDL::ChainFkSolverPos_recursive>> fk_solvers_;
    rclcpp::Subscription<std_msgs::msg::Float32MultiArray>::SharedPtr subscription_;

    bool loadURDFModel(const std::string& urdf_path)
    {
        urdf::Model model;
        if (!model.initFile(urdf_path)) {
            RCLCPP_ERROR(this->get_logger(), "Failed to load URDF file.");
            return false;
        }
        if (!kdl_parser::treeFromUrdfModel(model, kdl_tree_)) {
            RCLCPP_ERROR(this->get_logger(), "Failed to convert URDF to KDL tree.");
            return false;
        }
        return true;
    }

    bool createKDLChain(const std::string& base_link, const std::string& end_link, KDL::Chain& chain)
    {
        if (!kdl_tree_.getChain(base_link, end_link, chain)) {
            RCLCPP_ERROR(this->get_logger(), "Failed to extract KDL chain from %s to %s", base_link.c_str(), end_link.c_str());
            return false;
        }
        return true;
    }

    void footPoseCallback(const std_msgs::msg::Float32MultiArray::SharedPtr msg)
    {
        if (msg->data.size() != 12) {
            RCLCPP_ERROR(this->get_logger(), "Invalid foot_pose message size: expected 12, got %zu", msg->data.size());
            return;
        }

        std::stringstream ss;
        ss << "Received foot_pose: ";
        for (const auto& value : msg->data) {
            ss << value << " ";
        }
        RCLCPP_INFO(this->get_logger(), "%s", ss.str().c_str());

        for (size_t i = 0; i < leg_names_.size(); ++i) {
            KDL::Vector desired_position(msg->data[i * 3], msg->data[i * 3 + 1], msg->data[i * 3 + 2]);
            
            // Use identity rotation (no rotation) or provide actual orientation
            KDL::Frame desired_pose(KDL::Rotation::Identity(), desired_position);

            if (!solveIK(leg_names_[i], desired_pose)) {
                RCLCPP_ERROR(this->get_logger(), "Inverse kinematics solution failed for leg: %s", leg_names_[i].c_str());
            } else {
                RCLCPP_INFO(this->get_logger(), "Inverse kinematics solution succeeded for leg: %s", leg_names_[i].c_str());
            }
        }
    }

    bool solveIK(const std::string& leg, const KDL::Frame& desired_pose)
    {
        KDL::JntArray q_init(kdl_chains_[leg].getNrOfJoints());
        KDL::JntArray q_out(kdl_chains_[leg].getNrOfJoints());
        
        for (unsigned int i = 0; i < kdl_chains_[leg].getNrOfJoints(); ++i) {
            q_init(i) = 0.0;
        }
        
        int ret = solvers_[leg]->CartToJnt(q_init, desired_pose, q_out);
        
        if (ret >= 0) {
            for (unsigned int i = 0; i < q_out.rows(); ++i) {
                RCLCPP_INFO(this->get_logger(), "%s Joint %d: %f", leg.c_str(), i, q_out(i));
            }
            return true;
        }
        return false;
    }

    bool computeFK(const std::string& leg, const KDL::JntArray& joint_positions, KDL::Frame& end_effector_pose)
    {
        if (fk_solvers_.find(leg) == fk_solvers_.end()) {
            RCLCPP_ERROR(this->get_logger(), "No FK solver found for leg: %s", leg.c_str());
            return false;
        }

        int ret = fk_solvers_[leg]->JntToCart(joint_positions, end_effector_pose);
        return (ret >= 0);
    }
};

int main(int argc, char** argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<IKSolverNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
