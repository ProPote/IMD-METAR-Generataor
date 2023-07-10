from tkinter import *
import time
from inputimeout import inputimeout
from playsound import playsound
import multiprocessing

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
                data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
                if data.decode('utf-8')[0]=="-": #to take the right string
                    break
                FINAL_METAR=""
                root=Tk()
                #function to proceed after enterinf the timestamp
                cloudcover=""

                frame=LabelFrame(root,bg="#9ad7fc")
                frame.pack()

                output=Label(frame,text="Enter the four cloud terms",font="Verdana 15 ",bg="#9ad7fc")
                output.pack()

                output=Label(frame,text="")
                output.pack()

                e2=Entry(frame,width=40,font=('Georgia 30'))
                e2.pack()

                output=Label(frame,text="")
                output.pack()

                e3=Entry(frame,width=40,font=('Georgia 30'))
                e3.pack()

                output=Label(frame,text="")
                output.pack()

                e4=Entry(frame,width=40,font=('Georgia 30'))
                e4.pack()

                output=Label(frame,text="")
                output.pack()

                e5=Entry(frame,width=40,font=('Georgia 30'))
                e5.pack()

                output=Label(frame,text="")
                output.pack()

                frame2=LabelFrame(root,bg="#9ad7fc")
                frame2.pack()

                output=Label(frame2,text=e2.get())
                output.pack()
                output=Label(frame2,text="")
                output.pack()

                output=Label(frame2,text=e3.get())
                output.pack()

                output=Label(frame2,text="")
                output.pack()

                output=Label(frame2,text=e4.get())
                output.pack()

                output=Label(frame2,text="")
                output.pack()

                output=Label(frame2,text=e5.get())
                output.pack()



                def cloud_cover():
                    cloudcover=e2.get()+" "+e3.get()+" "+e4.get()+" "+e5.get()
                    print(cloudcover)
                    return cloudcover
                def onclic():
                    time.sleep(0)
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
                    myLabel=Label(root,text=FINAL_METAR,font="Times 20 bold")
                    myLabel.pack()
            #root=Tk()
            #myLabel=Label(root,text=FINAL_METAR)
            #myLabel.pack()
                new_button=Button(root,text="Generate Metar",command=onclic,font=('Georgia 20'),bg="orange",fg="blue")
                new_button.pack()

                #code to exit the screen
                '''new_button2=Button(root,text="Next",command=root.destroy())
                new_button2.pack()'''

                #def perform():
                   # myLabel=Label(root,text="Local")
                   # myLabel.pack()

                #output.after(10000,perform)


                root.mainloop()

        time.sleep(10) ##This timer can control the time after which the window will pop again
        frontend()
backend()
