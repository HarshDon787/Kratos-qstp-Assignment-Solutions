#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter',String)
	rospy.init_node('talker', anonymous=True)
	while not rospy.is_shutdown():
		user_str = raw_input("Please Enter your name")
		rospy.loginfo(user_str)
		pub.publish(user_str)
		rospy.sleep(1.0)


if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
	
