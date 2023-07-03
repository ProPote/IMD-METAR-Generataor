from tkinter import *
import time
from inputimeout import inputimeout

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
                #C1=e2.get()
                #C2=e3.get()
                #C3=e4.get()
                #C4=e5.get()
                def cloud_cover():
                    cloudcover=e2.get()+" "+e3.get()+" "+e4.get()+" "+e5.get()
                    print(cloudcover)
                    return cloudcover
                def onclic():
                    time.sleep(0)
                    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
                    data2=data.decode('utf-8')
                    print(data2)
                    runway_number=data2[8:10]
                    GST_Time=data2[20:28]
                    Date=data2[29:31]
                    WS_10_min=data2[61:64]
                    WD_10_min=data2[86:88]
                    Hum_10_min=data2[107:109]
                    Temp_10_min=data2[130:132]
                    DP_10_min=data2[154:156]
                    Pres_10_min=data2[185:190]
                    QNH_10_min=data2[215:219]
                    QFE_10_min=data2[237:240]

                    print(GST_Time)
                    print(Date)
                    #declaring all the components of the final METAR Report
                    METAR=""
                    report=" "
                    typ = "METAR"
                    #-----------------------------------------------------------
                    #Taking the timestamp for which the user wants the METAR
                    #Finding the row in the given data which has to be accessed
                    #row=0
                    #for i in range(25):
                    #    if time==df.iloc[i,3]:
                    #        row=i
                    #-----------------------------------------------------------

                    #Taking the four terms of cloud cover
                    #cell_value = df.iloc[row, 28] # cell_value = df.iloc[row_index, column_index]
                    #pressure=('Q -',cell_value)
                    #-----------------------------------------------------------

                    #status term which comprises of date,and time in zulu
                    time1=""
                    date=""
                    def status():
                        #runway=(df.iloc[row,2])
                        time_used=GST_Time
                        time1=time_used[0]+time_used[1]+time_used[3]+time_used[4]
                        check=Date

                        #print(date)
                        print(Date+time1+"DDDD")
                        return Date+time1
                        #-------------------------------------------------------
                    #temp and dew point temp component
                    temp =Temp_10_min
                    dew_pt = DP_10_min
                    print(Temp_10_min)
                    print(DP_10_min)
                    finaltempdew = str(temp) + '/' + str(dew_pt)
                    print(finaltempdew)
                    report=str(status())+'Z'
                    FINAL_METAR=str(typ)+" "+str(report)+" "+str(cloud_cover())+" "+str(finaltempdew)+" "+"Q"+str(QNH_10_min)+" "+"NOSIG="
                    print(FINAL_METAR)
                    myLabel=Label(root,text=FINAL_METAR)
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
        time.sleep(0)
        frontend()
backend()


