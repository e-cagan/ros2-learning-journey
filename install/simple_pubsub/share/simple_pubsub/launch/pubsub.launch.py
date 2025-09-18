from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Publisher node
        Node(
            package='simple_pubsub',
            namespace='pubsub',
            executable='talker',
            name='pub_node'
        ),
        
        # Subscriber node
        Node(
            package='simple_pubsub',
            namespace='pubsub',
            executable='listener',
            name='sub_node'
        )
    ])