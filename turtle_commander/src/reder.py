#! /usr/bin/python3

import rospy
from turtlesim.msg import Pose

def calllog(msg):
    rospy.logerr(msg)

rospy.init_node('turtle_log_pose')
rospy.Subscriber('/turtle1/pose', Pose, calllog)

rospy.spin()
