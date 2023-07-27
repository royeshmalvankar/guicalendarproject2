#import library 
from tkinter import *
from tkcalendar import *

#create object
cal=Tk()

#Give Title
cal.title("MyCalendar")

#set window size
cal.geometry("300x400")

#set tkinter background
cal.config(bg="orange")

#add calender
calendar1=Calendar(cal,selectmode="day",year=2023,month=7,showweeknumbers=False,showothermonthdays=False,background="lightgreen",
                    foreground="blue",selectbackground="red",normalforeground="green",weekendbackground="lightblue",weekendforeground="red"
                  )
calendar1.pack(pady=50)

# maintain modularity
def sel_date():
    lab.config(text="Date selected is:"+calendar1.get_date())

#add button and call function
Button(cal,text="Get Date",command=sel_date,relief="raised",borderwidth=5,font=("Arial,10"),fg="red").pack(pady=5)

#add label with click of button
lab=Label(cal,text="Select Date",font=("Arial,10"),bg="orange")
lab.pack(pady=5)

#execute code
cal.mainloop()