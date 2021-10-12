#! /usr/bin/python3
import rospy
from turtlesim.srv import Spawn
rospy.init_node('turtle_spawner')
rospy.wait_for_service('/spawn')
spawner = rospy.ServiceProxy('/spawn', Spawn)
spawner(2.0, 8.0, 4.0, rospy.get_param('~spawned_name'))