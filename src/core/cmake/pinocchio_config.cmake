# Add pinocchio library to the linker's search path
link_directories(
  ${pinocchio_LIBRARY_DIRS}
)

# Add pinocchio flags
set(DEEPBREAK_PINOCCHIO_FLAGS
  ${DEEPBREAK_CXX_FLAGS}
  ${pinocchio_CFLAGS_OTHER}
  -Wno-ignored-attributes
  # -Wno-invalid-partial-specialization   # to silence warning with unsupported Eigen Tensor
  -DPINOCCHIO_URDFDOM_TYPEDEF_SHARED_PTR
  -DPINOCCHIO_URDFDOM_USE_STD_SHARED_PTR
)