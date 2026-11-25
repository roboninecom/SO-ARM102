cmake_minimum_required(VERSION 3.8)
project(so_arm_102_description)

find_package(ament_cmake REQUIRED)

set(model_dir "${CMAKE_CURRENT_SOURCE_DIR}/../../urdf")
install(
  FILES
    "${model_dir}/so_arm_102.xacro"
    "${model_dir}/so_arm_102.urdf"
    "${model_dir}/materials.xacro"
  DESTINATION share/${PROJECT_NAME}/urdf
)
install(
  DIRECTORY "${model_dir}/meshes"
  DESTINATION share/${PROJECT_NAME}/urdf
)
install(
  DIRECTORY launch rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
