
from tkinter import *
from regle import *



class SaisieRegle:
	
	def __init__(self, fenetre, fonctionRetour, datasNoyau, laRegle = None):
		self.fenetre = fenetre
		self.fonctionRetour = fonctionRetour
		self.datasNoyau = datasNoyau
		
		
		if laRegle : # mode suppression ou modification
			assert(isinstance(laRegle, Regle))
			self.laRegle = laRegle 
			self.nomRegleInitiale = self.laRegle.getLeNom()  #   pour suppression ulterieure ***
			
		else: # mode nouvelle regle
			self.nomRegleInitiale = None
			self.laRegle = Regle()
			
		self.frame = Frame(self.fenetre, width = 700, height = 900, bg='#25ecde')
		self.frame.place(x= 0, y = 0)
		
		self.constructionFrame()
	
	 
	
	# ******************************************************************
	def constructionFrame(self):
		# le nom
		self.ruleNameTitre = Label(self.frame, text = 'Nom', font = ("times", 15))
		self.ruleNameTitre.place(x= 30, y = 20)
		self.alerteOubliNom = Label(self.frame, text = 'Nom obligatoire', font = ("times", 15), bg = 'red')
		
		self.ruleName = StringVar()
		self.ruleName.set(self.laRegle.getLeNom())
		self.entryRuleName = Entry(self.frame, textvariable = self.ruleName, font = ("times", 15), width = 30  )
		self.entryRuleName.place(x= 130, y = 20)
		
		
		# LHS, les noeuds
		yNodes = 100
		self.LHSTitre = Label(self.frame, text = 'LHS : nodes', font = ("times", 15))
		self.LHSTitre.place(x= 30, y = yNodes)
		
		self.saisieNoeuds = Text(self.frame, height = 6, width = 40, font = ('Helvetica',  15))
		self.saisieNoeuds.place (x= 100, y = yNodes)
		 
		self.saisieNoeuds.insert('insert',  self.laRegle.getLeftHandSide().imprimeLesNoeudsAvecDesVirgules())
		#~ print( self.laRegle.getLeftHandSide().printLesNoeudsPourSaisie())
		
		
		# ajouter des arcs
		yEdges = 300
		self.edgesTitre = Label(self.frame, text = 'edges', font = ("times", 15))
		self.edgesTitre.place(x= 30, y = yEdges)
		
		self.saisieAretes = Text(self.frame, height = 6, width = 40, font = ('Helvetica',  15))
		self.saisieAretes.place (x= 100, y = yEdges)
		
		self.saisieAretes.insert('insert',  self.laRegle.getLeftHandSide().imprimeLesArcsAvecDesVirgules())
		#~ print( self.laRegle.getLeftHandSide().printLesAretesPourSaisie())
		
		
		# ajouter des actions
		yActions = 500
		self.actionTitre = Label(self.frame, text = 'actions', font = ("times", 15))
		self.actionTitre.place(x= 30, y = yActions)
		
		self.saisieActions = Text(self.frame, height = 6, width = 40, font = ('Helvetica',  15))
		self.saisieActions.place (x= 100, y = yActions)
		
		self.saisieActions.insert('insert',  self.laRegle.getRightHandSide().printLesActionsPourSaisie())
		#~ self.saisieNoeuds.insert('insert',  self.formule_initiale)
		
		
		# valider
		self.validationButton = Button(self.frame, text = 'valider la Regle', font = ("times", 15), command = self.validationRegle  )
		self.validationButton.place(x = 30, y = 800)
		
		
		# annuler la saisie
		self.annulationSaisieButton = Button(self.frame, text = 'annuler la saisie', font = ("times", 15), command = self.annulationSaisie  )
		self.annulationSaisieButton.place(x = 230, y = 800)
		
		
		# detruire la regle
		self.destructionRegleButton = Button(self.frame, text = 'supprimer la regle', font = ("times", 15), command = self.destructionRegle )
		self.destructionRegleButton.place(x = 430, y = 800)
		

	
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
	def addAction(self, chaine):
		#~ print('addAction')
		listeMots = chaine.split(',')
		listeMots = [self.enleveParasites(m) for m in listeMots]
		#~ print(listeMots)
		self.laRegle.addAction(*listeMots)
	
	
	# ******************************************************************
	def addNode(self, chaine):
		#~ print('addNode')
		listeMots = chaine.split(',')
		listeMots = [self.enleveParasites(m) for m in listeMots]
		#~ print(listeMots)
		self.laRegle.addNoeud(*listeMots)
	
	
	# ******************************************************************
	def addEdge(self, chaine):
		#~ print('addEdge')
		listeMots = chaine.split(',')
		listeMots = [self.enleveParasites(m) for m in listeMots]
		#~ print(listeMots)
		self.laRegle.addArete(*listeMots)
		 
	
	# ******************************************************************
	def imprimeRegleconsole(self):
		print(self.laRegle)
	
	
	# ******************************************************************
	def annulationSaisie(self):
		self.laRegle = None
		self.fonctionRetour()
	
	# ******************************************************************
	def destructionRegle(self):
		if self.nomRegleInitiale:
			self.datasNoyau.delRegle(self.nomRegleInitiale)  # *************************************************
			self.laRegle = None
			self.fonctionRetour()
		else : 
			print("rien à supprimer")
	
	
	# ******************************************************************
	def validationRegle(self):
		self.laRegle = Regle() # re-initialisation
		
		# nom obligatoire
		nom = self.ruleName.get()
		nom = self.enleveParasites(nom)
		if nom == '':
			self.alerteOubliNom.place(x= 500, y = 20)
			return 
		
		self.laRegle.addNom(nom)
		
		# noeuds
		chaineLesNoeuds = self.saisieNoeuds.get('1.0', 'end')
		l = chaineLesNoeuds.split('\n')
		l = [self.enleveParasites(k) for k in l]
		l = [k for k in l if len(k)>0]
		for chaine in l :
			self.addNode(chaine)
		
		# aretes
		chaineLesAretes = self.saisieAretes.get('1.0', 'end')
		#~ print(chaineLesAretes)
		l = chaineLesAretes.split('\n')
		#~ print(l)
		#~ print(len(l))
		l = [self.enleveParasites(k) for k in l]
		l = [k for k in l if len(k)>0]
		
		for chaine in l :
			self.addEdge(chaine)
		
		# actions
		chaineLesActions = self.saisieActions.get('1.0', 'end')
		 
		l = chaineLesActions.split('\n')
		l = [self.enleveParasites(k) for k in l]
		l = [k for k in l if len(k)>0]
		for chaine in l :
			self.addAction(chaine)
		
		# ajout de la regle à l'objet DatasNoyau
		if self.laRegle: 
			self.datasNoyau.addRegle(self.laRegle)
		
		# fin
		self.fonctionRetour()
	
