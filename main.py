import subprocess
from tkinter import *
import tkinter as tk


#_______________________________LOGIC________________________________________________________
a = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

profiles = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
#print(profiles)

j = 0
#________________________________GUI_________________________________________________________
root = tk.Tk()

root.title('The-WiPass-Dumper v1.0.0')
root.config(bg='#000000')
root.geometry('550x550')
root.iconphoto(
	False,
	tk.PhotoImage(file="./wifi_icon.png")
)

for i in profiles:
	try:
		results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear',]).decode('utf-8').split('\n')
		results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
	except:
		pass


	try:
		l = Label(
			root,
			text="{:<30}	{:<}".format(i,results[0]),
			font=("arial",12,"bold"),
			bg="gray",
			justify=CENTER
		).place(x=10,y=10+(30*j))
		j+=1
		pass
	except IndexError:
		l = Label(
			root,
			text="{:<30}	{:<}".format(i,"Bad SSID Format"),
			font=("arial",12,"bold"),
			bg="gray",
			justify=CENTER
		).place(x=10,y=10+(30*j))
		j+=1
		pass


root.mainloop()