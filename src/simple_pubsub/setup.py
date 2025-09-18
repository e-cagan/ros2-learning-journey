from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'simple_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Integrating launch file
        (os.path.join('share', package_name, 'launch'), glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cagan',
    maintainer_email='emincaganapaydin@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = simple_pubsub.publisher_node:main',
            'listener = simple_pubsub.subscriber_node:main',
        ],
    },
)
