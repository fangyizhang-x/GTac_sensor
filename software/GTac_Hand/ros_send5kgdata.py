# from itertools import count
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import serial
# import rospy
# from std_msgs.msg import String

# rospy.init_node('topic_publisher_5kg_',anonymous=True)

# ser = serial.Serial('/dev/ttyUSB2', 9600)

# pub = rospy.Publisher('topic_publisher_5kg', String, queue_size=10)

# while not rospy.is_shutdown():
#     data_orginal = ser.readline()  # read data from serial port and decode i
#     data = data_orginal.decode('utf-8').strip()
#     print('data-original:',type(data_orginal))
#     print('data: ',type(data))
    
#     pub.publish(data)
#     print('data->', data)


from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial
import rospy
from std_msgs.msg import Float32

rospy.init_node('topic_publisher_5kg_',anonymous=True)

ser = serial.Serial('/dev/ttyUSB0', 9600)

pub = rospy.Publisher('topic_publisher_5kg', Float32, queue_size=10)

while not rospy.is_shutdown():
    data_orginal = ser.readline()  # read data from serial port and decode i
    data = data_orginal.decode('utf-8').strip()
    # print('data-original:',type(data_orginal))
    # print('data: ',type(data))
    a = float(data)
    pub.publish(a)
    # print('data->', type(a))
    print('data->', a)