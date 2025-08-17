
''' gere la liste des predicats
'''


class LeVocabulaire:
	
	
	
	# ******************************************************************
	def __init__(self):
		self.concepts = [] # predicats unaires 1
		self.roles = []  # predicats binaires 2
	
	
	
	# ******************************************************************
	def __str__(self):
		chaine = 'Concepts (predicats unaires) : \n' + " - ".join(self.concepts )
		chaine += '\nRoles (predicats binaires) : \n' + " - ".join(self.roles )  
		return chaine
	
	
	
	# ******************************************************************
	def initPredicat1(self):
		self.concepts = []
	
	
	def addPredicat1(self, p):
		assert(isinstance(p, str) )
		if p not in self.concepts:
			self.concepts.append(p)
	
	
	def addListePredicat1(self, laliste):
		for p in laliste:
			self.addPredicat1(p)
	
	
	# ******************************************************************
	def initPredicat2(self):
		self.roles = []
	
	
	def addPredicat2(self, p):
		assert(isinstance(p, str) )
		if p not in self.roles:
			self.roles.append(p)
	
	def addListePredicat2(self, laliste):
		for p in laliste:
			self.addPredicat2(p)
	 
	
	# ******************************************************************
	def getListePredicats_1(self):
		return self.concepts
		
	def getListePredicats_2(self):
		return self.roles
	 
	
	
	# ******************************************************************
	# ******************************************************************
	
	def unExemple(self):
		# utilisé pour les tests des autres classes 
		
		self.addListePredicat1(['ville', 'personne'])
		self.addListePredicat2(['habite', 'est_voisin_de'])
		 
		  
