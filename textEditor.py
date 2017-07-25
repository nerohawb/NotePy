import os
from tkinter import *
from tkinter import filedialog as fd

#Inits
filename = None

#Functions for Menu Bar
def newFile():
	global filename
	filename = "Untitled"
	text.delete(0.0, END)
	
def saveFile(event):
	global filename
	if filename == None or filename == "Untitled":
		saveAs()
	else:
		textFile = text.get(0.0, END)
		aFile = open(filename, "w")
		aFile.write(textFile)
		aFile.close()
		print('Saved')
	return 'break'

	
def saveAs():
	global filename
	aFile = fd.asksaveasfile(mode="w", defaultextension='.txt')
	textFile = text.get(0.0, END)
	try:
		filename = os.path.basename(aFile.name)
		aFile.write(textFile.rstrip())
	except:
		pass
		
root = Tk()	
		
def openFile():
	global filename
	aFile = fd.askopenfile(parent=root, title="Select a Text File")
	try:
		filename = os.path.basename(aFile.name)
		print(filename)
		textFile = aFile.read()
		text.delete(0.0, END)
		text.insert(0.0, textFile)
		aFile.close()
	except:
		pass
	

#Function for actionFind
#def find():
	#text.tag_remove('found', '1.0', END)
	#s = edit.get()
	#index = text.search(s, "1.0", END, count=StringVar(), regexp=True)
	#end = str(float(index) + float("0.{}".format(len(s))))
	#text.tag_add("search", index, end)
	#text.tag_config("search", background="yellow", foreground="black")


#Functions for Action Bar
def actionFind():
	#Search Window for Find
	global edit
	global status
	global finderWindow
	
	status = None
	
	finderWindow = Toplevel()
	finderWindow.minsize(width=0, height=20)
	finderWindow.maxsize(width=0, height=20)
	Label(finderWindow, text="Find: ", height=0, width=10).pack(side=LEFT)
	edit = Entry(finderWindow)
	edit.pack(side=LEFT, fill=BOTH, expand=1)
	edit.focus_set()
	Button(finderWindow, text='Find', command=find).pack(side=RIGHT)
	Label(finderWindow, text="Status: {}".format(status), height=0, width=15).pack(side=BOTTOM)

def actionCopy():
	try:
		root.clipboard_clear()
		root.clipboard_append(text.get("sel.first", "sel.last"))
	except:
		pass
def actionCut():
	try:
		actionCopy()
		text.delete("sel.first", "sel.last")
	except:
		pass
def actionPaste():
	try:
		text.insert('insert', root.selection_get(selection="CLIPBOARD"))
	except:
		pass

def actionRedo():
	try:
		text.edit_redo()
	except:
		pass
		
def actionUndo():
	try:
		text.edit_undo()
	except:
		pass
	
def actionSelect(event):
	text.tag_add(SEL, "1.0", END)
	text.mark_set(INSERT, "1.0")
	text.see(INSERT)
	return 'break'

#Function for Other Bar
def otherAbout():

	aboutWindow = Toplevel()
	aboutWindow.minsize(width=250, height=100)
	aboutWindow.maxsize(width=250, height=100)
	Label(aboutWindow, text="Developers:", height=1,width=50).pack()
	Label(aboutWindow, text="Nieric 'HelloWorld' Javinal", height=1, width=50).pack()
	Label(aboutWindow, text="Justine Lyle 'Bieber' Ybanes", height=1, width=50).pack()
	Label(aboutWindow, text="Johnbert Soria", height=1, width=50).pack()
	Button(aboutWindow, text='Okie', command=aboutWindow.destroy).pack()
	

#Tkinter
root.title("SkyNet Text Editor")
root.minsize(width=600, height=600)
root.maxsize(width=600, height=600)

text = Text(root, width=600, height=600)
text.pack()

menubar = Menu(root)
aMenu = Menu(menubar)
aMenu.add_command(label="New", command=newFile)
aMenu.add_command(label="Open", command=openFile)
aMenu.add_command(label="Save", command=saveFile)
aMenu.add_command(label="Save As..", command=saveAs)
aMenu.add_separator()
aMenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=aMenu)


actionMenu = Menu(menubar)
#actionMenu.add_command(label="Find", command=actionFind)
#actionMenu.add_separator()
actionMenu.add_command(label="Undo", command=actionUndo)
actionMenu.add_command(label="Redo", command=actionRedo)
actionMenu.add_separator()
actionMenu.add_command(label="Select All", command=actionSelect)
actionMenu.add_command(label="Copy", command=actionCopy)
actionMenu.add_command(label="Cut", command=actionCut)
actionMenu.add_command(label="Paste", command=actionPaste)
menubar.add_cascade(label="Action", menu=actionMenu)

otherMenu = Menu(menubar)
otherMenu.add_command(label="About", command=otherAbout)
menubar.add_cascade(label="Other", menu=otherMenu)

#Key Binds
text.bind("<Control-Key-a>", actionSelect)
text.bind("<Control-Key-A>", actionSelect)
text.bind("<Control-Key-S>", saveFile)
text.bind("<Control-Key-s>", saveFile)

root.config(menu=menubar)
root.mainloop()
	
