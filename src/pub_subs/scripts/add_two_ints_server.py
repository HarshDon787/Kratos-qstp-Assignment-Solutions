#!/usr/bin/env python

from pub_subs.srv import *
import rospy

def handle_add_two_ints(req):
    if(req.c == 1):
	print("Processing")
	return AddTwoIntsResponse(req.a + req.b,1)
    elif(req.c == 2):
	print("Processing")
	return AddTwoIntsResponse(req.a - req.b,1)
    elif(req.c == 3):
	print("Processing")
	return AddTwoIntsResponse(req.a * req.b,1)
    elif(req.c == 4):
	print("Processing")
	return AddTwoIntsResponse(req.a / req.b,1)
    else:
	print("Processing")
    	return AddTwoIntsResponse(0,0)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()

