# D_Program
This two programs connect to the Delsys Devices.

Delsys_Communication_1_9 is a code made in python that helps to communicate with the Delsys device.
It uses TCP/IP communication. It has three ports for communication, port 50040 to manage and set up the Delsys device, port 50041 where is received the EMG data and port 50042 where is received the ACC data.
This code calls the ConnectionDelsys_1_1 to decode the frame and these can be readable for use.

ConnectionDelsys_1_1 is a code made in Python that helps to decode the data which comes from Delsys.
This code takes a 4-bytes frame and changes it to float numbers using IEEE float.

