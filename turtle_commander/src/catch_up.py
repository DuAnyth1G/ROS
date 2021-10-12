#! /usr/bin/python3

import rospy
import math
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class CatchUp:
    def __init__(self) -> None:
        self.time = rospy.Rate(1)
        self.leo_pose = Pose() 
        self.leo_pub = rospy.Publisher(str(rospy.get_param('~spawned_name')) +'/cmd_vel', Twist, queue_size = 1)
        self.time.sleep()
        self.leo_sup = rospy.Subscriber(str(rospy.get_param('~spawned_name')) +'/pose', Pose, self.update)
        self.nik_sup = rospy.Subscriber('/turtle1/pose', Pose, self.catch)

    def update(self, leoPose) -> None:
        self.leo_pose = leoPose

    def catch(self, msg_from_nik) -> None:
        msg_to_leo = Twist()
        msg_to_leo.angular.z = math.atan2(msg_from_nik.y - self.leo_pose.y, msg_from_nik.x - self.leo_pose.x) - self.leo_pose.theta
        msg_to_leo.linear.x = msg_from_nik.linear_velocity
        self.leo_pub.publish(msg_to_leo)

rospy.init_node('catch_up')
CatchUp()
rospy.spin()
