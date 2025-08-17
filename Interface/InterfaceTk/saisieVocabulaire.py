
from tkinter import *
 



class SaisieVocabulaire:
	
	def __init__(self, fenetre, fonctionRetour, datasForNoyau):
		self.fenetre = fenetre
		self.fonction_retour = fonctionRetour
		 
		self.leVocabulaire =  datasForNoyau.getVocabulaire()
		
		self.frame = Frame(self.fenetre, width = 700, height = 900, bg='#25ecde')
		self.frame.place(x= 0, y = 0)
		
		self.constructionFrame()
	
	 
	
	# ******************************************************************
	# ******************************************************************
	def constructionFrame(self):
		# le nom
		self.ruleNameTitre = Label(self.frame, text = 'Saisie du vocabulaire de la logique', font = ("times", 15))
		self.ruleNameTitre.place(x= 30, y = 20)
		
		
		# predicats 1
		yConcept = 100
		self.Predicat1 = Label(self.frame, text = 'predicats 1', font = ("times", 15))
		self.Predicat1.place(x= 30, y = yConcept)
		
		self.saisieConcepts = Text(self.frame, height = 6, width = 40, font = ('Helvetica',  15))
		self.saisieConcepts.place (x= 100, y = yConcept+60)
		 
		self.saisieConcepts.insert('insert',  '\n'.join(self.leVocabulaire.getListePredicats_1())  )
		
		
		# predicats 2
		yRole = 360
		self.Predicat2 = Label(self.frame, text = 'predicats 2', font = ("times", 15))
		self.Predicat2.place(x= 30, y = yRole)
		
		self.saisieRoles = Text(self.frame, height = 6, width = 40, font = ('Helvetica',  15))
		self.saisieRoles.place (x= 100, y = yRole+60)
		 
		self.saisieRoles.insert('insert',  '\n'.join(self.leVocabulaire.getListePredicats_2())  )
		
		
		# valider
		self.validationButton = Button(self.frame, text = 'validation Vocabulaire', font = ("times", 15), command = self.validationVocabulaire  )
		self.validationButton.place(x=30, y = 700)
		
		# annuler
		self.annulationButton = Button(self.frame, text = 'aucune modification du vocabulaire', font = ("times", 15), command = self.annulationVocabulaire  )
		self.annulationButton.place(x=430, y = 700)
		
		# un exemple
		self.exempleButton = Button(self.frame, text = 'un exemple', font = ("times", 15), command = self.unExemple  )
		self.exempleButton.place(x = 30, y = 800)
		

	
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
	def unExemple(self):
		exempleConcepts = ['ville', 'personne', 'rue']
		self.saisieConcepts.insert('insert',  '\n'.join(exempleConcepts)  )
		
		exempleRoles = ['est_voisin', 'habite']
		self.saisieRoles.insert('insert',  '\n'.join(exempleRoles)  )
	 
	
	
	# ******************************************************************
	def annulationVocabulaire(self):
		self.fonction_retour()
	
	
	
	# ******************************************************************
	def validationVocabulaire(self):
		# predicats 1
		chaineLesConcepts = self.saisieConcepts.get('1.0', 'end')
		l = chaineLesConcepts.split('\n')
		l = [self.enleveParasites(k) for k in l]
		liste1 = [k for k in l if len(k)>0]
		
		self.leVocabulaire.initPredicat1()
		self.leVocabulaire.addListePredicat1(liste1)
		
		# predicats 2
		chaineLesRoles = self.saisieRoles.get('1.0', 'end')
		l = chaineLesRoles.split('\n')
		l = [self.enleveParasites(k) for k in l]
		liste2 = [k for k in l if len(k)>0]
		
		self.leVocabulaire.initPredicat2()
		self.leVocabulaire.addListePredicat2(liste2)
		
		# fin
		self.fonction_retour()
	
	
