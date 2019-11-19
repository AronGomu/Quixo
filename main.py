
from Tkinter import *

def getGridInfo(i,j):
	print("Position de la case :")
	print("i : ", i)
	print("j : ", j)

def createCase(i, j):

	pixel = PhotoImage(width=1, height=1)

	case = Button()
	case["text"] = "X"
	case["image"] = pixel
	case["command"] = lambda: getGridInfo(i,j)
	case["bg"]= "blue"
	case["height"] = 200
	case["width"] = 200
	if (i != 0 and i != 4 and j != 0 and j != 4):
		case["state"] = DISABLED
	case.grid(row=i,column=j, sticky="wens")



root = Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_width,screen_height)

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