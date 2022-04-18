#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import math

rospy.init_node('control')
end_effector = 0
lnk3 = 0
lnk2 = 0
lnk1 = 0
end_tip = 0
end_slide_vel = 0 #can be -0.1(deploy) or 0.1(retract)
vel = [0.1,-0.1]

pub_end_effector = rospy.Publisher('/robot_arm_iteration_3/Rev10_position_controller/command', Float64, queue_size=1)
pub_lnk3 = rospy.Publisher('/robot_arm_iteration_3/Rev11_position_controller/command', Float64, queue_size=1)
pub_lnk2 = rospy.Publisher('/robot_arm_iteration_3/Rev12_position_controller/command', Float64, queue_size=1)
pub_lnk1 = rospy.Publisher('/robot_arm_iteration_3/Rev13_position_controller/command', Float64, queue_size=1)
pub_end_tip = rospy.Publisher('/robot_arm_iteration_3/Rev15_position_controller/command', Float64, queue_size=1)
pub_end_slide_vel = rospy.Publisher('/robot_arm_iteration_3/Slider14_position_controller/command', Float64, queue_size=1)

count = 0
bool = True

r = rospy.Rate(100)

while not rospy.is_shutdown():
    print(":",end = '')
    angle = math.radians(int(input()))
    # angle = rospy.get_time() % 360 
    # pub_end_effector.publish(angle)
    # pub_lnk3.publish(angle)
    pub_lnk2.publish(angle)
    # pub_lnk1.publish(angle)
    # pub_end_tip.publish(angle)
    
    # count+=1
    # if count == 100:
    #     pub_end_slide_vel.publish(vel[int(bool)])
    #     bool = not bool
    #     count = 0
        
    r.sleep()
