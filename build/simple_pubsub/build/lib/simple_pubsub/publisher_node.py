import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Custom msg
from custom_interfaces.msg import Coordinates

class Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        # self.publisher_ = self.create_publisher(String, 'chatter', 10)
        self.publisher_ = self.create_publisher(Coordinates, 'coordinates', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # self.i = 0
        self.x = 0
        self.y = 0

    def timer_callback(self):
        # msg = String()
        msg = Coordinates()
        # msg.data = f'Counting: {self.i}'

        msg.x = float(self.x)
        msg.y = float(self.y)

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: x: {msg.x}, y: {msg.y}')
        # self.i += 1
        self.x += 1.0
        self.y += 1.0

def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()