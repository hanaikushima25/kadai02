#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('four')
pub = rospy.Publisher('count_up4', Int32, queue_size=1)
rate = rospy.Rate(10)
n = 0

def cb(message):
            rospy.loginfo(message.data*4)

if __name__ == '__main__':
            rospy.init_node('four')
            sub = rospy.Subscriber('count_up3', Int32, cb)
            rospy.spin()
