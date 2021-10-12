#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
rospy.init_node('turtle_draw_water_lily.py')
pub=rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 1)

msg = Twist()
r = rospy.Rate(0.5)
r.sleep()
while not rospy.is_shutdown():
    msg.linear.x = 2.0
    msg.angular.z = 0.6
    pub.publish(msg)
    r.sleep()
    msg.linear.x = 1
    msg.angular.z = -0.2
    pub.publish(msg)
    r.sleep()
    msg.linear.x = 2.0
    msg.angular.z = 0.6
    pub.publish(msg)
    r.sleep()
    msg.linear.x = 0.0
    msg.angular.z = 1.56
    pub.publish(msg)
    r.sleep()