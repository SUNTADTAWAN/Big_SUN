import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aitthikit/Memekhos_ws/install/examples_rclpy_pointcloud_publisher'
