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
prev_end_effector = end_effector

lo1 = [30 , 70 , -70] #pick up 
lo2 = [-90 , 45 , -90] #collection 
lo3 = [90 , 0 , -45] #deposit

state = 0

def read_data():
    print("reading data")
    f = open("/home/jayee/flask_server/communication.txt","r",)
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
    f = open("/home/jayee/flask_server/communication.txt","w")
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


def inverse_kinematics(lo):
    # x=float(input("enter x coordinate "))
    # y=float(input("enter y coordinate "))
    # z=float(input("enter z coordinate "))

    x = lo[0]
    y = lo[1]
    z = lo[2]

    base_height=100              #base height in cm(link 1)
    l1=float(50)                 #length of link 2 in cm    
    l2=float(50)                 #length of link 3 in cm

    def get_quadrant(x,y): 
        if(x>=0 and y>=0):
            return 1
        elif(x>=0 and y<0):
            return 4
        elif(x<0 and y>=0):
            return 2
        else:
            return 3

    if x!=0:
        theta_initial=math.degrees(math.atan(abs(y)/abs(x)))
    elif y>0:
        theta_initial=90
    else:
        theta_initial=-90

    quadrant = get_quadrant(x,y)
    if quadrant==2:
        theta_initial=180-theta_initial
    elif quadrant==3:
        theta_initial=180+theta_initial
    elif quadrant==4:
        theta_initial=360-theta_initial
        
    theta_initial=theta_initial%360
    if theta_initial>180:
        theta_initial=360-theta_initial  

    x2=float(math.sqrt(x*x+y*y))
    y2=float(z-base_height)

    #print(x2,y2)


    d=math.sqrt(x2*x2+y2*y2)
    k=float((l1*l1+l2*l2-d*d)/(2*l1*l2))

    #print(k)
    #print(d)
    #print(type(d))

    theta_final_1= math.acos(-1*k)
    #theta_final_1= math.pi-theta_final_1
    theta_final_2=-1*math.acos(-1*k)

    theta_mid_1=math.degrees(math.atan(y2/x2)-math.atan(l2*math.sin(theta_final_1)/(l1+l2*math.cos(theta_final_1))))
    theta_mid_2=math.degrees(math.atan(y2/x2)+math.atan(l2*math.sin(theta_final_1)/(l1+l2*math.cos(theta_final_1))))

    #print("x2,y2 ->",x2,y2)
    #print("theta_initial -> ",theta_initial) #theta 1
    #print("theta mid -> ",theta_mid_1,theta_mid_2) #theta 2 
    #print("theta mid for MATLAB",theta_mid_1-90,theta_mid_2-90) #-90 is added as compensation (alt theta 2)
    #print("theta final -> ",math.degrees(theta_final_1),math.degrees(theta_final_2)) #theta 3

    theta_final_1=math.degrees(theta_final_1)
    theta_final_2=math.degrees(theta_final_2)

    diff1=abs(-90-theta_mid_1)
    diff2=abs(-90-theta_mid_2)

    if diff1>diff2:
        #print(theta_initial,theta_mid_1,theta_final_1)
        return([theta_initial,theta_mid_1,theta_final_1])
    else:
       # print(theta_initial,theta_mid_2,theta_final_2)
       return([theta_initial,theta_mid_2,theta_final_2])




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

        lo1 = inverse_kinematics(lo1)

        lo2[0] = float(lst[4])
        lo2[1] = float(lst[5])
        lo2[2] = float(lst[6])

        lo2 = inverse_kinematics(lo2)

        lo3[0] = float(lst[7])
        lo3[1] = float(lst[8])
        lo3[2] = float(lst[9])

        lo3 = inverse_kinematics(lo3)

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

    elif inp == 5: #pickup
        state = 5
        move_end_effector(-lnk2-lnk3)
        pub_end_slide_vel.publish(-0.1)
        time.sleep(3)
        pub_end_slide_vel.publish(0.1)
        time.sleep(1)
        move_end_effector(-lnk2-lnk3+90)
        
    elif inp == 6: #collection operation
        state = 6
        #move_end_effector(prev_end_effector)
        pub_end_slide_vel.publish(-0.1)
        time.sleep(1)
        count = 0 
        while count<360:
            count+=1
            pub_end_tip.publish(math.radians(count))
            end_tip = count
            r.sleep()
        time.sleep(4)
        #add a twist operation here
        pub_end_slide_vel.publish(0.1)
        time.sleep(1)
        move_end_effector(-lnk2-lnk3+90)
        
    elif inp == 7: #deposition operation
        state = 7
        move_end_effector(-lnk2-lnk3-90)
        pub_end_slide_vel.publish(-0.1)
        time.sleep(3)
        pub_end_slide_vel.publish(0.1)
        time.sleep(1)
        move_end_effector(-lnk2-lnk3+90)
        
    elif inp == 8: #adjust angles
        state = 8
        
        
        for i in range(1,5):
            ang = int(lst[i])
            if i == 1 :
                lnk1+=ang*3
            elif i == 2:
                lnk2+=ang*3
            elif i == 3:
                lnk3+=ang*3
            elif i == 4:
                end_effector+=ang*3

            lo2=[lnk1,lnk2,lnk3]
            prev_end_effector = end_effector

            pub_lnk1.publish(math.radians(lnk1))
            pub_lnk2.publish(math.radians(lnk2))
            pub_lnk3.publish(math.radians(lnk3))
            pub_end_effector.publish(math.radians(end_effector))

    elif inp == 9: #goto previous end effector angle
        state = 9
        move_end_effector(prev_end_effector)

    elif inp == 0:
        state = 0


    elif inp == 0:
        state = 0
        

    if inp!=0:
        refresh()
    print(inp)
    time.sleep(1)