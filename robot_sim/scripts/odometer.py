#! /usr/bin/env python3


import sys
import rospy
from nav_msgs.msg import Odometry
from robot_sim.msg import OdoSensor

odoMsg = OdoSensor()

def setOdoMessage(msg):
    global odoMsg

    odoMsg.x = msg.pose.pose.position.x
    odoMsg.y = msg.pose.pose.position.y
    odoMsg.vel_x = msg.twist.twist.linear.x
    odoMsg.vel_y = msg.twist.twist.linear.y

if __name__ == "__main__":

    try:
        rospy.init_node('odemeter')
        odoMessageSubscriber = rospy.Subscriber("odom", Odometry, setOdoMessage)
        odoMessagePublisher = rospy.Publisher('odometer', OdoSensor, queue_size=10)

        rate = rospy.Rate(2) 

        while not rospy.is_shutdown():
            if odoMsg:
                odoMessagePublisher.publish(odoMsg)
                rate.sleep()

    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)


            

        