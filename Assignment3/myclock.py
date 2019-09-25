#all of the work herein is solely mine
import tkinter as tk
import time

#time1="" means it defaults to "" initially
def tick(time1=""):
    time2 = time.strftime("%H:%M:%S")
    if time2 != time1:
        time1 = time2
        clock.config(text = time2)
    clock.after(200,tick)

mywindow = tk.Tk()
mywindow.title("Zachary Graber")
mywindow.geometry("300x100")
clock = tk.Label(mywindow, font = ("gothic", 20, "bold"), bg = "green")
clock.pack(fill = "both", expand = 1)
tick()
mywindow.mainloop()