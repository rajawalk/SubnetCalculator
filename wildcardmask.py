#-------Wildcard---
import binascii
import struct
import sys
import numpy as np

def OrOperation(array1, array2):
    resultArray =  np.array([0,0,0,0])
    v=0
    for i in array1:
        resultArray[v] =array1[v] & array2[v]
        v=v+1
    return resultArray
def XorOperation(array1, array2):
    resultArray =  np.array([0,0,0,0])
    v=0
    for i in array1:
        resultArray[v] =array1[v] ^ array2[v]
        v=v+1
    return resultArray

v=0

print ("Choose \n 1)Normal mask \n 2)Discontiguous/Contiguous Wildcard Mask\n 0)Exit")
choice = raw_input("Enter Choice :")
if choice == "1":
    IP_string = raw_input("Enter IP address  : ")
    Mask_string = raw_input("Enter Mask Address: ")

    IP = np.array(IP_string.split("."))
    Mask = np.array(Mask_string.split("."))
    Mask = Mask.astype(int)
    IP = IP.astype(int)

    print ("-------------------------------------")
    print ("IP        :%s"%IP_string)
    print ("Mask      :%s"%Mask_string)

    resultArray =  np.array([0,0,0,0])
    """
        for i in IP:
            resultArray[v] = IP[v] & Mask[v]
            v = v+1"""
    resultArray = OrOperation(IP, Mask)
    resultArray_string = ".".join(str(x) for x in resultArray)
    print("NetworkID :%s"%resultArray_string)
    print ("-------------------------------------")

elif choice == "2":
    IP_string = raw_input("Enter IP address  : ")
    Mask_string = raw_input("Enter wildcard Mask Address: ")
    nwID_string = raw_input("Enter Network ID:")
    IP = np.array(IP_string.split("."))
    Mask = np.array(Mask_string.split("."))
    nwID = np.array(nwID_string.split("."))
    IP = IP.astype(int)
    Mask = Mask.astype(int)
    nwID = nwID.astype(int)
    fixedMask = np.array([255, 255, 255, 255])
    fixedMask = fixedMask.astype(int)
    print ("-------------------------------------")
    print ("IP            :%s"%IP_string)
    print ("WildcardMask  :%s"%Mask_string)

    Mask = XorOperation(fixedMask, Mask)
    CalNwID = OrOperation(IP, Mask)
    # print (nwID, CalNwID)
    
    if (nwID[0] == CalNwID[0]) and (nwID[1] == CalNwID[1]) and (nwID[2] == CalNwID[2]) and (nwID[3] == CalNwID[3]):
        print ("IP Address %s is in %s/%s"%(IP_string, nwID_string, Mask_string))
    else:
        print ("IP Address %s is NOT in %s/%s"%(IP_string, nwID_string, Mask_string))

elif choice == "0":
    sys.exit()
else:
    print ("Enter valid choice")
    sys.exit()

    #--- Test Code
"""
mask = np.array([255, 255, 240, 0])
mask = mask.astype(int)
fixedMask = np.array([255, 255, 255, 255])
fixedMask = fixedMask.astype(int)
wmask = np.array([0,0,0,0])

for i in mask:
    wmask[v] = mask[v] ^ fixedMask[v]
    v=v+1
print (wmask)

amask = np.array([0,0,0,0])
wmask = np.array([0,127,255,0])
wmask = wmask.astype(int)
v=0
for i in mask:
    amask[v] = wmask[v] ^ fixedMask[v]
    v=v+1
print (amask)
"""
