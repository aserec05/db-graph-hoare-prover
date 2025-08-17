from  action import *
 

class RightHandSide:
	
	def __init__(self):
		self.laListeActions = []
	
	# ******************************************************************
	
	
	def __str__(self):
		chaine = "[RHS]\nNombre d'action(s) = {}".format(len(self.laListeActions)) + "\n" 
		for action in self.laListeActions:
			chaine += str(action)+'\n'
		
		return chaine
	
	
	# ******************************************************************
	def __iter__(self): #ordre à modifier : voir regle (priorité) pour le calcul de wp
		ordre_inverse = [elt for elt in self.laListeActions] # car mutable
		ordre_inverse.reverse() # sur place
		return iter(ordre_inverse)
	
	
	def iterateurActions(self):
		return iter(self)
		
		
	def nbreActions(self):
		return len(self.laListeActions)
	
	
	# ******************************************************************
	def imprimeVirgule(self):
		chaine = "[RHS]\nNombre d'action(s) = {}".format(len(self.laListeActions)) + "\n" 
		for action in self.laListeActions:
			chaine += action.imprimeVirgule()+'\n'
		 
		return chaine
	
	def imprimeLesActionsFichierAscii(self):
		chaine = str(self.nbreActions()) + '\n'
		for action in self.laListeActions:
			chaine += action.imprimeVirgule()+'\n'
		return chaine
	
	def printLesActionsPourSaisie(self):
		chaine = ""
		for n in self.laListeActions:
			chaine += n.imprimeVirgule() + "\n"
		return chaine
	
	# ******************************************************************
	def addAction(self, *args):
		a = Action(*args)
		self.laListeActions.append(a)
	
	
	
	# ******************************************************************
	#          exemple
	# ******************************************************************
	def unExemple(self):
		#~ self.laListeActions.append(Action("add_C", 'variable_i', 'concept_c') )
		self.addAction("add_E", 'p', 'w', 'habite' )
		self.addAction("del_E", 'p', 'v', 'habite' )
	
	 
	def unExemple2(self):
		#~ self.laListeActions.append(Action("add_C", 'variable_i', 'concept_c') )
		self.addAction("add_C", 'p',  'ville' )
	
	
	
	
	
	
