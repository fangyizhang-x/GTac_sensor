from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import rospy
from std_msgs.msg import Float32, Float32MultiArray
from xela_server.msg import xServerMsg

import math
display_length = 1000
max_length = 800

y1 = [] # store sensor 1
y2 = [] # store sensor 2
shear1=[]
shear2=[]
k = 4

def callback(data):
    y1.append(data.data[0])
    y2.append(data.data[6]+1000)
    shear1.append(data.data[1]+2000)
    shear2.append(data.data[2]+2500)

    try:
        if len(y1) > max_length:
            y1.pop(0)
        if len(y2) > max_length:
            y2.pop(0)
        if len(shear1) > max_length:
            shear1.pop(0)
        if len(shear2) > max_length:
            shear2.pop(0)
    except:
        print('string is none!')

rospy.init_node('node_GTac_nus',anonymous=True)
rospy.Subscriber('/gtac_force', Float32MultiArray, callback)

def animate(i):
    
    plt.cla()
    plt.plot(y1,'r')
    plt.plot(y2,'b')
    plt.plot(shear1,'r--')
    plt.plot(shear2,'b--')
    plt.ylim(0, 3500)
    plt.xlim(0, display_length)
    plt.title('Gtac Sensor')
    plt.xlabel('Time')
    plt.ylabel('Force')


fig2 = plt.figure()
ani2 = FuncAnimation(fig2, animate, interval=1) # interval = 1 means that 'Delay between frames in 1 millisecond.' Default value is 200, but set to 1 here.

plt.tight_layout()
plt.show()