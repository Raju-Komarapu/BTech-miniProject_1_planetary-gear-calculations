import time
print("\n\n----------PLANETARY GEAR SELECTION AND CALCULATIONS TOOL----------\n")
time.sleep(2)
print("The following parameters must be known to select the correct Gearbox : \n")
time.sleep(1)
print("1. Torque to be transmitted (output torque)")
time.sleep(1)
print("2. Motor Power (kW)")
time.sleep(1)
print("3. Input speed (RPM)")
time.sleep(1)
print("4. Output speed (RPM)")
time.sleep(1)
print("4. Service Factor")
time.sleep(1)
print("5. Rated_Torque (Nm)")
time.sleep(2)
print("\nThe Tool will navigate through all the required steps :)\n")
time.sleep(2)
input("----------Press Enter to Start----------")
print("Step 1: Select the reduction ratio\n")
time.sleep(1.5)
print("The reduction ratio can be calculated as Input Speed/Output Speed.\nIf the output torque is not known then the torque can be calculated")
time.sleep(1.5)
Input = int(input("\nEnter Input Speed : "))
Output = int(input("Enter Output Speed : "))
print("\nEntered values are ", Input,Output)
time.sleep(1)
check = input("\nDo you know the output torque ? \nType 'YES' If known or type 'NO' to calculate the output torque : ")
if check == "YES":
    time.sleep(2)
    Torque = int(input("\nEnter the torque in N-m : "))
else:
    time.sleep(1)
    print("\n--------Output Torque calculation-------- \n")
    time.sleep(1.5)
    print("Output Torque = (P*9546)/N \nwhere P is power in KW and N is output speed in RPM\n")
    time.sleep(0.5)
    power = int(input("Enter power in KW : "))
    Torque = (power*9546)/Output
    print("Output torque calculated is : " ,Torque , "Nm")
    time.sleep(2)
print("\n-----Step 2: Find the service factor-----")
time.sleep(2)
print("Depending upon the type of application and working hours assume the service factor.")
hours = int(input("\nEnter the working hours of gearbox per day : "))
load = input("Enter type of load? (uniform/medium shock/heavy shock) : ")
if hours <= 2:
    if load == "uniform":
        sf = 1.0
    elif load == "medium shock":
        sf = 1.3
    elif load == "heavy shock":
        sf = 1.6
if hours > 2 and hours <=10 :
    if load == "uniform":
        sf = 1.3
    elif load == "medium shock":
        sf = 1.6
    elif load == "heavy shock":
        sf = 1.8
if hours > 10 :
    if load == "uniform":
        sf = 1.6
    elif load == "medium shock":
        sf = 1.8
    elif load == "heavy shock":
        sf = 2.0
time.sleep(2)
print("\nService factor = ",sf)
time.sleep(1.5)
print("\n------Step 3 : Calculating Rated Torque------ \n\nRated Torque = Calculated output torque * service factor")
time.sleep(1.5)
rated_torque = Torque*sf
print("\nRated Torque is : ", rated_torque,"Nm")
time.sleep(2)
print("Following parameters are calculated using the tool : \n\n")
time.sleep(1)
print("Speed of Input Shaft : ",Input,"rpm\n")
time.sleep(1)
print("Speed of Output Shaft : ",Output,"rpm\n")
time.sleep(1)
print("Power transmitted : ",power,"KW\n")
time.sleep(1)
print("Power transmitted : ",power,"KW\n")
time.sleep(1)
print("Output torque : ",Torque,"Nm\n")
time.sleep(1)
print("Service factor : ",sf,"\n")
time.sleep(1)
print("Rated Torque : ",rated_torque,"Nm\n")
time.sleep(1)
print("Power transmitted : ",power,"KW")
print("\n\n-----------Thank You-----------")