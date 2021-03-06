#!/usr/bin/env python3

#BSD 3-Clause Lisence
#Copyright (c) 2021 Ryuichi Ueda. All rights reserved.


import rospy
from std_msgs.msg import Int32

def cb(message):
        rospy.loginfo(message.data*2)

if __name__ == '__main__':
        rospy.init_node('twice')
        sub = rospy.Subscriber('count_up', Int32, cb)
        rospy.spin()
