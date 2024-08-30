from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int32
#from sensor_pkg.msg import *
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
        # print('hx711->', hx711data.data)
        y22.append(y2[-1])
        try:
            if len(y1) > max_length:
                y1.pop(0) # delete the value whose index is 0, which means deleting the first element.
            if len(y22) > max_length:
                y22.pop(0)
        except:
            print('string is none!')


def callback2(sensor_data):
    y2.append(sensor_data.data)
    # y11.append(y1[-1])
    # try:
    #     if len(y11) > max_length:
    #         y11.pop(0) # delete the value whose index is 0, which means deleting the first element.
    #     if len(y2) > max_length:
    #         y2.pop(0)
    # except:
    #     print('string is none!')
    # ------------------------------------------

rospy.init_node('topic_subscriber_2_topics',anonymous=True)
# subscribe 2 topics
# 1, data from: send5kgdata.py
rospy.Subscriber('topic_publisher_5kg', Float32, callback1)
# 2. data from the seed hand sensors
rospy.Subscriber("topic_publisher_GTac_NUS", Float32, callback2)

def animate2(i):
    
    plt.cla()
    # plt.scatter(y11,y2)
    # plt.plot(y1,'r')
    # plt.scatter(y1,y22)
    plt.plot(y22, y1)
    # plt.plot(y22,'b')
    plt.ylim(0, 2500)
    # plt.xlim(0, 2600)
    plt.xlim(0, 4000)
    # plt.title('red---Load Cell Data,  blue---finger-fz data')
    plt.xlabel('Sensor Readings')
    plt.ylabel('Load Cell Readings')


# fig = plt.figure()
# # ani = FuncAnimation(plt.gcf(), animate, interval=1) # interval = 1 means that 'Delay between frames in 1 millisecond.' Default value is 200, but set to 1 here.
# ani = FuncAnimation(fig, animate, interval=1) # interval = 1 means that 'Delay between frames in 1 millisecond.' Default value is 200, but set to 1 here.

fig2 = plt.figure()
ani2 = FuncAnimation(fig2, animate2, interval=1) # interval = 1 means that 'Delay between frames in 1 millisecond.' Default value is 200, but set to 1 here.

plt.tight_layout()
plt.show()
