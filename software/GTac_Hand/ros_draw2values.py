from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int32
#from sensor_pkg.msg import *
import math
display_length = 500
max_length = 400

y1 = [] # store load cell data
y2 = [] # store seed hand sensor data
y11 =[] # store the latest data from the y1
k = 4  # set the finger index to choose the specific finger to test

def callback1(hx711data):
    y1.append(hx711data.data)
    # print('hx711->', hx711data.data)


def callback2(sensor_data):
    y2.append(sensor_data.data)
    if len(y1)>0:
        y11.append(y1[-1])
        try:
            if len(y11) > max_length:
                y11.pop(0) # delete the value whose index is 0, which means deleting the first element.
            if len(y2) > max_length:
                y2.pop(0)
        except:
            print('string is none!')
    # ------------------------------------------

rospy.init_node('node_subscriber_2_topics_Gtac_NUS',anonymous=True)
# subscribe 2 topics
# 1, data from: send5kgdata.py
rospy.Subscriber('topic_publisher_5kg', Float32, callback1)
# 2. data from the seed hand sensors
rospy.Subscriber("topic_publisher_GTac_NUS", Float32, callback2)
# rospy.spin()

def animate(i):
    
    plt.cla()
    plt.plot(y11,'r')
    plt.plot(y2,'b')
    plt.ylim(-10, 4000)
    plt.xlim(0, display_length)
    plt.title('red---Load Cell Data,  blue---Normal Force Signal, FA-I Sum')
    plt.xlabel('Time')
    plt.ylabel('red[ g ], blue[ unknown ]')

ani = FuncAnimation(plt.gcf(), animate, interval=1) # interval = 1 means that 'Delay between frames in 1 millisecond.' Default value is 200, but set to 1 here.
plt.tight_layout()
plt.show()
