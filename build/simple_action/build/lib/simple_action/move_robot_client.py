import sys
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient

from custom_interfaces.action import MoveRobot

class MoveRobotActionClient(Node):
    """Sends a goal, prints feedback and result. Use ctrl+c to stop the client; use cancel_demo=True to test cancel."""

    def __init__(self):
        super().__init__('move_robot_client')
        self._client = ActionClient(self, MoveRobot, 'move_robot')

    def send_goal(self, target_distance: float, speed: float, cancel_demo: bool = False):
        goal_msg = MoveRobot.Goal()
        goal_msg.target_distance = float(target_distance)
        goal_msg.speed = float(speed)

        # Wait for server
        if not self._client.wait_for_server(timeout_sec=5.0):
            self.get_logger().error('Action server not available.')
            return

        # Send goal with feedback callback
        self.get_logger().info(f'Sending goal: target={target_distance} speed={speed}')
        send_goal_future = self._client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        rclpy.spin_until_future_complete(self, send_goal_future)
        goal_handle = send_goal_future.result()

        if not goal_handle.accepted:
            self.get_logger().warn('Goal rejected.')
            return

        # Optional cancel demo
        if cancel_demo:
            self.get_logger().info('Canceling goal in 2s to test cancel...')
            self.create_timer(2.0, lambda: goal_handle.cancel_goal_async())

        # Wait for result
        get_result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, get_result_future)
        result = get_result_future.result().result
        status = get_result_future.result().status

        self.get_logger().info(f'Result: total_time={result.total_time:.2f}s, status={status}')

    def feedback_callback(self, feedback_msg):
        fb = feedback_msg.feedback
        self.get_logger().info(
            f'Feedback -> current_distance={fb.current_distance:.2f} m, progress={fb.progress*100:.1f}%'
        )

def main():
    rclpy.init()
    node = MoveRobotActionClient()

    # Args: target_distance speed [cancel_demo]
    if len(sys.argv) < 3:
        node.get_logger().info('Usage: ros2 run simple_action client <target_distance> <speed> [cancel]')
        rclpy.shutdown()
        return

    target = float(sys.argv[1])
    speed = float(sys.argv[2])
    cancel_demo = (len(sys.argv) > 3 and sys.argv[3].lower() in ['1','true','yes','y'])

    node.send_goal(target, speed, cancel_demo)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
