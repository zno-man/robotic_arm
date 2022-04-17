

import rospy
import math


from std_msgs.msg import Float64

rospy.init_node('control')
pub = rospy.Publisher('/robot_arm_iteration_3/Rev13_position_controller/command', Float64, queue_size=10)
pub2 = rospy.Publisher('/robot_arm_iteration_3/Rev12_position_controller/command', Float64, queue_size=10)
pub3 = rospy.Publisher('/robot_arm_iteration_3/Rev11_position_controller/command', Float64, queue_size=10)
pub4 = rospy.Publisher('/robot_arm_iteration_3/Rev10_position_controller/command', Float64, queue_size=10)
r = rospy.Rate(50)

initial_angle=math.radians(0)


def oscilation(pub_name,ang):
	temp=0
	while not rospy.is_shutdown():
		angle=temp
		if temp>ang:
			angle = 2*ang-temp
		angle = math.radians(angle)
		pub_name.publish(angle)
		temp=temp+1
		if temp>2*ang:
			temp=0
		r.sleep()

def one_time(pub_name,ang):
	temp=0
	while not rospy.is_shutdown():
		angle = temp
		angle = math.radians(angle)
		pub_name.publish(angle)
		temp=temp+1
		if temp>ang:
			break
		r.sleep()

def return_to_initial_stage():
	pub.publish(initial_angle)
	pub2.publish(initial_angle)
	pub3.publish(initial_angle)
	pub4.publish(initial_angle)	
		
#print(type(pub))
"""
while not rospy.is_shutdown():
    #angle = rospy.get_time() % 360
    angle = temp
    if temp>60:
    	angle=120-temp
    
    angle=math.radians(angle)
    pub.publish(angle)
    pub2.publish(angle)
    pub3.publish(angle)
    pub4.publish(angle)    
    temp=temp+1
    if temp>120:
    	temp=0
    	"""

one_time(pub,60)
one_time(pub2,29)
one_time(pub4,100)
return_to_initial_stage()


    #r.sleep()
