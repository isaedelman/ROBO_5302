import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/isaac/Documents/ROBO_5302/install/ised7881_hw2'
