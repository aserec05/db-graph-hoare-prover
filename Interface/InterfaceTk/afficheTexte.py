
from tkinter import *
 



class AfficheTexte:
	
	def __init__(self, parent , chaine):
		self.frameParent = parent 
		self.leTexte = chaine
		
		self.frameLocal = Frame(self.frameParent, width = 700, height = 900, bg='#25ecde')
		self.frameLocal.place(x= 0, y = 0)
		
		self.constructionFrame()
	
	 
	
	# ******************************************************************
	# ******************************************************************
	def constructionFrame(self):
		
		self.message = Text(self.frameLocal, height = 26, width = 50, font = ('Helvetica',  15) )
            
		self.message.place (x= 50, y = 60)
		
		self.message.insert('insert',  self.leTexte  )
	
	
	def efface(self):
		self.message.place_forget()
		self.message.destroy()
		self.frameLocal.place_forget()
		self.frameLocal.destroy()
		# à reprendre ---------------------------
		self.frameLocal = Frame(self.frameParent, width = 700, height = 900, bg='#95ecde')
		self.frameLocal.place(x= 0, y = 0)
		 
 
