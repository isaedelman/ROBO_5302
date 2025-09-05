import sys
import rclpy
from rclpy.node import Node
from ised7881_service.srv import Ised7881Service
import time
import matplotlib.pyplot as plt


class StringServiceClient(Node):
    def __init__(self):
        super().__init__("string_service_client")
        # Create client
        self.client = self.create_client(Ised7881Service, "process_string")
        # Wait for service
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Waiting for service ...")

    def send_request(self, input_string):
        req = Ised7881Service.Request()
        req.input = input_string
        return self.client.call_async(req)
    
def main(args = None):
    rclpy.init(args = args)
    node = StringServiceClient()

    n_calls = 400
    latencies = []

    for i in range(n_calls):
        input_text = f"Message {i}"
        start = time.time()
        future = node.send_request(input_text)
        rclpy.spin_until_future_complete(node, future)
        end = time.time()

        if future.result() is not None:
            srv_response = future.result()
            round_trip = end - start
            # Subtract float64 value to only get data transfer time
            transfer_latency = round_trip - srv_response.runtime
            latencies.append(transfer_latency)
            node.get_logger().info(f"Call {i}: Transfer latency = {transfer_latency:.6f}s")
        else:
            node.get_logger().error("Service call failed")

    # Plot histogram stuff
    plt.hist(latencies, bins=400, edgecolor="black")
    plt.xlabel("Transfer Latency (sec)")
    plt.ylabel("Frequency (#)")
    plt.title("Client/Server Transfer Latency over 400 Messages")
    plt.xlim(0, 0.014)
    plt.show()

    Node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()