# anaswarrajesh_horizon_s4
Horizon software task

Task 3 - ROS 2 Humble Setup and Implementation

Description

This task involves setting up Ubuntu, installing ROS 2 Humble, and implementing a basic publisher-subscriber model in ROS 2.

Part A: Installing Ubuntu

Downloaded Ubuntu 22.04 from the official website: Ubuntu Downloads

Install Ubuntu via one of the following methods:

Dual Boot alongside windows OS

Follow the installation guide provided by Ubuntu.

Part B: Installing ROS 2 Humble

Follow the official ROS 2 Humble installation guide: ROS 2 Installation

Install ROS 2 dependencies and set up the environment:

sudo apt update && sudo apt install -y software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install -y curl
curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key | sudo apt-key add -
sudo apt update && sudo apt install -y ros-humble-desktop
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc

