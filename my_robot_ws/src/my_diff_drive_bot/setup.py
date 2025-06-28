from setuptools import setup

package_name = 'my_diff_drive_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    data_files=[
        # Include URDF and launch files in the install directory
        ('share/' + package_name + '/urdf', ['urdf/diff_drive_bot.urdf']),
        ('share/' + package_name + '/launch', ['launch/spawn.launch.py']),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joslyn',
    maintainer_email='joslynsajangeorge@gmail.com',
    description='A simple differential drive robot simulated in Gazebo using ROS 2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
