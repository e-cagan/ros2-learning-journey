import rclpy
from rclpy.node import Node

class ParamsNode(Node):
    def __init__(self):
        super().__init__('params_node')
        self.params_ = self.declare_parameter('parameter', 'cagan')
        self.timer = self.create_timer(1, self.timer_callback)
    
    def timer_callback(self):
        # Take parameter value
        parameter = self.get_parameter('parameter').get_parameter_value().string_value

        # Write logs
        self.get_logger().info(f'User: {parameter}')

        # Declare new param and set
        new_parameter = rclpy.Parameter(
            'parameter',
            rclpy.Parameter.Type.STRING,
            'cagan'
        )
        all_new_parameters = [new_parameter]
        self.set_parameters(all_new_parameters)

def main():
    rclpy.init()
    params = ParamsNode()
    rclpy.spin(params)
    params.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()