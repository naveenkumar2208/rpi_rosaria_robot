#! /usr/bin/env python

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

key_mapping = { 'A': [ 0, 0.06], 'B': [0, -0.06],
		'D': [0.1, 0], 'C': [-0.1, 0],
		' ': [ 0, 0] }
# g_last_twist = None

# def keys_cb(msg, twist_pub):
# 	global g_last_twist
# 	if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
# 		return # unknown key.
# 	vels = key_mapping[msg.data[0]]
# 	g_last_twist.angular.z = vels[0]
# 	g_last_twist.linear.x = vels[1]
# 	twist_pub.publish(g_last_twist)

# if __name__ == '__main__':
# 	rospy.init_node('keys_to_twist_using_rate')
# 	twist_pub = rospy.Publisher('RosAria/cmd_vel', Twist, queue_size=1)
	#twist_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=1)
# 	rospy.Subscriber('string_test', String, keys_cb, twist_pub)
# 	rate = rospy.Rate(10)
# 	g_last_twist = Twist() # initializes to zero
# 	while not rospy.is_shutdown():
# 		twist_pub.publish(g_last_twist)
#		rate.sleep()

def keys_cb(msg, twist_pub):
  # BEGIN CB
  if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
    return # unknown key.
  vels = key_mapping[msg.data[0]]
  # END CB
  t = Twist()
  t.angular.z = vels[0]
  t.linear.x  = vels[1]
  twist_pub.publish(t)

if __name__ == '__main__':
  rospy.init_node('keys_to_twist')
  twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
  rospy.Subscriber('string_test', String, keys_cb, twist_pub)
  rospy.spin()
# END ALL
