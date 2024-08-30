# import the opencv library
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

# define a video capture object
# check the USB camera port number and then congifure the VideoCapture number
# v4l2-ctl --list-devices
# UVC Camera (046d:0990) (usb-0000:00:14.0-4):
# 	/dev/video0
# 	/dev/video1


vid = cv2.VideoCapture(6)
cv_bridge = CvBridge()


rospy.init_node('video_publisher')
pub = rospy.Publisher('sensor_camera_16june', Image, queue_size=10)


while not rospy.is_shutdown():
	
	# Capture the video frame
	# by frame
    ret, frame = vid.read()
    
    
    if ret:
        # Convert the OpenCV frame to a ROS Image message
        image_msg = cv_bridge.cv2_to_imgmsg(frame, "bgr8")
        # image_msg = Image()
        image_msg.header.stamp = rospy.Time.now()
        # image_msg.width = frame.shape[1]
        # image_msg.height = frame.shape[0]
        # image_msg.encoding = 'bgr8'
        # image_msg.data = frame.tobytes()
        # print(">> send")
        # Publish the message
        
        pub.publish(image_msg)
	
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

# rosbag record /camera/color/image_raw /sensor_camera_16june /sensor_data_16june

# ******** open camera 1 ********
# roslaunch realsense2_camera rs_camera.launch
# rosrun image_view image_view image:=/camera/color/image_raw

# ******** open camera 2 ********
# rosrun image_view image_view image:=/sensor_camera_16june

# data: "997.11,1028.09,480,126,220,-744,439,1296,659,-1917,-374,1875,-604,112,300,-2213,-885,-2226,-700,-1037,1762,806,-178,-1049,25,278,-1430,17,-230,548,-2708,-26,-340,223,477,443,295,741,97,-342,-349,571,-1087,-1125,1856,838,81"
# data: "1952.24,1805.98,383,639,796,-325,938,1765,405,-1301,-1490,1146,-347,-329,305,-2596,-347,-1348,-533,-1256,1570,848,-56,-898,260,320,-1271,-87,-151,48,83,278,-389,540,604,367,605,733,97,-458,-206,561,-1754,-1090"
# data: "1932.44,1844.47,439,1591,562,-419,1240,1139,287,-937,-1210,1539,383,-850,-128,-2157,-1265,-1656,-250,-814,1505,819,73,-891,256,391,-1408,-73,154,288,41,0,-362,706,786,323,408,731,110,-367,-153,482,-1631,-912"