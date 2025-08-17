
from tkinter import *



class SaisieEcrireFichier:
	
	def __init__(self, fenetre, fonction_retour ):
		self.fenetre = fenetre
		 
		self.fonction_retour = fonction_retour
		 
		
		self.frame = Frame(self.fenetre, width = 700, height = 900, bg='#25ecde')
		self.frame.place(x= 0, y = 0)
		
		self.construction()
	
	 
	# ******************************************************************
	def construction(self):
		
		self.openFileButton = Label(self.frame, text = 'Enregistrer : écrire le nom du fichier', font = ("times", 15)   )
		self.openFileButton.place(x= 30, y = 100)
		
		self.fileNameSave = StringVar()
		self.fileNameSave.set('')
		self.labelFileNameOpen = Entry(self.frame, textvariable = self.fileNameSave, font = ("times", 15), width = 50  )
		self.labelFileNameOpen.place(x= 30, y = 200)
		 
		
		# valider
		self.validationButton = Button(self.frame, text = 'validation Enregistrer dans fichier', font = ("times", 15), command = self.validationWriteFile )
		self.validationButton.place(x=30, y = 800)
		
		
		# annuler
		self.annulationButton = Button(self.frame, text = 'annulation  ', font = ("times", 15), command = self.annulation   )
		self.annulationButton.place(x=430, y = 800) 
		
	
	# ******************************************************************
	def validationWriteFile(self):
		self.fileName = self.fileNameSave.get()
		# fin
		self.fonction_retour()


	
	# ******************************************************************
	def annulation(self):
		self.fileName = ''
		# fin
		self.fonction_retour()
 
	
	 
 

