from ament_index_python.packages import get_package_share_path
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
import xacro


def generate_launch_description():
    package_name = 'so_arm_102_description'
    package_share = get_package_share_path(package_name)
    model = xacro.process_file(
        str(package_share / 'urdf' / 'so_arm_102.xacro'),
        mappings={'mesh_prefix': f'package://{package_name}/urdf/meshes'},
    )
    robot_description = ParameterValue(model.toxml(), value_type=str)
    use_gui = LaunchConfiguration('gui')

    return LaunchDescription([
        DeclareLaunchArgument(
            'gui',
            default_value='true',
            choices=['true', 'false'],
            description='Show joint sliders. If disabled, publish default joint positions.',
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}],
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            condition=IfCondition(use_gui),
        ),
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            condition=UnlessCondition(use_gui),
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', str(package_share / 'rviz' / 'display.rviz')],
        ),
    ])
