#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def cb(message):
            rospy.loginfo(message.data*5)

if __name__ == '__main__':
        rospy.init_node('five')
        sub = rospy.Subscriber('count_up5', Int32, cb)
        rospy.spin()
