#__author__ = 'MTabaz'
# import matplotlib.pyplot as plt
# import pylab
from datetime import datetime
# import numpy as np

hex_string = "0107911326040000F0040B911346610089F60000208062917314080CC8F71D14969741F977FD07"
#print datetime(02,8,26,19,37,41)
# print datetime.strptime("02-8-26 19:37:41","%y-%m-%d %H:%M:%S")
#
# x=[datetime.strptime("02-8-26 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-8-27 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-01 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-02 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-03 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-04 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-05 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-06 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-07 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-08 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-09 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-10 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-11 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-12 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-13 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-14 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-15 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-16 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-17 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-18 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-19 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-20 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-21 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-22 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-23 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-24 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-25 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-26 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-27 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-28 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-01 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-30 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-01 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-01 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-01 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-01 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-01 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-01 19:37:41","%y-%m-%d %H:%M:%S"),datetime.strptime("02-9-01 19:37:41","%y-%m-%d %H:%M:%S"),
#    datetime.strptime("02-9-01 19:37:41","%y-%m-%d %H:%M:%S")]

# x=["02-8-26 19:37:41","02-8-27 19:37:41",
#    "02-9-01 19:37:41",
#    "02-9-02 19:37:41","02-9-03 19:37:41",
#    "02-9-04 19:37:41","02-9-05 19:37:41",
#    "02-9-06 19:37:41","02-9-07 19:37:41",
#    "02-9-08 19:37:41","02-9-09 19:37:41",
#    "02-9-10 19:37:41","02-9-11 19:37:41",
#    "02-9-12 19:37:41","",
#    "02-9-14 19:37:41","02-9-15 19:37:41",
#    "","02-9-17 19:37:41",
#    "02-9-18 19:37:41","02-9-19 19:37:41",
#    "02-9-20 19:37:41","02-9-21 19:37:41",
#    "02-9-22 19:37:41","02-9-23 19:37:41",
#    "02-9-24 19:37:41","",
#    "02-9-26 19:37:41","02-9-27 19:37:41",
#    "02-9-28 19:37:41","02-9-01 19:37:41",
#    "02-9-30 19:37:41","",
#    "02-9-01 19:37:41","02-9-01 19:37:41",
#    "02-9-01 19:37:41","02-9-01 19:37:41",
#    "02-9-01 19:37:41","02-9-01 19:37:41",
#    "02-9-01 19:37:41"]
# y=[]
# for i in range(0,40):
#     y.append(i+1)
#
# for i in range(10,30):
#     y[i] = 0
#
# for i in range(10,30):
#     if i%2 == 0:
#         y[i] = i
#y = y[(y>=0) & (y<=40)]
# y.sort()
#y=[i for i in range(0,40)]

#plt.autoscale(False,'both')

# plt.plot(x,y,"ro")
# plt.show()
# beautify the x-labels

# fig = pylab.figure()
# ax = fig.gca()
# ax.set_autoscale_on(False)
#
# ax.plot(x,y)
# ax.axis([x[0],x[39],y[0],y[39]])

# fig.show()
#fig.savefig("test")


# pylab.figure(1)
# c = range(len(x))
# pylab.xticks(c, x)
# pylab.ylim([0,40])
# pylab.gcf().autofmt_xdate()
# pylab.plot(c,y,"g")
#
# pylab.show()

