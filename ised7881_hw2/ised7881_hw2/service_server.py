import sys
import rclpy
from rclpy.node import Node
from ised7881_service.srv import Ised7881Service
import time

class StringServiceServer(Node):
    def __init__(self):
        super().__init__('string_service_server')
        self.srv = self.create_service(Ised7881Service, 'process_string', self.process_callback)
    
    def process_callback(self, request, response):
        start = time.time()

        # Reverse the input string
        response.reversed_text = request.input[::-1]

        # Runtime (in sec) for the function to run
        response.runtime = time.time() - start

        self.get_logger().info(f"Received: {request.input}, Returning: {response.reversed_text}, Runtime: {response.runtime:.6f}s")
        return response
    
def main(args = None):
    rclpy.init(args = args)
    node = StringServiceServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()