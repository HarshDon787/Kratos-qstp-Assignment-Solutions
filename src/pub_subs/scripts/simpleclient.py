#!/usr/bin/env python

import sys
import rospy
from pub_subs.srv import *

def add_two_ints_client(x, y, z):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
        resp1 = add_two_ints(x, y, z)
	print(resp1.result)
        return resp1.sum

    except rospy.ServiceException, e:
        print "Service call failed: %s"%e





if __name__ == "__main__":
    x = float(input("Please enter the x"))
    y = float(input("Please enter the y"))
    z = int(input("Please enter the z"))
    print "the result is  %s"%( add_two_ints_client(x, y, z))
   
