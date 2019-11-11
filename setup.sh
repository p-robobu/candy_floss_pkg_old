#!/bin/bash
# Setup candy_floss project

cd `dirname $0`

# Prompt the user to approve installation
read -p "#### Setup candy_floss project? (Y/N): " res_prompt

if [ "$res_prompt" == "N" ]; then
    echo "Setup cancelled..."
    exit 0
fi

# Install Baxter SDK
sudo apt update
sudo apt upgrade
sudo apt install git-core python-argparse python-wstool python-vcstools python-rosdep ros-kinetic-control-msgs ros-kinetic-joystick-drivers gazebo7 ros-kinetic-qt-build ros-kinetic-gazebo-ros-control ros-kinetic-gazebo-ros-pkgs ros-kinetic-ros-control ros-kinetic-control-toolbox ros-kinetic-realtime-tools ros-kinetic-ros-controllers ros-kinetic-xacro python-wstool ros-kinetic-tf-conversions ros-kinetic-kdl-parser ros-kinetic-moveit

cd ..
wstool init
wstool merge https://raw.githubusercontent.com/RethinkRobotics/baxter/master/baxter_sdk.rosinstall
wstool merge https://raw.githubusercontent.com/RethinkRobotics/baxter_simulator/kinetic-devel/baxter_simulator.rosinstall
wstool update
git clone https://github.com/ros-planning/moveit_robots.git
source /opt/ros/kinetic/setup.bash

cd ..
catkin_make
catkin_make install

# Copy the baxter.sh to in the workspace folder
cp -af ./src/candy_floss/baxter.sh .

# Check 
read -p "#### Do you want to connect a real robot? (Y/N): " res_prompt

if [ "$res_prompt" == "Y" ]; then
    bash ./baxter.sh

    echo "If no response, something wrong with connection"
    ping 011411P0028.local
fi

echo "#### Installation finished" 
