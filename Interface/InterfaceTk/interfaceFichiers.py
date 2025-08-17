
from tkinter import *
import pickle
 

from saisieOuvrirFichier import *
from saisieEcrireFichier import *
from afficheTexte import *

from datasNoyau import *

from lectureFichierAscii import *
from ecritureFichierAscii import *

from leNoyau import *




class InterfaceFichiers:
	
	def __init__(self, interfaceParent , fenetre):
		self.parent = interfaceParent
		self.fenetre = fenetre
		
		
		self.frameMenu = Frame(self.fenetre, width = 700, height = 300, bg='#25ecde')
		self.frameMenu.place(x= 0, y = 0)
		self.constructionFrameMenu()
		
	
	 
	# ******************************************************************
	def constructionFrameMenu(self):
		xMarge = 30
		
		# --------------------  fichier binaire ------------------------
		yFile = 40

		# ouvrir fichier
		self.openFileButton = Button(self.frameMenu, text = 'ouvrir fichier binaire', font = ("times", 15), command = self.ouvrirFichier  )
		self.openFileButton.place(x= xMarge, y = yFile)
		
		# enregistrer fichier
		self.saveFileButton = Button(self.frameMenu, text = 'enregistrer dans fichier binaire', font = ("times", 15), command = self.enregistrerFichier  )
		self.saveFileButton.place(x= xMarge + 300, y = yFile)
		
		
		# ----------------  fichier ascii ------------------------------
		yFileTexte = 100
		
		self.openFileAsciiButton = Button(self.frameMenu, text = 'ouvrir fichier ascii', font = ("times", 15), command = self.ouvrirFichierAscii)
		self.openFileAsciiButton.place(x= xMarge   , y = yFileTexte)
		
		self.saveFileAsciiButton = Button(self.frameMenu, text = 'enregistre fichier ascii', font = ("times", 15), command = self.enregistrerFichierAscii)
		self.saveFileAsciiButton.place(x= xMarge + 300 , y = yFileTexte)
		
		
		# ----------------  fichier texte ------------------------------
		yFileTexte = 160
		
		self.enregistreDatasFichierTexteButton = Button(self.frameMenu, text = 'enregistre datas fichier texte', font = ("times", 15), command = self.imprimeDatasFichierTexte)
		self.enregistreDatasFichierTexteButton.place(x= xMarge   , y = yFileTexte)
		
		self.enregistrePreuveFichierTexteButton = Button(self.frameMenu, text = 'enregistre preuve fichier texte', font = ("times", 15), command = self.imprimePreuveFichierTexte)
		self.enregistrePreuveFichierTexteButton.place(x= xMarge + 300 , y = yFileTexte)
		
		
		# ---------  affichages console --------------------------------
		yConsole = 220
		
		# imprime  la correction
		self.buttonAction = Button(self.frameMenu, text = 'Console : imprime la preuve', font = ("times", 15), command = self.parent.imprimePreuveConsole )
		self.buttonAction.place(x= xMarge, y = yConsole)
		
		# imprime les datas
		self.imprimeDatasConsoleButton = Button(self.frameMenu, text = 'Console : imprime datas', font = ("times", 15), command = self.parent.imprimeDatasConsole)
		self.imprimeDatasConsoleButton.place(x= xMarge + 300 , y = yConsole)
	
	
	
	
	
	# ******************************************************************
	# ******************************************************************
	
	
	# **********************************************************************
	#         lecture  dans un fichier binaire
	# **********************************************************************
	def ouvrirFichier(self):
		self.parent.enleveAfficheTexte()
		self.parent.frameCache.place(x= 0, y = 0)
		self.saisieOuvrirFichier = SaisieOuvrirFichier(self.parent.frameBis,  '[Exemples]/[binaires]/',  self.fonctionRetourOuvrirFichierBinaire )
	
	
	def fonctionRetourOuvrirFichierBinaire(self):
		
		leFileNameOpen = self.saisieOuvrirFichier.fileName
		
		if leFileNameOpen:
			print("Lecture du fichier binaire : {}  ".format(leFileNameOpen) )
			leFileNameComplet = '[Exemples]/[binaires]/'+leFileNameOpen
			
			# *********************************************************************  if  nom de fichier valide ....
			datasNoyau = pickle.load(open(leFileNameComplet, 'rb'))
			assert(isinstance(datasNoyau, DatasNoyau))
			
			self.parent.updateAffichageDataNoyau(datasNoyau)
		
		# nettoyer
		self.parent.frameCache.place_forget()
		self.saisieOuvrirFichier.frame.place_forget()
		del self.saisieOuvrirFichier
	
	
	# **********************************************************************
	#         ecriture  dans un fichier binaire
	# **********************************************************************
	def enregistrerFichier(self):
		self.parent.enleveAfficheTexte()
		self.parent.frameCache.place(x= 0, y = 0)
		self.saisieEcrireFichier = SaisieEcrireFichier(self.parent.frameBis, self.fonctionRetourEcrireFichier )
	
	
	
	def fonctionRetourEcrireFichier(self):
		leFileNameSave = self.saisieEcrireFichier.fileName
		
		if leFileNameSave:
			datasNoyau = self.parent.datasNoyau
			
			assert(isinstance(datasNoyau, DatasNoyau))
			assert(isinstance(datasNoyau.getFormulePre(), FormuleLogique))
			assert(isinstance(datasNoyau.getStrategie(), Strategie))
		
			leFileNameComplet = '[Exemples]/[binaires]/'+leFileNameSave
			pickle.dump(datasNoyau, open(leFileNameComplet, 'wb'))
		
		# nettoyer
		self.parent.frameCache.place_forget()
		self.saisieEcrireFichier.frame.place_forget()
		del self.saisieEcrireFichier 
	
	
	
	# **********************************************************************
	#         lecture   dans un fichier ASCII
	# **********************************************************************
	def ouvrirFichierAscii(self):
		self.parent.enleveAfficheTexte()
		self.parent.frameCache.place(x= 0, y = 0)
		self.saisieOuvrirFichier = SaisieOuvrirFichier(self.parent.frameBis,  '[Exemples]/[ascii]/',  self.fonctionRetourOuvrirFichierAscii )
	
	
	def fonctionRetourOuvrirFichierAscii(self): 
		leFileNameOpen = self.saisieOuvrirFichier.fileName
		
		if leFileNameOpen:
			print("Lecture du fichier ascii : {}  ".format(leFileNameOpen) )
			leFileNameComplet = '[Exemples]/[ascii]/'+leFileNameOpen
			
			# *********************************************************************  if  nom de fichier valide ....
			l = LectureFichierAscii(leFileNameComplet )
			
			datasNoyau = l.getDatasForNoyau()
			assert(isinstance(datasNoyau, DatasNoyau))
			
			self.parent.updateAffichageDataNoyau(datasNoyau)
		
		
		# nettoyer
		self.parent.frameCache.place_forget()
		self.saisieOuvrirFichier.frame.place_forget()
		del self.saisieOuvrirFichier 
	
	
	
	# **********************************************************************
	#         ecriture   dans un fichier ASCII
	# **********************************************************************
	def enregistrerFichierAscii(self):
		self.parent.enleveAfficheTexte()
		self.parent.frameCache.place(x= 0, y = 0)
		self.saisieEcrireFichier = SaisieEcrireFichier(self.parent.frameBis, self.fonctionRetourEcrireFichierAscii )
	
	
	
	def fonctionRetourEcrireFichierAscii(self):
		leFileNameSave = self.saisieEcrireFichier.fileName
		if leFileNameSave:
			print("ecriture du fichier ascii : {}  ".format(leFileNameSave) )
			leFileNameComplet = '[Exemples]/[ascii]/'+leFileNameSave
			
			datasNoyau = self.parent.datasNoyau

			l = EcritureFichierAscii(leFileNameComplet, datasNoyau)
		 
		
		# nettoyer
		self.parent.frameCache.place_forget()
		self.saisieEcrireFichier.frame.place_forget()
		del self.saisieEcrireFichier 
	
	 
	
	# **********************************************************************
	#        imprime Preuve Fichier Texte
	# **********************************************************************
	def imprimePreuveFichierTexte(self):
		self.parent.enleveAfficheTexte()
		self.parent.frameCache.place(x= 0, y = 0)
		self.saisieEcrireFichierTexte = SaisieEcrireFichier(self.parent.frameBis, self.fonctionRetourEcrirePreuveFichierTexte )
	
	
	def fonctionRetourEcrirePreuveFichierTexte(self):
		leFileNameSave = self.saisieEcrireFichierTexte.fileName
		 
		if leFileNameSave:
			datasNoyau = self.parent.datasNoyau
			assert(isinstance(datasNoyau, DatasNoyau))
			
			
			self.parent.calculCorrection()
			
			leFileNameComplet = '[Exemples]/[texte]/'+leFileNameSave
			f = open(leFileNameComplet, 'w')
			f.write(datasNoyau.imprimeFichierTexte())
			f.write('\n\nPreuve-----------------------------\n\n')
			f.write(self.parent.reponse)
			f.close()
			
			print("\nEnregistrement de la preuve dans fichier")
		
		# nettoyer
		self.parent.frameCache.place_forget()
		self.saisieEcrireFichierTexte.frame.place_forget()
		del self.saisieEcrireFichierTexte 
	
	
	
	# **********************************************************************
	#        imprime Datas Fichier Texte
	# **********************************************************************
	def imprimeDatasFichierTexte(self):
		self.parent.enleveAfficheTexte()
		self.parent.frameCache.place(x= 0, y = 0)
		self.saisieEcrireFichierTexte = SaisieEcrireFichier(self.parent.frameBis, self.fonctionRetourEcrireDatasFichierTexte )
	
	
	
	def fonctionRetourEcrireDatasFichierTexte(self):
		leFileNameSave = self.saisieEcrireFichierTexte.fileName
		
		
		 
		if leFileNameSave:
			datasNoyau = self.parent.datasNoyau
			assert(isinstance(datasNoyau, DatasNoyau))
		
		
			leFileNameComplet = '[Exemples]/[texte]/'+leFileNameSave
			f = open(leFileNameComplet, 'w')
			f.write(datasNoyau.imprimeFichierTexte())
			f.close()
			
			print("\nEnregistrement des datas dans fichier texte")
		
		# nettoyer
		self.parent.frameCache.place_forget()
		self.saisieEcrireFichierTexte.frame.place_forget()
		del self.saisieEcrireFichierTexte 
	
	
# **********************************************************************
# **********************************************************************
 
