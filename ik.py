import math

x=float(input("enter x coordinate "))
y=float(input("enter y coordinate "))
z=float(input("enter z coordinate "))

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

theta_initial=math.degrees(math.atan(abs(y)/abs(x)))
quadrant = get_quadrant(x,y)
if quadrant==2:
    theta_initial=180-theta_initial
elif quadrant==3:
    theta_initial=180+theta_initial
elif quadrant==4:
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
    print(theta_initial,theta_mid_1,theta_final_1)
else:
    print(theta_initial,theta_mid_2,theta_final_2)
