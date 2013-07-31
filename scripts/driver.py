#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from serial import Serial
from struct import pack


def sensorStream():
    pub = rospy.Publisher('roomba_sensors', String)
    rospy.init_node('roomba_driver')
    rospy.loginfo( "Connecting to serial port")
    port = Serial('/dev/ttyAMA0', 57600, timeout = 5)
    rospy.loginfo( "Connected")
    opcodes = [128,148,2,29,13]
    data = pack('B'*len(opcodes), *opcodes)
    rospy.loginfo( "Sent Request")
    port.write(data)
    while not rospy.is_shutdown():
        data = port.read(8)
        pub.publish(String(data.encode("hex")))
    port.close()

if __name__ == '__main__':
    try:
        sensorStream()
    except rospy.ROSInterruptException:
        pass




