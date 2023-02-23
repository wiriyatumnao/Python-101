# Author: Wiriya Tumnao
# e-Mail: wiriya_tumnao@yahoo.com
#----------------------------------------------------
# homework-ep4 (write/read data to/from csv file)

import csv
import tkinter as tk
from tkinter import ttk             

# create window
GUI = tk.Tk()                                    #หน้าจอหลักของโปรแกรม
GUI.title('Homework EP#4 โดย...วิริยะ ทำเนาว์')      #ชื่อโปรแกรม
GUI.geometry('700x700')                          #ขนาดหน้าจอแสดง

# create Label
label = tk.Label(GUI, text=' ใส่รายการซื้อของใช้ในบ้าน/อาหาร :  ' ,font=("Angsana", 30),fg='blue')
input_box = tk.Entry(GUI)


#-------------write data to csv file ----------------------
def wdata():
    with open("data.csv", "a", newline="") as f:

    # Create a csv.writer object
        data = input_box.get()
        f.write(data)
        f.write("\n")
             
# create button to submit data for save to file
button = tk.Button(GUI, text=' บันทึกข้อมูล (save to file)',font=("Angsana", 20) ,command=wdata)
                          
# grid geometry
label.grid(row=10, column=100)
input_box.grid(row=10, column=151)
button.grid(row=50, column=50, columnspan=100)



#-------------Read data ----------------------
def rdata():
    with open("data.csv") as fd:
        lines = fd.readlines()
        for line in lines:
            print(line.rstrip())
    
             
# create button to read data from csv file
button2 = tk.Button(GUI, text=' อ่านข้อมูลจากไฟล์ CSV ',font=("Angsana", 20) ,command=rdata)
                          
# grid geometry
#label.grid(row=200, column=100)
button2.grid(row=250, column=50, columnspan=100)



# Start the GUI event loop
GUI.mainloop()




