# SIMULATION OF A NASOPHARYNGEAL SWAB COLLECTING ROBOTIC ARM

## CONFIGURATION

<i>
open four terminals and type in the following commands<br>
<br>

 <b>#terminal 1: launches gazebo</b><br>

cd ~/robotic_arm/catkin_ws<br>
source devel/setup.bash <br>
roslaunch robot_arm_iteration_3_description gazebo.launch<br>

<b>#terminal 2: launches the controllers</b><br>

cd ~/robotic_arm/catkin_ws<br>
source devel/setup.bash <br>
roslaunch robot_arm_iteration_3_description controller.launch<br>


(make sure the simulation inside gazebo is running)<br>

<b>#terminal 3: launches the rosnode</b><br>

cd ~/robotic_arm/flask_server<br>
python3 ~/robotic_arm/catkin_ws/src/robot_control/src/control.py<br>

 <b>#terminal 4: launches the flask server </b><br>

cd ~/robotic_arm/flask_server<br>
export FLASK_APP=flk.py<br>
export FLASK_ENV=development<br>
flask run --host=0.0.0.0<br>


<br>
(the flask server gives you an link open that in the browser)
</i>


<br>



## SPECS
ROS noetic was used.<br>
rosversion --all : details are present in "rosversion_details.txt"

<br>

[<b>sample video of simulation</b>](https://www.youtube.com/watch?v=KTm77U-Daog&list=PLR_FmEFFCB3JdIsf11Cr5g7DOb9cal-JV&index=35&t=249s&ab_channel=ebinjohny)




