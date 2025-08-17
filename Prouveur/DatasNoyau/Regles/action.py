class Action:
	
	listeDesActions = ['add_N', 'del_N', 'add_C', 'del_C', 'add_E', 'del_E', 'redirection', 'merge']
	
	
	
	# ******************************************************************
	def __init__(self,  leNom, *args):
		
		assert( leNom in self.listeDesActions )
		self.leNom = leNom
		
		self.lesArguments = tuple(args)
		
		if leNom == 'add_N' : self.creationNode()
		elif leNom == 'del_N' : self.destructionNode()
		
		elif leNom == 'add_C' : self.ajouteConcept()
		elif leNom == 'del_C' : self.destructionConcept()
		
		elif leNom == 'add_E' : self.ajouteEdge()
		elif leNom == 'del_E' : self.destructionEdge()
		 
		elif leNom == 'merge' : self.fusion()
		elif leNom == 'redirection' : self.redirection()
		
		else : # ne peut pas se produire ************
			print("probleme action")
	
	
	# ******************************************************************
	def __str__(self):
		chaine = "[{}] ".format(self.leNom) + " - ".join(self.lesArguments) 
		return chaine
	
	
	# ******************************************************************
	def imprimeVirgule(self):
		liste = [self.leNom] + list(self.lesArguments)
		chaine =   ", ".join(liste)
		return chaine
	
	
	# ******************************************************************
	#~ def ecritureFichier(self):
		#~ ''' permet la sauvegarde d'une action :
		#~ ecriture dans un fichier '''
		#~ chaine = str(self.name)
		#~ for elt in self.tupleParametres :
			#~ chaine += ' | '+str(elt)
		
		#~ return chaine
	
	# ******************************************************************
	def getLeNom(self):
		return self.leNom
	
	# ******************************************************************
	def getLesArguments(self):
		return self.lesArguments
	
	
	# ******************************************************************
	def creationNode(self):
		assert(len(self.lesArguments) == 1)
		self.leNoeud = self.lesArguments[0]
	
	
	def destructionNode(self):
		assert(len(self.lesArguments) == 1)
		self.leNoeud = self.lesArguments[0]
	
	
	def ajouteConcept(self):
		assert(len(self.lesArguments) == 2)
		self.leNoeud = self.lesArguments[0]
		self.leConcept = self.lesArguments[1]
	
	
	def destructionConcept(self):
		assert(len(self.lesArguments) == 2)
		self.leNoeud = self.lesArguments[0]
		self.leConcept = self.lesArguments[1]
	
	
	def ajouteEdge(self):
		assert(len(self.lesArguments) == 3)
		self.laSource = self.lesArguments[0]
		self.laCible = self.lesArguments[1]
		self.leRole = self.lesArguments[2]
	
	
	def destructionEdge(self):
		assert(len(self.lesArguments) == 3)
		self.laSource = self.lesArguments[0]
		self.laCible = self.lesArguments[1]
		self.leRole = self.lesArguments[2]
	
	
	def fusion(self):
		assert(len(self.lesArguments) == 2)
		self.noeudOne = self.lesArguments[0]
		self.noeudTwo = self.lesArguments[1]
	 
	
	def redirection(self):
		assert(len(self.lesArguments) == 2)
		self.noeudOne = self.lesArguments[0]
		self.noeudTwo = self.lesArguments[1]
	
	 
	
	
	
# **********************************************************************

def addConcept(nom, predicat1):
	return Action("add_C", nom, predicat1)

def delConcept(nom, predicat1):  # **************************************************** ???
	return Action("del_C", nom, predicat1)


def addRole(nom, source, cible, predicat2):
	return Action("add_R", nom, source, cible, predicat2)

def delRole(nom, source, cible, predicat2):  # **************************************************** ???
	return Action("del_R", nom, source, cible, predicat2)










# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************

if __name__ == '__main__':
	
	a= Action("add_C", 'variable_i', 'concept_c')
	
	b = addConcept('r', 'concept')
	
	print(a)
	print(a.imprimeVirgule())
	
	print(b)
	print(b.imprimeVirgule())
