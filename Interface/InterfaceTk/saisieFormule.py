
from tkinter import *

from formuleLogique import *

from symbolesLogique import *

class SaisieFormule:
	
	# ******************************************************************
	def __init__(self, parent , fonction_retour, indiceFormule, datasForNoyau):
		self.fenetre = parent
		
		self.frame = Frame(self.fenetre, width = 700, height = 900, bg='#25ecde')
		self.frame.place(x= 0, y = 0)
		
		self.fonction_retour = fonction_retour
		
		
		self.indiceFormule = indiceFormule
		
		self.formuleInitiale = ''
		#~ assert(indiceFormule in ['pre', 'post', 'inv'])
		if indiceFormule == 'pre' :
			formulePre = datasForNoyau.getFormulePre()
			if formulePre:
				self.formuleInitiale = formulePre.getChaineUnicode()
				
		elif indiceFormule == 'post' :
			formulePost = datasForNoyau.getFormulePost()
			if formulePost:
				self.formuleInitiale = formulePost.getChaineUnicode()
				
		elif indiceFormule == 'inv' : # invariant pour une regle * de la strategie
			self.formuleInitiale = ''
			
		else : # modification d'un invariant pour une regle * de la strategie
			assert(isinstance(indiceFormule, int) )
			
			formuleLogique = datasForNoyau.getStrategie().lesInvariants[indiceFormule]
			assert( isinstance(formuleLogique, FormuleLogique))
			self.formuleInitiale = formuleLogique.getChaineUnicode()
		
		
		
		self.vocabulaire = datasForNoyau.getVocabulaire()
		self.formuleLogique = None
		
		self.construction()
	
	 
	# ******************************************************************
	def construction(self):
		# --------------------------------------------------------------
		#            boutons : predicats et fonctions
		# --------------------------------------------------------------
		self.liste_boutons = []
		
		pos = 20
		lesPredicats1 = self.vocabulaire.getListePredicats_1()
		for k in  lesPredicats1:
			b = Button(self.frame, text = k, command = lambda x= k :self.ecrit_predicat(x))
			self.liste_boutons.append(b)
			b.place(x = pos, y = 30)
			pos += 100
		
		pos = 20
		lesPredicats2 = self.vocabulaire.getListePredicats_2()
		for k in lesPredicats2:
			b = Button(self.frame, text = k, command = lambda x = k :self.ecrit_predicat(x))
			self.liste_boutons.append(b)
			b.place(x = pos, y = 110)
			pos += 100
		
		# --------------------------------------------------------------
		#                caracteres speciaux 
		# --------------------------------------------------------------
		pos = 20
		lesCaracteres = getTupleSymboles()
		for k in lesCaracteres:
			b = Button(self.frame, text = chr(k), command = lambda x= k :self.ecrit_caractere(x))
			self.liste_boutons.append(b)
			b.place(x = pos, y = 200)
			pos += 50
		
		# --------------------------------------------------------------
		#           zone de saisie
		# --------------------------------------------------------------
		#t = Text(fenetre, height = 10, width = 40, font = ("Purisa", 15))
		self.zoneSaisie = Text(self.frame, height = 10, width = 40, font = ('Helvetica',  15)     )
		self.zoneSaisie.place (x= 50, y = 300)
		 
		self.zoneSaisie.insert('insert',  self.formuleInitiale)
		
		
		# --------------------------------------------------------------
		#            boutons : validation, test
		# --------------------------------------------------------------
		self.valid = Button(self.frame, text = 'validation',font = ("times", 15), command = self.validation)
		self.valid.place(x= 30, y = 700)
		
		self.testbutton = Button(self.frame, text = 'exemple',font = ("times", 15), command = self.exemple)
		self.testbutton.place(x= 230, y = 700)
		
		self.annulationButton = Button(self.frame, text = 'annulation',font = ("times", 15), command = self.annulation)
		self.annulationButton.place(x= 430, y = 700)
	 
	
	
	
	# ******************************************************************
	# ******************************************************************
	def ecrit_caractere(self, indice):
		# pour insertion en fin de chaine : 'end'
		self.zoneSaisie.insert('insert', chr(indice))
	
	 
	# ******************************************************************
	def ecrit_predicat(self, chaine):
		# pour insertion en fin de chaine : 'end'
		self.zoneSaisie.insert('insert', chaine)
	
	
	# ******************************************************************
	def exemple(self):
		chaine = chr(8704)+"x(personne(x)" + chr(8658)+chr(8707)+"z(ville(z)"+chr(8743)+"habite(x,z)))"
		self.zoneSaisie.insert('insert',  chaine)
		 
 
	
	# ******************************************************************
	# ******************************************************************
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
	def validation(self):
		self.chaine = self.zoneSaisie.get('1.0', 'end')
		self.chaine  = self.enleveParasites(self.chaine )
		
		
		self.formuleLogique = FormuleLogique(self.chaine, self.vocabulaire)
		# declenche l'analyse syntaxique
		
		self.fonction_retour(self.indiceFormule)
	
	
	# ******************************************************************
	def annulation(self):
		self.formuleLogique = None
		self.fonction_retour(self.indiceFormule)
	
	 
 

