import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

# Custom srv
from custom_interfaces.srv import MultiplyThree

class Client(Node):
    def __init__(self):
        super().__init__('client')
        # self.cli = self.create_client(AddTwoInts, 'add_two_ints')
        self.cli = self.create_client(MultiplyThree, 'multiply_three_nums')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service is not ready. Requesting again...")
        # self.req = AddTwoInts.Request()
        self.req = MultiplyThree.Request()

    # def send_request(self, a, b):
        # self.req.a = a
        # self.req.b = b
        
        # return self.cli.call_async(self.req)

    def send_request(self, a, b, c):
        self.req.a = a
        self.req.b = b
        self.req.c = c

        return self.cli.call_async(self.req)

def main():
    rclpy.init()
    cli = Client()

    # Sending request
    # future = cli.send_request(int(sys.argv[1]), int(sys.argv[2]))
    future = cli.send_request(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    rclpy.spin_until_future_complete(cli, future)

    # Taking response
    response = future.result()
    # cli.get_logger().info(f"Result of add two ints {sys.argv[1]} and {sys.argv[2]} is {response.sum}")
    cli.get_logger().info(f'Result of multiply three nums {sys.argv[1]}, {sys.argv[2]} and {sys.argv[3]} is {response.product}')

    rclpy.shutdown()

if __name__ == '__main__':
    main()