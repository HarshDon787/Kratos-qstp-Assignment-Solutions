#! /usr/bin/env python
from __future__ import print_function

import rospy


# Brings in the SimpleActionClient
import pub_subs
import pub_subs.msg
import actionlib

import pub_subs.msg


def userAction_client():
    string = ""
    client = actionlib.SimpleActionClient('server', pub_subs.msg.assignmentAction)

	
     
   

    while(string != 'A'):
	string=raw_input("Please enter a message")
    	goal = pub_subs.msg.assignmentGoal(string)
   	client.send_goal(goal)
	

    if(string == 'A'):
    	client.wait_for_result()

    # Prints out the result of executing the action
    	return client.get_result()  

if __name__ == '__main__':
    try:
	result = []
        # Initializes a rospy node so that the SimpleActionClient can
        # publish and subscribe over ROS.
        rospy.init_node('user_client')
        result = userAction_client()
	list=[]
	list = result.uoutput.split("\n")
	for line in list:
		print(line)
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
