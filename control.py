import rospy
from std_msgs.msg import Float64

rospy.init_node('control')
pub = rospy.Publisher('/robot_arm_iteration_3/Rev13_position_controller/command', Float64, queue_size=10)
r = rospy.Rate(100)


while not rospy.is_shutdown():
    angle = rospy.get_time() % 360
    pub.publish(angle)
    r.sleep()
