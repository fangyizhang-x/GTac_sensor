from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int32
from sensor_pkg.msg import *
import math
display_length = 10000
max_length = 10000

y1 = [] # store load cell data
y2 = [] # store seed hand sensor data
y22 = []
y11 =[] # store the latest data from the y1
k = 4  # set the finger index to choose the specific finger to test

def callback1(hx711data):
    if len(y2) > 0:
        y1.append(hx711data.data)
        print('hx711->', hx711data.data)
        y22.append(y2[-1])
        try:
            if len(y1) > max_length:
                y1.pop(0) # delete the value whose index is 0, which means deleting the first element.
            if len(y22) > max_length:
                y22.pop(0)
        except:
            print('string is none!')


def callback2(sensor_data):
   
    # Initialize a list of lone_sensor messages to store the data that will be read
    sensor_values = [lone_sensor() for i in range(sensor_data.length)]

    if sensor_data.data[1].is_present == False: # Check if the sensor is present
        return # if not : set id to None, sensor will be displayed as "Sensor None"
    else:
        sensor_values = sensor_data.data  # If sensor is present, then copy the informations in the lone_sensor message
        # sum = math.sqrt(sensor_values[k].fx**2 + sensor_values[k].fy**2 + sensor_values[k].fz**2)
        # print("\t fx:{}, fy:{}, fz:{}, sum:{}\n".format(sensor_values[k].fx, sensor_values[k].fy, sensor_values[k].fz, sum))

    yt = abs(sensor_values[k].fz)/9.8
    y2.append(yt)

    # * Notice: below code shoud be placed inside the callback function 
    #   because callback function is faster then animate(i) function which will update 1ms.
    # ------------------------------------------
    y11.append(y1[-1])
    print('sensor---->', yt)
    try:
        if len(y11) > max_length:
            y11.pop(0) # delete the value whose index is 0, which means deleting the first element.
        if len(y2) > max_length:
            y2.pop(0)
    except:
        print('string is none!')
    # ------------------------------------------

rospy.init_node('topic_subscriber_2_topics',anonymous=True)
# subscribe 2 topics
# 1, data from: send5kgdata.py
rospy.Subscriber('topic_publisher_5kg', Float32, callback1)
# 2. data from the seed hand sensors
rospy.Subscriber("R_AllSensors", AllSensors, callback2)
# rospy.spin()

def animate(i):
    
    plt.cla()
    plt.plot(y11,'r')
    plt.plot(y2,'b')
    plt.ylim(0, 1200)
    plt.xlim(0, display_length)
    plt.title('red---Load Cell Data,  blue---finger-fz data')
    plt.xlabel('Time')
    plt.ylabel('red[g], blue[mN]')


def animate2(i):
    
    plt.cla()
    # plt.scatter(y11,y2)
    plt.scatter(y1,y22)
    # plt.plot(y2,'b')
    # plt.ylim(0, 1200)
    # plt.xlim(0, display_length)
    # plt.title('red---Load Cell Data,  blue---finger-fz data')
    # plt.xlabel('Time')
    # plt.ylabel('red[g], blue[mN]')

# fig = plt.figure()
# # ani = FuncAnimation(plt.gcf(), animate, interval=1) # interval = 1 means that 'Delay between frames in 1 millisecond.' Default value is 200, but set to 1 here.
# ani = FuncAnimation(fig, animate, interval=1) # interval = 1 means that 'Delay between frames in 1 millisecond.' Default value is 200, but set to 1 here.

fig2 = plt.figure()
ani2 = FuncAnimation(fig2, animate2, interval=1) # interval = 1 means that 'Delay between frames in 1 millisecond.' Default value is 200, but set to 1 here.

plt.tight_layout()
plt.show()