class SMSParser:
    def __init__(self):
        #Configuration Flags
        self.TP_VP_REL   = 0
        self.TP_VP_ABS   = 0
        self.STATUS_REP  = 0
        self.TP_MMS      = 0
        self.TP_RP       = 0
        self.SMS_SUBMIT_DELIEVER = 0

        self.binary_string = ""
        #Filters
        self.FILTER         = '00000001'
        # self.MASK_TWO       = 1
        # self.MASK_THREE     = 2
        # self.MASK_FOUR      = 3
        # self.MASK_FIVE      = 4
        # self.MASK_SIX       = 5
        # self.MASK_SEVEN     = 6
        # self.MASK_EIGHT     = 7
        # #Byte Size
        # self.TP_OA_SIZE     = 16
        # self.TP_PI_SIZE     = 8
        # self.TP_DCS_SIZE    = 8
        # self.TP_SCTS_SIZE   = 56
        # self.TP_UDL_SIZE    = 16

        self.SMSC_PLAN = {  0   :"Unknown",
                            1   :"ISDN/telephone numbering plan",
                            3   :"Data numbering plan",
                            4   :"T elex numbering plan",
                            5   :"Service Centre Specific",
                            6   :"Service Centre Specific",
                            8   :"National numbering plan",
                            9   :"Private numbering plan",
                            10  :"ERMES numbering plan"}
        self.SMSC_TYPE = {  8   :"Unknown",
                            9   :"International number",
                            10  :"National number",
                            11  :"Network specific number",
                            12  :"Subscriber number",
                            13  :"Alphanumeric",
                            14: "Abbreviated number",
                            15: "Reserved"}
        self.SMS_SUBMIT = {
            "TP_SMSC_LENGTH"    : 0, #SMS centre length
            "TP_SMSC_TYPE"      : 0, #SMS centre number type
            "TP_SMSC"           : 0, #SMS centre number
            "TP_DA_LENGTH"      : 0, #Destination address length
            "TP_DA_TYPE"        : 0, #Destination address Type
            "TP_DA"             : 0, #Destination address
            "TP_VP"             : 0, #SMS vaild period
            "TP_DATA_LENGTH"    : 0, #User data length
            "TP_DATA"           : 0, #Contain SMS data
        }
        self.SMS_DELIEVER = {
            "TP_SMSC_LENGTH"    : 0, #SMS centre length
            "TP_SMSC_TYPE"      : 0, #SMS centre number type
            "TP_SMSC"           : 0, #SMS centre number
            "TP_SA_LENGTH"      : 0, #Source address length
            "TP_SA_TYPE"        : 0, #Source address Type
            "TP_DA"             : 0, #Source address
            "TP_SCTS"           : 0, #SMS Timestamp
            "TP_DATA_LENGTH"    : 0, #User data length
            "TP_DATA"           : 0, #Contain SMS data
        }
        
    def GetBinaryStrig(self,hexformat):
        binaryformat = ''
        for i in range(0,len(hexformat)):
            binaryformat += "{0:04b}".format(int(hexformat[i],16))
        return binaryformat

    def GetSMSConfig(self,binary):
        index = 0
        Flag = [0,0,0,0,0,0,0,0]
        Filter = ''
                
        while index < 8:
            Filter = int(binary,2)>>index & int(self.FILTER,2)
            Flag[index] = Filter
            index += 1
        if Flag[4] == 1 and Flag[3] == 1:
            self.TP_VP_ABS = 1
        elif Flag[4] == 1 and Flag[3] == 0:
            self.TP_VP_REL = 1

        self.STATUS_REP = Flag[5]
        self.TP_MMS     = Flag[2]
        self.TP_RP      = Flag[7]
        self.TP_UDHI    = Flag[6]

    def GetTimeStamp(self,hex_string):
        timestamp = ''
        #print hex_string
        for i in range(0,12,2):
            timestamp += hex_string[i+1]+hex_string[i]
            if i == 4:
                timestamp += " "
            elif i < 5:
                timestamp += "-"
            elif i < 10:
                timestamp += ":"
        timeZone = hex_string[13]+hex_string[12]
        #print timestamp
        #print "Timestamp: " + str(datetime.strptime(timestamp,"%y-%m-%d %H:%M:%S"))
        #return str(datetime.strptime(timestamp,"%y-%m-%d %H:%M:%S")) #+ " GMT+" + timeZone
        return datetime.strptime(timestamp,"%y-%m-%d %H:%M:%S") #+ " GMT+" + timeZone

    def GetNumberType(self,string,hex_string):
        print string +": "+ self.SMSC_TYPE[int(hex_string[0])]+", "+ self.SMSC_PLAN[int(hex_string[1])]

    def SMSDetails(self,hex_string):
        binary_string = self.GetBinaryStrig(hex_string[0:2])
        self.GetSMSConfig(binary_string)
        
        SMS_OBJ = 0

        if int(binary_string,2) == 1 or int(binary_string,2) == 3:
            SMS_OBJ = [self.SMS_DELIEVER]
        else:
            SMS_OBJ = [self.SMS_SUBMIT]
        
        SMS_OBJ[0]["TP_SMSC_LENGTH"]   = hex_string[2:4]
        SMS_OBJ[0]["TP_SMSC_TYPE"]     = hex_string[4:6]
        
        # self.GetNumberType("SMSC Number",SMS_OBJ[0]["TP_SMSC_TYPE"])
        endofSMSC = (int(SMS_OBJ[0]["TP_SMSC_LENGTH"],16)-1)*2
        SMS_OBJ[0]["TP_SMSC"] = hex_string[6:(6+endofSMSC)]
        
        SMS_OBJ[0]["TP_SA_LENGTH"]   = hex_string[(8+endofSMSC):(10+endofSMSC)]
        SMS_OBJ[0]["TP_SA_TYPE"]     = hex_string[(10+endofSMSC):(12+endofSMSC)]
        if (int(SMS_OBJ[0]["TP_SA_LENGTH"],16) % 2) == 0:
            counter = 12+endofSMSC+int(SMS_OBJ[0]["TP_SA_LENGTH"],16)
        else:
            counter = 12+endofSMSC+int(SMS_OBJ[0]["TP_SA_LENGTH"],16)+1
        SMS_OBJ[0]["TP_SA"] = hex_string[(12+endofSMSC):counter]
        # self.GetNumberType("Source Number",SMS_OBJ[0]["TP_SA_TYPE"])
        # SMS_OBJ[0]["TP_PID"] = hex_string[(counter):(counter+2)]
        # SMS_OBJ[0]["TP_DCS"] = hex_string[(counter+2):(counter+4)]
        SMS_OBJ[0]["TP_SCTS"] = self.GetTimeStamp(hex_string[(counter+4):(counter+18)])
        #print hex_string[(counter+4):(counter+18)]
        return SMS_OBJ[0]["TP_SCTS"]
        
        
# SMS = SMSParser()
# SMS.SMSDetails(hex_string)
        