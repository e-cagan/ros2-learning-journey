import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Custom msg
from custom_interfaces.msg import Coordinates

class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        # self.subscription_ = self.create_subscription(String, "chatter", self.listener_callback, 10)
        self.subscription_ = self.create_subscription(Coordinates, "coordinates", self.listener_callback, 10)
        self.subscription_ # Prevent unused var warning
    
    def listener_callback(self, msg):
        # return self.get_logger().info(f'I heard: {msg.data}')
        return self.get_logger().info(f"I heard -> x={msg.x:.1f}, y={msg.y:.1f}")

def main(args=None):
    rclpy.init()
    subscriber = Subscriber()
    rclpy.spin(subscriber)
    subscriber.destroy_node()
    rclpy.shutdown()