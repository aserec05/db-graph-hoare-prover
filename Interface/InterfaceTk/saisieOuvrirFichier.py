
from tkinter import *


from os import listdir
from os.path import isfile, join

class SaisieOuvrirFichier:
	
	def __init__(self, fenetre, repertoire, fonction_retour ):
		self.fenetre = fenetre
		 
		self.fonction_retour = fonction_retour
		 
		self.repertoire = repertoire
		self.frame = Frame(self.fenetre, width = 700, height = 900, bg='#25ecde')
		self.frame.place(x= 0, y = 0)
		
		self.construction()
	
	
	# ******************************************************************
	def construction(self):
		
		self.lesFichiers = [f for f in listdir(self.repertoire) if isfile(join(self.repertoire, f))]
		nbFichiers = len(self.lesFichiers)
		
		self.fileNameTitre = StringVar()
		self.fileNameTitre.set('Nombre de fichiers : {}'.format(nbFichiers))
		
		self.openFileButton = Label(self.frame, textvariable = self.fileNameTitre, font = ("times", 15)   )
		self.openFileButton.place(x= 30, y = 100)
		 
		
		self.laliste = Listbox(self.frame,   height = min(nbFichiers,8),  font = ("times", 15)   )
		for i,f in enumerate(self.lesFichiers):
			self.laliste.insert(i, f)
	 
		self.laliste.place(x= 30, y = 180)
		
		 
		btn = Button(self.frame, text = "Ouvrir le fichier selectionné", font = ("times", 15), command = self.suite)  
		btn.place(x= 30, y = 700)
		
		
		# annuler
		self.annulationButton = Button(self.frame, text = 'annulation  ', font = ("times", 15), command = self.annulation   )
		self.annulationButton.place(x=430, y = 700) 
		
		
	
		'''
		self.openFileButton = Label(self.frame, text = 'écrire le nom du fichier', font = ("times", 15)   )
		self.openFileButton.place(x= 30, y = 100)
		
		self.fileNameOpen = StringVar()
		self.fileNameOpen.set('')
		self.labelFileNameOpen = Entry(self.frame, textvariable = self.fileNameOpen, font = ("times", 15), width = 50  )
		self.labelFileNameOpen.place(x= 30, y = 200)
		 
		
		# valider
		self.validationButton = Button(self.frame, text = 'validation Ouverture fichier', font = ("times", 15), command = self.validationOpenFile )
		self.validationButton.place(x=30, y = 800)
		'''
		
	
	
	
	def suite(self):
		letuple = self.laliste.curselection() 
		if letuple :
			indice = letuple[0]
			#~ print(self.lesFichiers[indice])
			self.fileName = self.lesFichiers[indice]
			self.fonction_retour()
		else :
			print("aucune sélection")
		
	# ******************************************************************
	def validationOpenFile(self):
		self.fileName = self.fileNameOpen.get()
		# fin
		self.fonction_retour()


	
	# ******************************************************************
	def annulation(self):
		self.fileName = ''
		# fin
		self.fonction_retour()
 
	
	 
 

