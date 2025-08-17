
from tkinter import *
from saisieFormule import *



class SaisieStrategie:
	
	def __init__(self, fenetre, fonctionRetour, datasForNoyau):
		self.fenetre = fenetre
		 
		self.fonctionRetour = fonctionRetour
		self.datasNoyau = datasForNoyau
		self.laStrategie = datasForNoyau.getStrategie()
		#~ self.chaineStrategie = ''
		
		self.frame = Frame(self.fenetre, width = 700, height = 900, bg='#e2a4de')
		self.frame.place(x= 0, y = 0)
		
		self.constructionFrame()
	
	 
	
	# ******************************************************************
	def constructionFrame(self):
		xMarge = 30
		
		# titre
		self.titre = Label(self.frame, text = 'Assistant de saisie de la strategie', font = ("times", 15))
		self.titre.place(x= xMarge, y = 90)
		
		# cadre de saisie de la chaine principale
		self.chaineLaStrategie = StringVar()
		self.chaineLaStrategie.set(self.laStrategie.getFormuleStrategie() )
		self.entryStrategie = Entry(self.frame, textvariable = self.chaineLaStrategie, font = ("times", 15), width = 30  )
		self.entryStrategie.place(x = xMarge, y = 150)
		
		# bouton pour imprimer les invariants
		self.buttonImprimeStrategie = Button(self.frame, text = 'imprimer les invariants', font = ("times", 15), command =  self.imprimerInvariants )
		self.buttonImprimeStrategie.place(x= xMarge, y = 240)
		
		# bouton pour ajouter une formule d'invariant pour une opération etoile
		self.ajoutInvariantEtoileButton = Button(self.frame, text = 'ajouter invariant', font = ("times", 15), command = self.ajouterInvariant  )
		self.ajoutInvariantEtoileButton.place(x = xMarge, y = 310)
		
		
		# bouton pour modifier une formule d'invariant pour une opération etoile
		self.titreModifier = Label(self.frame, text = 'modifier invariant', font = ("times", 15))
		self.titreModifier.place(x= xMarge, y = 370)
		
		self.afficheBoutonsModification( )
		
		 
		# valider la strategie et quitter
		self.validationButton = Button(self.frame, text = 'validation Strategie', font = ("times", 15), command = self.validationStrategie  )
		self.validationButton.place(x = xMarge, y = 510)
		
		
	
	
	# ******************************************************************
	def enleveParasites(self, chaine):
		''' enleve espace et saut de ligne'''
		listeCaracteres = list(chaine)
		
		caractereParasite = [' ', '\n']
		for c in caractereParasite :
			while c in listeCaracteres:
				listeCaracteres.remove(c)

		chaineFinale = ''.join(listeCaracteres)
		return chaineFinale
	
	
	

	# ******************************************************************
	#         ajouter invariant
	# ****************************************************************** 
	def ajouterInvariant(self):
		self.saisieInvariant = SaisieFormule(self.fenetre, self.fonctionRetourSaisieInvariant, 'inv', self.datasNoyau )
	
	
	def fonctionRetourSaisieInvariant(self, indiceInutile):
		# on recupere un objet FormuleLogique
		laFormule = self.saisieInvariant.formuleLogique
		assert(isinstance(laFormule, FormuleLogique))
		 
		# formule à écrire
		self.laStrategie.addInvariant(laFormule)
		self.afficheBoutonsModification()
		
		self.saisieInvariant.frame.place_forget()
		del self.saisieInvariant
		  
	

	# ******************************************************************
	#         modifier invariant
	# ****************************************************************** 
	def modifierInvariant(self, indiceEntier):
		print("modifier invariant " , indiceEntier)
		self.saisieInvariant = SaisieFormule(self.fenetre, self.fonctionRetourModificationInvariant, indiceEntier, self.datasNoyau )
	
	
	
	def fonctionRetourModificationInvariant(self, indice):
		# on recupere une chaine de caracteres
		laFormule = self.saisieInvariant.formuleLogique
		assert(isinstance(laFormule, FormuleLogique))
		
		# formule à écrire
		self.laStrategie.modifieInvariant(indice, laFormule)
		self.afficheBoutonsModification()
		
		self.saisieInvariant.frame.place_forget()
		del self.saisieInvariant
		  
	
	
	def afficheBoutonsModification(self):
		self.liste_boutons = []
		pos = 230
		listeDesInvariants = self.laStrategie.lesInvariants # à modifier avec iterateur
		
		for indice in range(len(listeDesInvariants)):
			b = Button(self.frame, text = str(indice), command = lambda x= indice :self.modifierInvariant(x))
			self.liste_boutons.append(b)
			b.place(x = pos, y =  370)
			pos += 50	
	
	 
	
	# ******************************************************************
	def validationStrategie(self):
		chaine = self.chaineLaStrategie.get()
		chaine = self.enleveParasites(chaine)

		self.laStrategie.saisieFormuleStrategie(chaine) # declenche l'analyse syntaxique

		self.fonctionRetour()
	
	
	
	def imprimerInvariants(self):
		print("les invariants : ")
		print(self.laStrategie.imprimerInvariants())
		
 
 
  

