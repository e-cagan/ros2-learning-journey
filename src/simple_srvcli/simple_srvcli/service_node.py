import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

# Custom srv
from custom_interfaces.srv import MultiplyThree

class Service(Node):
    def __init__(self):
        super().__init__('service')
        # self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.srv = self.create_service(MultiplyThree, 'multiply_three_nums', self.multiply_three_nums_callback)

    def add_two_ints_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'Request: {request.a} + {request.b}')

        return response
    
    def multiply_three_nums_callback(self, request, response):
        response.product = request.a * request.b * request.c
        self.get_logger().info(f'Request: {request.a} * {request.b} * {request.c}')

        return response

def main():
    rclpy.init()
    srv = Service()
    rclpy.spin(srv)
    srv.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()