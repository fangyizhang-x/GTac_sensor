from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import rospy
from std_msgs.msg import Float32, Float32MultiArray
import math
display_length = 1000
max_length = 800

y1 = [] # store sensor 1
y11 =[]

y2 = [] # store sensor 2
y22 = []
k = 4

y3 = [] # store sensor 1
y4 = [] # store sensor 1

def callback(gtacdata):
    
    y1.append(gtacdata.data[1])
    y2.append(gtacdata.data[2])
    y3.append(gtacdata.data[7])
    y4.append(gtacdata.data[8])
    print(gtacdata.data[0], gtacdata.data[6])
    try:
        if len(y1) > max_length:
            y1.pop(0) # delete the value whose index is 0, which means deleting the first element.
        if len(y2) > max_length:
            y2.pop(0)
        if len(y3) > max_length:
            y3.pop(0)
        if len(y4) > max_length:
            y4.pop(0)
    except:
        print('string is none!')

rospy.init_node('topic_subscriber_2_topics',anonymous=True)
# subscribe 2 topics
# 1, data from: send5kgdata.py
rospy.Subscriber('gtac2023', Float32MultiArray, callback)

def animate(i):
    
    plt.cla()
    plt.plot(y1,'r')#force
    plt.plot(y2,'g')#x
    plt.plot(y3,'b')#y
    plt.plot(y4,'y')#z
    plt.ylim(0, 300)
    plt.xlim(0, display_length)
    plt.title('Gtac Sensor')
    plt.xlabel('Time')
    plt.ylabel('Normal Force')


# fig = plt.figure()
# # ani = FuncAnimation(plt.gcf(), animate, interval=1) # interval = 1 means that 'Delay between frames in 1 millisecond.' Default value is 200, but set to 1 here.
# ani = FuncAnimation(fig, animate, interval=1) # interval = 1 means that 'Delay between frames in 1 millisecond.' Default value is 200, but set to 1 here.

fig2 = plt.figure()
ani2 = FuncAnimation(fig2, animate, interval=1) # interval = 1 means that 'Delay between frames in 1 millisecond.' Default value is 200, but set to 1 here.

plt.tight_layout()
plt.show()
