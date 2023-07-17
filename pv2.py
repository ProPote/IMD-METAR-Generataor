import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
from inputimeout import inputimeout
from playsound import playsound
import multiprocessing
import xlsxwriter
from openpyxl import *
from openpyxl import Workbook,load_workbook
from datetime import datetime
import pytz

def backend():
    import socket
    UDP_IP = "192.168.103.93"
    UDP_PORT = 5000
    sock = socket.socket(socket.AF_INET, # Internet
    socket.SOCK_DGRAM) 
    sock.bind((UDP_IP, UDP_PORT))

    wb = Workbook()
    ws = wb.active

    while True:

        def frontend():
            while True:
                data, addr = sock.recvfrom(1024)
                if data.decode('utf-8')[0]=="-":
                    break

                FINAL_METAR=""

                root = tk.Tk()
                cloudcover=""
                def end_window():
                    time.sleep(0)
                    data2=data.decode('utf-8')
                    print(data2)
                    runway_number=data2[8:10]
                    GST_Time=data2[20:28]
                    Date=data2[29:31]
                    WS_10_min=data2[61:64]
                    WD_10_min=data2[83:86]
                    Hum_10_min=data2[107:109]
                    Temp_10_min=data2[130:132]
                    DP_10_min=data2[154:156]
                    Pres_10_min=data2[185:190]
                    QNH_10_min=data2[215:219]
                    QFE_10_min=data2[237:240]
                    temp =Temp_10_min
                    dew_pt = DP_10_min
                    finaltempdew = str(temp) + '/' + str(dew_pt)

                    METAR=""
                    report=" "
                    typ = "METAR"
                    time1=""
                    date=""

                    def status():
                        time_used=GST_Time
                        time1=time_used[0]+time_used[1]+time_used[3]+time_used[4]
                        check=Date
                        return Date+time1
                    def wind():
                        finalspeed = round(float(WS_10_min))
                        finalwind = str(finalspeed)+str(WD_10_min)+'KT'
                        if finalspeed < 10:
                            finalwind = '0' + str(finalspeed)+str(WD_10_min)+'KT'
                        return finalwind

                    FINAL_METAR=str(typ)+" "+"VAPO "+str(report)+str(wind())+" "+str(finaltempdew)+" "+"Q"+str(QNH_10_min)+" "+"NOSIG="

                    gmt = pytz.timezone('GMT')
                    now = datetime.now(gmt)

                    current_time = now.strftime("%H:%M:%S")

                    ws.append([current_time,FINAL_METAR])
                    wb.save("demo.xlsx")

                    myLabel=Label(root,text=FINAL_METAR,font="Tektur 25")
                    myLabel.pack()

                    def execute():
                        root.destroy()
                        time.sleep(0)

                    root.after(4000,execute)
                    root.mainloop()


                root.title("METAR Generator")
                # Simply set the theme
                root.tk.call("source", "C:\\Users\\hp\\Azure\\azure.tcl")
                root.tk.call("set_theme", "dark")

                output=Label(root,text="Enter the four cloud terms",font="Tektur 20")
                output.pack(pady = 20)

                e2=Entry(root, width = 40,borderwidth = 8,font=('Tektur 25'))
                e2.pack(padx = 20, pady = 10)

                       

                e3=Entry(root,width=40,borderwidth = 8,font=('Tektur 25'))
                e3.pack(padx = 20, pady = 10)

                        

                e4=Entry(root,width=40,borderwidth = 8,font=('Tektur 25'))
                e4.pack(padx = 20, pady = 10)

                        

                e5=Entry(root,width=40,borderwidth = 8,font=('Tektur 25'))
                e5.pack(padx = 20, pady = 10)


                # Set a minsize for the window, and place it in the middle
                root.update()
                root.minsize(root.winfo_width(), root.winfo_height())
                x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
                y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
                root.geometry("+{}+{}".format(x_cordinate, y_cordinate-20))

                def cloud_cover():
                    cloudcover=e2.get()+" "+e3.get()+" "+e4.get()+" "+e5.get()
                    return cloudcover

                def onclic():
                    time.sleep(0)
                    data2=data.decode('utf-8')
                    runway_number=data2[8:10]
                    GST_Time=data2[20:28]
                    Date=data2[29:31]
                    WS_10_min=data2[61:64]
                    WD_10_min=data2[83:86]
                    Hum_10_min=data2[107:109]
                    Temp_10_min=data2[130:132]
                    DP_10_min=data2[154:156]
                    Pres_10_min=data2[185:190]
                    QNH_10_min=data2[215:219]
                    QFE_10_min=data2[237:240]
                    METAR=""
                    report=" "
                    typ = "METAR"

                    time1=""
                    date=""
                    def status():
                        time_used=GST_Time
                        time1=time_used[0]+time_used[1]+time_used[3]+time_used[4]
                        check=Date
                        return Date+time1
                        #-------------------------------------------------------
                    #temp and dew point temp component
                    temp =Temp_10_min
                    dew_pt = DP_10_min
                    finaltempdew = str(temp) + '/' + str(dew_pt)
                    def wind():
                        finalspeed = round(float(WS_10_min))
                        finalwind = str(finalspeed)+str(WD_10_min)+'KT'
                        if finalspeed < 10:
                            finalwind = '0' + str(finalspeed)+str(WD_10_min)+'KT'
                        return finalwind

                    report=str(status())+'Z'
                    FINAL_METAR=str(typ)+" "+ "VAPO "+str(report)+" " +str(wind())+str(cloud_cover())+" "+str(finaltempdew)+" "+"Q"+str(QNH_10_min)+" "+"NOSIG="

                    gmt = pytz.timezone('GMT')
                    now = datetime.now(gmt)

                    current_time = now.strftime("%H:%M:%S")

                    ws.append([current_time,FINAL_METAR])
                    wb.save("demo.xlsx")

                    myLabel2=Label(root,text=FINAL_METAR,font="Tektur 25")
                    myLabel2.pack()

                    def execute():
                        root.destroy()
                        time.sleep(0)
                    root.after(4000,execute)

                new_button=Button(root,text="Generate METAR",command=onclic,font=('Tektur 15'))
                new_button.pack()

                root.after(10000, end_window)

                root.mainloop()

        time.sleep(0)

        frontend()

backend()
#trend, excel issue
