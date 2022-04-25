#!/usr/bin/env python3
import time
import rospy
from std_msgs.msg import Float64
import math

pub_end_effector = rospy.Publisher('/robot_arm_iteration_3/Rev10_position_controller/command', Float64, queue_size=1)
pub_lnk3 = rospy.Publisher('/robot_arm_iteration_3/Rev11_position_controller/command', Float64, queue_size=1)
pub_lnk2 = rospy.Publisher('/robot_arm_iteration_3/Rev12_position_controller/command', Float64, queue_size=1)
pub_lnk1 = rospy.Publisher('/robot_arm_iteration_3/Rev13_position_controller/command', Float64, queue_size=1)
pub_end_tip = rospy.Publisher('/robot_arm_iteration_3/Rev15_position_controller/command', Float64, queue_size=1)
pub_end_slide_vel = rospy.Publisher('/robot_arm_iteration_3/Slider14_position_controller/command', Float64, queue_size=1)

end_effector = 90
lnk3 = 0
lnk2 = 0
lnk1 = 0
end_tip = 0
end_slide_vel = 0 #can be -0.1(deploy) or 0.1(retract)
vel = [0.1,-0.1]

lo1 = [30 , 70 , -70] #pick up 
lo2 = [-90 , 45 , -90] #collection 
lo3 = [90 , 0 , -45] #deposit

state = 0

def read_data():
    print("reading data")
    f = open("/home/jayee/Desktop/project/prototyping stuff/communication.txt","r",)
    lst = []
    for i in f:
        lst.append(i)
    f.close()
    print(lst)
    return lst

def get_data():

    complete = False
    while not complete :
        try:
            lst = read_data()
        except:
            pass
        else:
            complete = True
        #time.sleep(1)
    #print(lst)
    return lst


def move_to(loc): #input in degrees
    global lnk1,lnk2,lnk3,end_effector
    lst = [lnk1,lnk2,lnk3]
    pub = [pub_lnk1,pub_lnk2,pub_lnk3]
    

    for i in range(3): # i = 0 lnk1 , i =1 lnk2 , i = 2 lnk 3
        temp = loc[i]-lst[i] #target - current location 
        if temp>0:
            while not rospy.is_shutdown():
                lst[i]+=1 
                if lst[i] > loc[i]:
                    break
                pub[i].publish(math.radians(lst[i]))
                
                if i>0 and not lst[i] > loc[i]: #other than for the base angle we must stabilise end effector
                    end_effector -=1 
                    pub_end_effector.publish(math.radians(end_effector))
                    

                r.sleep()

            lnk1 = lst[0]-1
            lnk2 = lst[1]-1
            lnk3 = lst[2]-1
        
        else:
            
            while not rospy.is_shutdown(): 
                if lst[i] < loc[i] :
                    break

                pub[i].publish(math.radians(lst[i]))
                lst[i]-=1
                r.sleep()

                if i>0 and not lst[i] < loc[i]: #other than for the base angle we must stabilise end effector
                    end_effector +=1 
                    pub_end_effector.publish(math.radians(end_effector))
                    
            lnk1 = lst[0]+1
            lnk2 = lst[1]+1
            lnk3 = lst[2]+1





def move_end_effector(ang):
    global end_effector
    
    while not rospy.is_shutdown():
        temp =  ang - end_effector
        
        if temp>0:
            end_effector += 1
        elif temp<0:
            end_effector -= 1
        else :
            break
        pub_end_effector.publish(math.radians(end_effector))
        r.sleep()


def write_data():
    f = open("/home/jayee/Desktop/project/prototyping stuff/communication.txt","w")
    f.write('0\n')
    f.close()

    

def refresh():
    complete = False
    while not complete :
        try:
            write_data()
        except:
            pass
        else:
            complete = True
    print("refreshed")




rospy.init_node('control')
pub = rospy.Publisher('/robot_arm_iteration_3/Rev13_position_controller/command', Float64, queue_size=10)
r = rospy.Rate(100)



while True:
    
    lst = get_data()
    inp = int(lst[0])
     
    if inp == 1:   # config
        #lo1,lo2,lo3 = configure()
        
        lo1[0] = float(lst[1])
        lo1[1] = float(lst[2])
        lo1[2] = float(lst[3])

        lo2[0] = float(lst[4])
        lo2[1] = float(lst[5])
        lo2[2] = float(lst[6])

        lo3[0] = float(lst[7])
        lo3[1] = float(lst[8])
        lo3[2] = float(lst[9])

        state = 1
        #break
        
    elif inp == 2: # goto l1
        state = 2
        move_to(lo1)
    elif inp == 3: # goto l2
        state = 3
        move_to(lo2)
    elif inp == 4: # goto l3
        state = 4
        move_to(lo3)

    elif inp == 5:
        state = 5
        move_end_effector(-lnk2-lnk3)
        pub_end_slide_vel.publish(-0.1)
        time.sleep(1)
        pub_end_slide_vel.publish(0.1)
        time.sleep(1)
        move_end_effector(-lnk2-lnk3+90)
        
    elif inp == 6:
        state = 6
        move_end_effector(-lnk2-lnk3+45)
        pub_end_slide_vel.publish(-0.1)
        time.sleep(1)
        pub_end_slide_vel.publish(0.1)
        time.sleep(1)
        move_end_effector(-lnk2-lnk3+90)
        
    elif inp == 7:
        state = 7
        move_end_effector(-lnk2-lnk3-90)
        pub_end_slide_vel.publish(-0.1)
        time.sleep(1)
        pub_end_slide_vel.publish(0.1)
        time.sleep(1)
        move_end_effector(-lnk2-lnk3+90)
        
    elif inp == 8: #adjust angles
        state = 8
        
        
    elif inp == 0:
        state = 0
        

    if inp!=0:
        refresh()
    print(inp)
    time.sleep(1)
