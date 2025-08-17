
from tkinter import *
import pickle


from interfaceFichiers import *

from leNoyau import *

from saisieVocabulaire import *
from saisieFormule import *
from saisieRegle import *
from saisieStrategie import *

from datasNoyau import *
from strategie import *


class Interface:
	
	def __init__(self, fenetre ):
		self.fenetre = fenetre
		self.datasNoyau = DatasNoyau()
		
		
		# setup
		self.construction_frames()
	
	
	
	# ******************************************************************
	#         (0)  deux   FRAMES
	# ******************************************************************
	def construction_frames(self):
		
		# cadre 1 : commandes
		self.frameFichiers = InterfaceFichiers(self, self.fenetre)
		
		
		
		
		# cadre 2 : saisie
		self.frameSaisie = Frame(self.fenetre, width = 700, height = 600, bg='#cdecde')
		self.frameSaisie.place(x= 0, y = 300)
		self.constructionFrameSaisie()
		
		# cadre 3 : frameBis
		self.frameBis = Frame(self.fenetre, width = 700, height = 900, bg='#55dd44')
		self.frameBis.place(x= 700, y = 0)
		#~ self.constructionAffichage()
		
		# frame qui masque le frame Menu pendant les saisies
		self.frameCache = Frame(self.fenetre, width = 700, height = 900, bg='#125741')
		
		self.afficheTexte = None
	
	
	
	# ******************************************************************
	# ******************************************************************
	#         (1)  Frame  Menu
	# ******************************************************************
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
		self.buttonAction = Button(self.frameMenu, text = 'Console : imprime la preuve', font = ("times", 15), command = self.imprimePreuveConsole )
		self.buttonAction.place(x= xMarge, y = yConsole)
		
		# imprime les datas
		self.imprimeDatasConsoleButton = Button(self.frameMenu, text = 'Console : imprime datas', font = ("times", 15), command = self.imprimeDatasConsole)
		self.imprimeDatasConsoleButton.place(x= xMarge + 300 , y = yConsole)
	
		
		
	
	# ******************************************************************
	# ******************************************************************
	#         (1)  Frame  saisie
	# ******************************************************************
	# ******************************************************************
	def constructionFrameSaisie(self):
		xMarge = 30
		
		# **************************************************************
		# **************************************************************
		# saisir logique / vocabulaire
		yLogique = 20
		self.buttonSaisirLogique = Button(self.frameSaisie, text = 'saisir ou modifier Logique', font = ("times", 15), command = self.saisirLogique )
		self.buttonSaisirLogique.place(x= 30, y = yLogique)
		
		# formule Pre  
		yPre = 100
		self.buttonSaisirPre = Button(self.frameSaisie, text = 'saisir ou modifier la formule Pre', font = ("times", 15), command = lambda x= 'pre' :self.saisirFormule(x)  )
		self.buttonSaisirPre.place(x= xMarge, y = yPre)

		self.textFormulePre = StringVar()
		self.textFormulePre.set('...')
		self.labelPre = Label(self.frameSaisie, textvariable = self.textFormulePre, font = ("times", 15) , width = 50, bg='#eeeeee' )
		self.labelPre.place(x= xMarge, y = yPre + 50)

		# formule   Post
		yPost = 220
		self.buttonSaisirPost = Button(self.frameSaisie, text = 'saisir ou modifier la formule Post', font = ("times", 15), command = lambda x= 'post' :self.saisirFormule(x) )
		self.buttonSaisirPost.place(x= xMarge, y = yPost)
		 
		self.textFormulePost = StringVar()
		self.textFormulePost.set('...')
		self.labelPost = Label(self.frameSaisie, textvariable = self.textFormulePost, font = ("times", 15) , width = 50 , bg='#eeeeee' )
		self.labelPost.place(x= xMarge, y = yPost + 50)
		
		
		# saisie regle
		self.yRegle = 350
		self.buttonSaisirRegle = Button(self.frameSaisie, text = 'saisir une nouvelle regle', font = ("times", 15), command = self.saisirRegle )
		self.buttonSaisirRegle.place(x= 30, y = self.yRegle)
		
		self.buttonAfficherLesRegles = Button(self.frameSaisie, text = 'afficher les regles', font = ("times", 15), command = self.afficherLesRegles )
		self.buttonAfficherLesRegles.place(x= 330, y = self.yRegle)
		
		# boutons de modification des regles
		self.listeBoutonsRegles = []
		self.afficheBoutonsRegles( )
		
		 
		#  strategie
		yStrategie = 480

		self.buttonStrategie = Button(self.frameSaisie, text = 'saisir ou modifier la strategie', font = ("times", 15), command =  self.saisirStrategie )
		self.buttonStrategie.place(x= xMarge, y = yStrategie)

		self.buttonImprimeStrategie = Button(self.frameSaisie, text = 'afficher la Strategie', font = ("times", 15), command =  self.imprimerStrategie )
		self.buttonImprimeStrategie.place(x= xMarge+300, y = yStrategie)
		 
		self.chaineStrStrategie = StringVar()
		self.chaineStrStrategie.set('...')
		self.labelPost = Label(self.frameSaisie, textvariable = self.chaineStrStrategie, font = ("times", 15) , width = 50, bg='#eeeeee'  )
		self.labelPost.place(x= xMarge, y = yStrategie + 50)
	
	
	 
	
	
	# ******************************************************************
	#          saisie        vocabulaire
	# ****************************************************************** 
	def saisirLogique(self):
		self.enleveAfficheTexte()
		self.frameCache.place(x= 0, y = 0)
		self.saisieVocabulaire = SaisieVocabulaire(self.frameBis, self.fonctionRetourSaisieLogique,  self.datasNoyau)
	
	
	def fonctionRetourSaisieLogique(self):
		self.frameCache.place_forget()
		self.saisieVocabulaire.frame.place_forget()
		del self.saisieVocabulaire
	
	
	
	# ******************************************************************
	#          saisie         PRE  et  POST
	# ****************************************************************** 
	def saisirFormule(self, indiceFormule):
		assert(indiceFormule in ['pre', 'post'])
		self.enleveAfficheTexte()
		self.frameCache.place(x= 0, y = 0)
		self.saisie = SaisieFormule(self.frameBis, self.fonctionRetourSaisieFormule, indiceFormule, self.datasNoyau )
		 
	
	def fonctionRetourSaisieFormule(self, indiceFormule):
		assert(indiceFormule in ['pre', 'post'])
		# on recupere un objet FormuleLogique ou None
		laFormule = self.saisie.formuleLogique
		
		if laFormule and indiceFormule == 'pre':
			assert(isinstance(laFormule, FormuleLogique))
			formulePre = laFormule.getChaineUnicode()
			self.textFormulePre.set(formulePre)
			self.datasNoyau.addFormulePre(laFormule)   
		
		elif laFormule and indiceFormule == 'post':
			assert(isinstance(laFormule, FormuleLogique))
			formulePost = laFormule.getChaineUnicode()
			self.textFormulePost.set(formulePost)
			self.datasNoyau.addFormulePost(laFormule)  
			
		self.frameCache.place_forget()
		self.saisie.frame.place_forget()
		del self.saisie


	# ******************************************************************
	#          saisie       REGLE
	# ******************************************************************
	def saisirRegle(self):
		self.enleveAfficheTexte()
		# masquer partie gauche
		self.frameCache.place(x= 0, y = 0)
		self.saisieRegle = SaisieRegle(self.frameBis, self.fonctionRetourSaisieRegle, self.datasNoyau )
	
	
	def modifieRegle(self, laRegle):
		self.enleveAfficheTexte()
		self.frameCache.place(x= 0, y = 0)
		self.saisieRegle = SaisieRegle(self.frameBis, self.fonctionRetourSaisieRegle , self.datasNoyau, laRegle )
	
	
	def fonctionRetourSaisieRegle(self):
		self.afficheBoutonsRegles()
		
		self.frameCache.place_forget()
		self.saisieRegle.frame.place_forget()
		del self.saisieRegle

	
	def afficheBoutonsRegles(self):
		while self.listeBoutonsRegles:
			b = self.listeBoutonsRegles.pop()
			b.destroy()
		self.listeBoutonsRegles = []
		pos = 30
		for nomRegle in self.datasNoyau.getLesRegles().lesNomsDesregles() :
			laRegle = self.datasNoyau.getLesRegles().getRegle(nomRegle)
			b = Button(self.frameSaisie, text = nomRegle, command = lambda x= laRegle :self.modifieRegle(x))
			self.listeBoutonsRegles.append(b)
			b.place(x = pos, y =  self.yRegle + 60)
			pos += 100
	
	
	
	def afficherLesRegles(self):
		texte = "Les regles : \n" + str(self.datasNoyau.getLesRegles()) 
		self.afficheTexte = AfficheTexte(self.frameBis, texte)
	
	
	 
	# ******************************************************************
	#          saisie       STRATEGIE
	# ******************************************************************
	def saisirStrategie(self):
		self.enleveAfficheTexte()
		self.frameCache.place(x= 0, y = 0)
		self.saisieStrategie = SaisieStrategie(self.frameBis, self.fonctionRetourSaisieStrategie,  self.datasNoyau)
	
	
	def fonctionRetourSaisieStrategie(self):
		# on recupere un objet Strategie mais pas de nouvelle affectation à éffectuer !
		#~ laStrategie = self.saisieStrategie.laStrategie
		
		self.chaineStrStrategie.set(self.datasNoyau.getStrategie().getFormuleStrategie() )
		
		self.frameCache.place_forget()
		self.saisieStrategie.frame.place_forget()
		del self.saisieStrategie
	
	
	def imprimerStrategie(self):
		texte = "Strategie : \n" + str(self.datasNoyau.getStrategie()) 
		self.afficheTexte = AfficheTexte(self.frameBis, texte)
		 
	
	# ******************************************************************
	#         enleveAfficheTexte
	# ******************************************************************
	def enleveAfficheTexte(self):
		if self.afficheTexte:
			print("ok self.afficheTexte")
			#~ self.afficheTexte.frame.place_forget()
			#~ a = self.afficheTexte.frame
			#~ print(a)
			self.afficheTexte.efface()
			self.afficheTexte = None
			#~ print(a) 
	
	
	
	
	# ******************************************************************
	# ******************************************************************
	# ******************************************************************
	def updateAffichageDataNoyau(self, datasNoyau):
		self.datasNoyau = datasNoyau
		
		
		# afficher les datas
		if self.datasNoyau.getFormulePre(): 
			self.textFormulePre.set(self.datasNoyau.getFormulePre().getChaineUnicode())
		if self.datasNoyau.getFormulePost():
			self.textFormulePost.set(self.datasNoyau.getFormulePost().getChaineUnicode())

		self.afficheBoutonsRegles( )
		self.chaineStrStrategie.set(self.datasNoyau.getStrategie().getFormuleStrategie() )

	
	# ******************************************************************
	#          calcul  Correction
	# ******************************************************************	 
	def calculCorrection(self):
		self.enleveAfficheTexte()
		imprimer = 0
		lenoyau = LeNoyau(self.datasNoyau, imprimer)
		
		f = lenoyau.getFormuleCompleteZ3() 
		assert(  isinstance(f, z3.BoolRef) )
		
		self.reponse = "[Formule à valider] ----------------------  \n\n    {}\n\n".format(f)
		self.reponse += "\n[Calcul de la correction avec Z3] ---------------------- \n"
		self.reponse += str(lenoyau.reponseCourte()) + "\n\n"
		
		#~ 
		
		#~ fi = open('[Exemples]/reponse', 'w')
		#~ fi.write(reponse)
		#~ fi.close()
 
	
	
	# ******************************************************************
	# ******************************************************************
	# ******************************************************************
	# ******************************************************************
	def imprimeDatasConsole(self):
		print(self.datasNoyau)
	
	
	
	
	
	def imprimePreuveConsole(self):
		self.calculCorrection()
		print(self.reponse)
	
	 
	
	 
	
	 
	 


# **********************************************************************
# **********************************************************************
# **********************************************************************
 
