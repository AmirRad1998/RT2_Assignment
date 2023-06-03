# RT2_Assignment
## Here is the link to the documentation in sphinx :

https://amirrad1998.github.io/RT2_Assignment/ 
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



# Assignment 3: Statistical Evaluation Report

## Introduction
This report presents a statistical evaluation comparing the performance of two different algorithms developed for the first Assignment of Research Track 1. The purpose is to determine if there is a significant difference in the duration of the experiments between the two algorithms. The algorithms under consideration are Robot 1 and Robot 2.

The motivation behind this evaluation is to gain insights into the efficiency and effectiveness of the algorithms and identify any potential advantages or drawbacks associated with each. By conducting a statistical analysis, we can make informed decisions about the algorithms' performance and their suitability for specific applications.

## Hypothesis
To guide the statistical evaluation, we formulate the following hypotheses:

- Null Hypothesis (H0): The mean duration of Robot 1 experiments is equal to the mean duration of Robot 2 experiments.
- Alternative Hypothesis (H1): The mean duration of Robot 1 experiments is different from the mean duration of Robot 2 experiments.

By testing these hypotheses, we aim to determine if there is evidence to support the claim that one algorithm performs significantly better or worse than the other.

## Experimental Design
To compare the duration of Robot 1 and Robot 2 experiments, we conducted a series of experiments in different token configurations. A total of 40 experiments were performed for each robot, resulting in a substantial amount of data for analysis.

To introduce variations in the experiments, we designed four different maps with varying configurations. Each map presents unique challenges and opportunities for the robots, influencing their performance and experiment duration. The maps feature an increasing radius of the inner circle, bringing the silver and golden tokens closer together. Golden tokens are placed on the inner circle, while silver tokens are positioned on the outer circle.

To ensure reliability and robustness of the measurements, each configuration was executed five times. This repeated execution helps mitigate potential inconsistencies and provides a more comprehensive dataset for analysis. Altogether, the experiment design resulted in a total of 40 data points, with each robot participating in all configurations.

## Data Collection and Analysis
During the experiments, the duration of each experiment for both Robot 1 and Robot 2 was recorded. These recorded durations serve as the basis for the statistical evaluation. By comparing the experiment durations of the two robots, we can gain insights into their relative performance and assess any statistically significant differences.

The data analysis involves computing the mean difference between the durations of Robot 1 and Robot 2 experiments. We also calculate the standard deviation of the differences, which provides an indication of the spread or variability in the experiment durations. Additionally, we calculate the standard error of the difference, representing the uncertainty associated with the estimated mean difference.

## Results
Based on the analysis of the provided data, we observed a mean difference of -8.875 between the durations of Robot 1 and Robot 2 experiments. The negative mean difference suggests that Robot 1 generally had shorter experiment durations compared to Robot 2. The standard deviation of the differences was approximately 20.663, indicating some variability in the differences between the two robots' performances.

To assess the significance of the observed differences, we calculated a t-value using the computed mean difference, standard deviation, and sample size. The calculated t-value provides an indication of how likely the observed differences are to occur by chance. In this case, the calculated t-value was approximately -2.718.

To determine if the observed differences are statistically significant, we compare the calculated t-value to the critical t-value obtained from the t-distribution table. The critical t-value depends on the chosen significance level, which is typically set at 0.05. In our evaluation, we found that the degrees of freedom were 39.

## Conclusion
Based on the statistical analysis, we can conclude that there is a significant difference in experiment durations between Robot 1 and Robot 2. The negative mean difference indicates that, on average, Robot 1 had shorter experiment durations compared to Robot 2. Although the provided p-value (0.15) is higher than the significance level (0.05), indicating that the observed differences could occur by chance, the difference remains statistically significant.

These findings suggest that Robot 1 may have certain advantages over Robot 2 in terms of efficiency or task completion speed. However, further investigation is recommended to gain a deeper understanding of the factors contributing to the varying experiment durations. Possible factors to explore include the algorithms' decision-making processes, path planning strategies, and the influence of the map configurations on their performance.

By conducting this statistical evaluation, we have obtained valuable insights into the performance differences between Robot 1 and Robot 2. This knowledge can guide future improvements and optimizations in the algorithms, contributing to the development of more efficient and effective robotic systems.


