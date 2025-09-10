import math
import time

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, CancelResponse

from custom_interfaces.action import MoveRobot

class MoveRobotActionServer(Node):
    """Simulated motion: increases current_distance at 'speed' m/s until target_distance is reached."""

    def __init__(self):
        super().__init__('move_robot_server')
        self._action_server = ActionServer(
            self,
            MoveRobot,
            'move_robot',                 # action name
            execute_callback=self.execute_callback,
            goal_callback=self.goal_callback,
            cancel_callback=self.cancel_callback,
            handle_accepted_callback=None
        )

    # Called when a goal request arrives (you can reject/accept here)
    def goal_callback(self, goal_request):
        self.get_logger().info(
            f"Received goal: target={goal_request.target_distance:.2f} m, speed={goal_request.speed:.2f} m/s"
        )
        # Basic validation: positive speed and distance
        if goal_request.target_distance <= 0.0 or goal_request.speed <= 0.0:
            self.get_logger().warn("Rejecting goal: target_distance and speed must be > 0")
            return rclpy.action.GoalResponse.REJECT
        return rclpy.action.GoalResponse.ACCEPT

    # Called when a cancel request arrives
    def cancel_callback(self, goal_handle):
        self.get_logger().info('Cancel request received.')
        return CancelResponse.ACCEPT

    # Main execution (runs in its own thread)
    async def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        goal = goal_handle.request

        start_time = self.get_clock().now()
        current_distance = 0.0
        dt = 0.1  # 10 Hz loop

        feedback = MoveRobot.Feedback()

        while current_distance < goal.target_distance:
            # Check for cancel
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Goal canceled.')
                return MoveRobot.Result(total_time=(self.get_clock().now() - start_time).nanoseconds / 1e9)

            # Integrate distance
            current_distance += goal.speed * dt
            current_distance = min(current_distance, goal.target_distance)

            # Send feedback
            progress = current_distance / goal.target_distance if goal.target_distance > 0 else 1.0
            feedback.current_distance = float(current_distance)
            feedback.progress = float(progress)
            goal_handle.publish_feedback(feedback)

            # Sleep
            await rclpy.task.Future()  # noop to allow cooperative scheduling
            time.sleep(dt)

        # Succeed
        goal_handle.succeed()
        elapsed = (self.get_clock().now() - start_time).nanoseconds / 1e9
        result = MoveRobot.Result()
        result.total_time = float(elapsed)
        self.get_logger().info(f'Goal succeeded in {elapsed:.2f}s')
        return result

def main():
    rclpy.init()
    node = MoveRobotActionServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
