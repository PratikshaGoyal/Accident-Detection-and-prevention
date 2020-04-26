import FaBo9Axis_MPU9250
import time
import sys
import nearby_places

mpu9250 = FaBo9Axis_MPU9250.MPU9250()

try:
    while True:
        accel = mpu9250.readAccel()
        ax = accel['x']
        ay = accel['y']
        az = accel['z']

        # print(" ax = " ,accel['x'])
        # print(" ay = " ,accel['y'])
        # print(" az = " ,accel['z'])

        # gyro = mpu9250.readGyro()
        # print(" gx = " ,gyro['x'])
        # print(" gy = " ,gyro['y'])
        # print(" gz = " ,gyro['z'])

        # mag = mpu9250.readMagnet()
        # print(" mx = " ,mag['x'])
        # print(" my = " ,mag['y'])
        # print(" mz = " ,mag['z'])
        # print("\n\n\n")

        time.sleep(0.1)

        if ax[0] == "-" and ay[0] =="-" and az[0] == "-":
            nearby_places.nearby()
            break   


except KeyboardInterrupt:
    sys.exit()
