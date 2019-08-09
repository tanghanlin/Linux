#!/bin/bash

cd /home/ros/robocup
source devel/setup.bash

sleep 1s
{
gnome-terminal -t "simulate_amada_launch" -x bash -c "roslaunch bringup simulate-amada.launch;exec bash"
}
sleep 3s
{
gnome-terminal -t "THL_test_launch" -x bash -c "roslaunch gpsr_2019 THL_test.launch;exec bash"
}&
 
sleep 3s
{
gnome-terminal -t "recognizer_launch" -x bash -c "roslaunch gpsr_2019 recognizer.launch;exec bash"
}&

sleep 3s
{
gnome-terminal -t "rqt_graph" -x bash -c "rqt_graph;exec bash"
}&
sleep 3s
{
gnome-terminal -t "rqt_graph" -x bash 
}&
exit

