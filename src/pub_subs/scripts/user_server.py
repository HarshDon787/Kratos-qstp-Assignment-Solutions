#! /usr/bin/env python

import rospy

import actionlib

import pub_subs.msg
import actionlib
import time
class userAction(object):
    print("Started here11")
    # create messages that are used to publish feedback/result
    _feedback = pub_subs.msg.assignmentFeedback()
    _result = pub_subs.msg.assignmentResult()
    passs = 0
    t0 = 0
    t1 = 0

    def __init__(self, name):	
	print("Reached at def init")
        self._action_name = name
        self._as = actionlib.SimpleActionServer("server", pub_subs.msg.assignmentAction, execute_cb=self.execute_cb, auto_start = False)
        self._as.start()
	self._feedback.feedBack = ""


      
    def execute_cb(self, goal)

        # helper variables
        success = True
 
        
        # start executing the action
        if(goal.uinput != 'A'):
	    if(self.passs == 0):
	    	self.t0=time.time()
	    	
            self._feedback.feedBack = self._feedback.feedBack + goal.uinput
	    self._feedback.feedBack = self._feedback.feedBack + "\n"
            self._as.publish_feedback(self._feedback)
	    print(self._feedback.feedBack)
	    self.passs = self.passs + 1
          
        else:
	    self.t1=time.time()
	    self._feedback.feedBack = self._feedback.feedBack + "elapsed time is" + str(self.t1-self.t0)
	    self._feedback.feedBack = self._feedback.feedBack + "\n"
            self._as.publish_feedback(self._feedback)
            self._result.uoutput = self._feedback.feedBack
            rospy.loginfo('%s: Succeeded' % self._action_name)
            self._as.set_succeeded(self._result)
	    exit()
        
if __name__ == '__main__':
    print("Starting")
    rospy.init_node('user_action')
    print("Node Initiated")
    server = userAction(rospy.get_name())
    
    rospy.spin()
