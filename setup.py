from setuptools import find_packages, setup

package_name = 'webots_ros2_limo'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name, ['package.xml']))

# launch / worlds / protos / resource 설치
data_files.append(('share/' + package_name + '/launch', ['launch/robot_launch.py']))
data_files.append(('share/' + package_name + '/worlds', ['worlds/limo_world.wbt']))
data_files.append(('share/' + package_name + '/protos', ['protos/LimoFourDiff.proto']))
data_files.append(('share/' + package_name + '/protos', ['protos/LimoAckerman.proto']))
data_files.append(('share/' + package_name + '/resource', ['resource/ros2control.yaml']))
data_files.append(('share/' + package_name + '/resource', ['resource/limo.urdf']))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lsbean991',
    maintainer_email='lsbean991@gmail.com',
    description='webots_ros2 limo package',
    license='Apache-2.0',
    extras_require={'test': ['pytest']},
    entry_points={'console_scripts': []},
)
