from Tkinter import *
import youtube1
import ttk
root = Tk()
from threading import Thread
import Queue
import time 
#root.tilte('download')
root.geometry('640x250+700+300')
root.resizable(0,0)
url_frame = Frame(root , width = 630 , height = 50,padx=3 , pady = 3)
check_frame = Frame (root , width = 630 , height = 50 , padx =3)
selection_frame = Frame(root , width = 630 , height = 100 , padx =3)
download_frame = Frame(root , width = 630  , padx = 3 ,pady = 3)
root.grid_rowconfigure(1, weight=0)
root.grid_columnconfigure(0, weight=1)
url_frame.grid(row = 0 , sticky = 'w')
check_frame.grid(row = 1 )
selection_frame.grid(row = 2 , sticky ='w')
download_frame.grid(row = 3)
var= IntVar()
ls = []
select_code = []
extension = []
type = []
q = Queue.Queue()
global progress_var
progress_var = DoubleVar()
def Thread1():
	empty_label2 = Label(selection_frame , text='\t\tThe available formats are ')
	empty_label3 = Label(selection_frame , text='\t\t')
	ls , s , ext= youtube1.check(str(e_url.get()))
	empty_label2.grid(row=0, column =0)
	for x in range(0, len(ls)):
		choice = Radiobutton(selection_frame , text = ls[x], variable = var , value = x)
		type.append(ls[x])
		select_code.append(s[x])
		extension.append(ext[x])
		empty_label3.grid(row= (x+1) , column =0 )
		choice.grid(row = (x+1) , column =0)
	global b2 
	b2= Button(download_frame , text = 'Download' , width = 10 , command = download)
	b2.grid(row=0,column =0)
def Thread2():
	youtube1.dwd(select_code[var.get()], type[var.get()],extension[var.get()] , q)
	
def Thread3():
	def loop_function():
		if not q.empty():
			progress_var.set(q.get())
			time.sleep(0.02)
			root.update_idletasks()
		root.after(100, loop_function)
	#Label(download_frame , value = q.get()).grid(row =1,column =0 )
	loop_function()
		
def check():
	if e_url.get()!='':
		Thread(target = Thread1).start()		
	else :
		print "input please"
def download():
	b2.destroy()
	ttk.Progressbar(download_frame , length = 200 ,variable = progress_var).grid(row = 0 , column =0)
	Thread(target = Thread2).start()
	Thread(target = Thread3).start()


empty_label1 = Label(url_frame , text = '\t\t')
url_label = Label(url_frame , text = 'Enter URL')
empty_label = Label(url_frame , text = '\t\t\t')
e_url = Entry(url_frame , width = 60)

empty_label1.grid(row = 0 , column =0 )
url_label.grid(row = 0 , column  =1 )
empty_label.grid(row = 0 ,column = 2)
e_url.grid(row = 0 , column =3 )

b1 = Button(check_frame , text = "Check" , width = 10 , command =check)
b1.grid(row =0 , column =0 )
root.mainloop()