# RT2_Assignment

## Assignment 2: ROS and Jupyter Assignment

This repository contains the code for a ROS and Jupyter assignment. The code allows a robot to navigate to different goals in a simulated environment while avoiding obstacles.

## Prerequisites
- ROS: Make sure you have ROS installed on your system.
- Jupyter: Install Jupyter Notebook to run the code.
- Gazebo: Install Gazebo for simulating the robot environment.
- RViz: Install RViz for visualization and debugging.
- 
## Installation

1. Open Jupyter Notebook:
jupyter notebook
2. Open the assignment file:
AAAAAAAAAAAAAAAAAAAAAAA.ipynb


## Usage

1. Set the goal coordinates:
- Enter the X-coordinate in the "Xg" field.
- Enter the Y-coordinate in the "Yg" field.
- Click the "Set Goal" button to send the goal to the robot.

2. Monitor obstacle distance:
- The "Min" field shows the minimum obstacle distance detected by the robot.

3. Visualization:
- The "Robot - Goal Positions" plot shows the trajectory of the robot as it navigates towards the goals.
- The "Reached-Cancelled Goals" plot displays the number of goals reached and cancelled.

## Functionality
- The code subscribes to the robot's odometry and laser scan data to determine the robot's position and obstacle distances.
- The `calculate_color` function assigns colors to obstacles based on their distance.
- The `find_minimum_distance` function calculates the minimum obstacle distance.
- The code provides a GUI for setting goals and monitoring the minimum obstacle distance.
- The `OdoVisualiser` class plots the robot's trajectory.
- The `GoalVisualiser` class displays the number of goals reached and cancelled.
- The `updateGUI` function updates the GUI with the latest information.
- The `handle_send_goal_click` function is triggered when the "Set Goal" button is clicked and sends the goal to the robot.
- The `createClient` function creates an action client for sending goals.
- The `sendGoal` function sends the goal to the robot using the action client.
- The `setOdoMessage` function updates the robot's position based on odometry data.
- The `clbk_laser` function updates obstacle distances based on laser scan data.
- The `updateGoalSummary` function updates the number of goals reached and cancelled.
- The `main` function initializes the ROS node and sets up the necessary subscribers and clients.

## Notes
- This code is designed to work in a simulated environment and may require modifications to run on a physical robot.
- Make sure you have the necessary dependencies installed to run ROS and Jupyter Notebook.

Feel free to explore the code and make any necessary modifications for your specific use case. Enjoy!



