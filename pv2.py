#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     30/06/2023
# Copyright:   (c) User 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
import time
from inputimeout import inputimeout
cloudcover=""
C1="df"
C2=""
C3=""
C4=""
#def frontend_initial():
#FINAL_METAR="ABCD"
def backend():
    import socket
    UDP_IP = "192.168.103.150"
    UDP_PORT = 5000
    sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP, UDP_PORT))


    while True:

        def frontend():

            while True:
                FINAL_METAR=""
                root=Tk()
                #function to proceed after enterinf the timestamp
                cloudcover=""
                output=Label(root,text="Enter the four cloud terms")
                output.pack()
                e2=Entry(root)
                e2.pack()
                e3=Entry(root)
                e3.pack()
                e4=Entry(root)
                e4.pack()
                e5=Entry(root)
                e5.pack()
                C1=e2.get()
                C2=e3.get()
                C3=e4.get()
                C4=e5.get()
                cloudcover=C1+C2+C3+C4
                def onclic():
                    time.sleep(10)
                    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
                    runway_number=data[10:12]
                    GST_Time=data[22:30]
                    Date=data[31:42]
                    WS_10_min=data[63:66]
                    WD_10_min=data[86:88]
                    Hum_10_min=data[104:106]
                    Temp_10_min=data[131:136]
                    DP_10_min=data[155:160]
                    Pres_10_min=data[183:188]
                    QNH_10_min=data[217:223]
                    QFE_10_min=data[246:251]
                    #declaring all the components of the final METAR Report
                    METAR=""
                    report=" "
                    typ = "METAR"
                    #-----------------------------------------------------------------------
                    #Taking the timestamp for which the user wants the METAR
                    #Finding the row in the given data which has to be accessed
                    #row=0
                    #for i in range(25):
                    #    if time==df.iloc[i,3]:
                    #        row=i
                    #---------------------------------------------------------------------------

                    #Taking the four terms of cloud cover
                    #cell_value = df.iloc[row, 28] # cell_value = df.iloc[row_index, column_index]
                    #pressure=('Q -',cell_value)
                    #---------------------------------------------------------------------------

                    #status term which comprises of date,and time in zulu
                    time1=""
                    date=""
                    def status():
                        #runway=(df.iloc[row,2])
                        time_used=GST_Time
                        if time_used[3]==':':time1='0'+time_used[2]+time_used[4]+time_used[5]
                        else:time1=time_used[2]+time_used[3]+time_used[5]+time_used[6]
                        check=Date
                        if check[1]=='-':date='0'+check[0]
                        else: date=check[0]+check[1]
                        #print(date)
                        print(date+time1)
                        return date+time1
                        #---------------------------------------------------------------------------
                    #temp and dew point temp component
                    temp =Temp_10_min
                    dew_pt = DP_10_min
                    finaltempdew = str(temp) + '/' + str(dew_pt)
                    print(finaltempdew)
                    report=str(report)+str(status())+'Z'
                    FINAL_METAR=str(typ)+report+str(cloudcover)+" "+finaltempdew
                    print(FINAL_METAR)
                    myLabel=Label(root,text=FINAL_METAR+""+cloudcover)
                    myLabel.pack()
            #root=Tk()
            #myLabel=Label(root,text=FINAL_METAR)
            #myLabel.pack()
                new_button=Button(root,text="OK",command=onclic)
                new_button.pack()
                #def perform():
                   # myLabel=Label(root,text="Local")
                   # myLabel.pack()

                #output.after(10000,perform)


                root.mainloop()
        time.sleep(10)
        frontend()
backend()


