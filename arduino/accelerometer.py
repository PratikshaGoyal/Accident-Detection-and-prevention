#!/usr/bin/env python
# coding: utf-8

import serial
from googleplaces import GooglePlaces, types, lang 
from twilio.rest import Client 
import nearby_places


serial_port = 'COM10';
baud_rate = 115200; #In arduino, Serial.begin(baud_rate)
write_to_file_path = "F:/output.txt";

output_file = open(write_to_file_path, "a+");
ser = serial.Serial(serial_port, baud_rate)
while True:
    line = ser.readline();
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    line = line.split(" ")
    count=0
    for i in line:
        print(i)
        if i[0]=='-':
            count+=1
        if count == 3:
            nearby_places.nearby()
            break
    
    output_file.write(i);

