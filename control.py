#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import math

rospy.init_node('control')
end_effector = 90
lnk3 = 0
lnk2 = 0
lnk1 = 0
end_tip = 0
end_slide_vel = 0 #can be -0.1(deploy) or 0.1(retract)
vel = [0.1,-0.1]

lo1 = [0,0,0]
lo2 = [45,45,0]
lo3 = [90,90,0]


pub_end_effector = rospy.Publisher('/robot_arm_iteration_3/Rev10_position_controller/command', Float64, queue_size=1)
pub_lnk3 = rospy.Publisher('/robot_arm_iteration_3/Rev11_position_controller/command', Float64, queue_size=1)
pub_lnk2 = rospy.Publisher('/robot_arm_iteration_3/Rev12_position_controller/command', Float64, queue_size=1)
pub_lnk1 = rospy.Publisher('/robot_arm_iteration_3/Rev13_position_controller/command', Float64, queue_size=1)
pub_end_tip = rospy.Publisher('/robot_arm_iteration_3/Rev15_position_controller/command', Float64, queue_size=1)
pub_end_slide_vel = rospy.Publisher('/robot_arm_iteration_3/Slider14_position_controller/command', Float64, queue_size=1)

count = 0
bool = True

r = rospy.Rate(100)


#functions



def configure():
    print("Enter loc 1 cordinates:",end = '')
    lo1 = list(map(float , input().strip().split()))
    print("Enter loc 2 cordinates:",end = '')
    lo2 = list(map(float , input().strip().split()))
    print("Enter loc 3 cordinates:",end = '')
    lo3 = list(map(float , input().strip().split()))
    print(lo1,lo2,lo3)
    return lo1,lo2,lo3

def move_to(loc): #input in degrees
    global lnk1,lnk2,lnk3,end_effector
    lst = [lnk1,lnk2,lnk3]
    pub = [pub_lnk1,pub_lnk2,pub_lnk3]
    

    for i in range(3): # i = 0 lnk1 , i =1 lnk2 , i = 2 lnk 3
        temp = loc[i]-lst[i]
        if temp>0:
            while not rospy.is_shutdown():
                lst[i]+=1 
                if lst[i] > loc[i]:
                    break
                pub[i].publish(math.radians(lst[i]))
                
                if i>0: #other than for the base angle we must stabilise end effector
                    end_effector -=1 
                    pub_end_effector.publish(math.radians(end_effector))
                    

                r.sleep()

            lnk1 = lst[0]-1
            lnk2 = lst[1]-1
            lnk3 = lst[2]-1
        
        else:
            while not rospy.is_shutdown(): 
                if lst[i] < loc[i]:
                    break
                pub[i].publish(math.radians(lst[i]))
                lst[i]-=1
                r.sleep()

                if i>0: #other than for the base angle we must stabilise end effector
                    end_effector +=1 
                    pub_end_effector.publish(math.radians(end_effector))
                    
            lnk1 = lst[0]+1
            lnk2 = lst[1]+1
            lnk3 = lst[2]+1



def debug():
    pass
    

#driver

while(True):
    print("""
    main menu
    ---------
      
        0) debug
        1) config
        2) goto l1
        3) goto l2
        4) goto l3
        5) pick up
        6) collect
        7) deposit
        8) adjust angles
        9) exit
              """)
    print(":",end = "")
        
    inp = input()
    if inp == "1":   # config
        lo1,lo2,lo3 = configure()
    elif inp == "2": # goto l1
        # pub_lnk1.publish(math.radians(lo1[0]))
        # pub_lnk2.publish(math.radians(lo1[1]))
        # pub_lnk3.publish(math.radians(lo1[2]))
        move_to(lo1)
    elif inp == "3": # goto l2
        # pub_lnk1.publish(math.radians(lo2[0]))
        # pub_lnk2.publish(math.radians(lo2[1]))
        # pub_lnk3.publish(math.radians(lo2[2]))
        move_to(lo2)
    elif inp == "4": # goto l3
        # pub_lnk1.publish(math.radians(lo3[0]))
        # pub_lnk2.publish(math.radians(lo3[1]))
        # pub_lnk3.publish(math.radians(lo3[2]))
        move_to(lo3)
    elif inp == "5":
        move_to(lo1)
    elif inp == "6":
        pass
    elif inp == "7":
        pass
    elif inp == "8":
        pass
    elif inp == "9":
        break
    elif inp == "0":
        pass

print("exiting menu...")












# while not rospy.is_shutdown():
#     print(":",end = '')
#     angle = math.radians(int(input()))
#     # angle = rospy.get_time() % 360 
#     # pub_end_effector.publish(angle)
#     # pub_lnk3.publish(angle)
#     pub_lnk2.publish(angle)
#     # pub_lnk1.publish(angle)
#     # pub_end_tip.publish(angle)
    
#     # count+=1
#     # if count == 100:
#     #     pub_end_slide_vel.publish(vel[int(bool)])
#     #     bool = not bool
#     #     count = 0
        
#     r.sleep()
