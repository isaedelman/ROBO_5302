import rclpy
import time
from rclpy.node import Node
from std_msgs.msg import Header

class TimePublisher(Node):
    def __init__(self):

        # Create node
        super().__init__('time_publisher')

        # Create publisher that pubs Header messages on the topic "time_topic"
        self.publisher_ = self.create_publisher(Header, 'time_topic', 10)

        # Create timer to call publish_time every 0.1 sec
        self.timer = self.create_timer(0.1, self.timer_callback)

        self.count = 0
        self.max_messages = 400

    def timer_callback(self):
        if self.count >= self.max_messages:
            self.get_logger().info('Finished publishing 400 messages.')
            rclpy.shutdown()
            return
        
        # Create header message
        msg = Header()

        # stamp message with current time
        now = self.get_clock().now().to_msg()
        msg.stamp = now

        # give each message a number
        msg.frame_id = str(self.count)

        # Publish message
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing message {self.count}")
        self.count += 1

def main(args=None):
    # Start node
    rclpy.init(args=args)
    node = TimePublisher()

    # Keep node alive
    rclpy.spin(node)

    # Clean up
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()