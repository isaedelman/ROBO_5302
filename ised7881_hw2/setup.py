from setuptools import find_packages, setup

package_name = 'ised7881_hw2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='isaac',
    maintainer_email='edelmanisaac@gmail.com',
    description='latency histogram plotter',
    license='Apache 2.0?',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service_server = ised7881_hw2.service_server:main',
            'service_client = ised7881_hw2.service_client:main',
            'time_publisher = ised7881_hw2.time_publisher:main',
            'time_subscriber = ised7881_hw2.time_subscriber:main',
        ],
    },
)
