
from Tkinter import *

def getGridInfo(i,j):
	print("Position de la case :")
	print("i : ", i)
	print("j : ", j)

def createCase(i, j):
	case = Button()
	case["command"] = lambda: getGridInfo(i,j)
	case["bg"]= "blue"
	if (i != 0 and i != 4 and j != 0 and j != 4):
		case["state"] = DISABLED
	case.grid(row=i,column=j)


root = Tk()
for i in range(0,5):
	for j in range(0,5):
		createCase(i,j)
root.mainloop()
root.destroy()


"""
import Tkinter
root = Tkinter.Tk(  )
for r in range(3):
   for c in range(4):
      Tkinter.Label(root, text='R%s/C%s'%(r,c),
         borderwidth=1 ).grid(row=r,column=c)
root.mainloop(  )
"""