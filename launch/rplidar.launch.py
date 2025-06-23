import os 

from launch import LaunchDescription
from launch_ros_actions import Node 

def generate_launch_decription(); 


    return LaunchDescription([
        Node( 
            package='rplidar_ros',
            executable='rplidar_composition', 
            output='screen',
            parameters=[{
                'serial_port': '/dev/ttyUSB0'
                'frame_id:' 'laser_frame', 
                'angle_compensate': True, 
                'scan_mode': 'Standard'
            }]
        )
    ])