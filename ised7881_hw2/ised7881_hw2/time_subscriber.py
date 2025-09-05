import rclpy
import matplotlib.pyplot as plt
import time
from rclpy.node import Node
from std_msgs.msg import Header


class TimeSubscriber(Node):
    def __init__(self):

        # Create Node
        super().__init__("time_subscriber")

        # Create a subscriber to the "time_topic"
        self.subscription = self.create_subscription(
            Header,
            "time_topic",
            self.listener_callback,
            10,
        )

        # Store latencies
        self.latencies = []
        self.n_messages = 400

    def listener_callback(self, msg):

        # Convert message timestamp to sec
        sent_time = msg.stamp.sec + msg.stamp.nanosec * 1e-9

        # Current time in sec
        ref_time = self.get_clock().now().nanoseconds * 1e-9

        # Calculate latency (rec - sent)
        latency = ref_time - sent_time
        self.latencies.append(latency)

        self.get_logger().info(f"Received latency: {latency:.6f}s")

        # After 400 msgs stop and plot hist
        if len(self.latencies) >= self.n_messages:
            self.plot_historgram()
            rclpy.shutdown()

    def plot_historgram(self):
        
        # Plot hist
        plt.hist(self.latencies, bins=30, edgecolor='black')
        plt.xlabel("Transfer Latency (sec)")
        plt.ylabel("Frequency (#)")
        plt.title("Subscriber/Publisher Latency over 400 Messages")
        plt.xlim(0, 0.014)
        plt.show()

def main(args=None):
    rclpy.init(args=args)
    node = TimeSubscriber()

    # Run sibscriber
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
