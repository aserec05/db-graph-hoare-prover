 
from leftHandSide import *
from rightHandSide import *

class Regle:
	 
	
	# ******************************************************************
	def __init__(self, nom =''):
		self.nom = nom
		self.leftHandSide = LeftHandSide()
		self.rightHandSide = RightHandSide()
	
	
	# ******************************************************************
	def __str__(self):
		chaine = "Regle [" + self.nom + "]\n"
		chaine += str(self.leftHandSide)
		chaine += str(self.rightHandSide)
		 
		return chaine
	
	
	# ******************************************************************
	def getNombreNoeuds(self):
		return self.leftHandSide.nbreNoeud()
		
	def getNombreArcs(self):
		return self.leftHandSide.nbreArcs()
		
	def getNombreActions(self):
		return self.rightHandSide.nbreActions()
	
	# ******************************************************************
	def iterateurNoeuds(self):
		return self.leftHandSide.iterateurNoeuds()
		
	def iterateurArcs(self):
		return self.leftHandSide.iterateurArcs()
		
	def iterateurActions(self):
		return self.rightHandSide.iterateurActions()
	
	# ******************************************************************
	def imprimeVirgule(self):
		chaine = "Regle [" + self.nom + "]\n"
		chaine += self.leftHandSide.imprimeVirgule()
		chaine += self.rightHandSide.imprimeVirgule()
		 
		return chaine
	
	 
	
	
	# ******************************************************************
	def imprimeLesNoeudsFichierAscii(self):
		return self.leftHandSide.imprimeLesNoeudsFichierAscii()
	
	
	# ******************************************************************
	def imprimeLesArcsFichierAscii(self):
		return self.leftHandSide.imprimeLesArcsFichierAscii()
	
	
	# ******************************************************************
	def imprimeLesActionsFichierAscii(self):
		return self.rightHandSide.imprimeLesActionsFichierAscii()
	
	
	# ******************************************************************
	def getLeNom(self):
		return self.nom
		
		
	def getLeftHandSide(self):
		l = self.leftHandSide
		assert(isinstance(l, LeftHandSide))
		return l
	
	
	def getRightHandSide(self):
		r = self.rightHandSide
		assert(isinstance(r, RightHandSide))
		return r
	
	
	# ******************************************************************
	#           left
	# ******************************************************************
	
	def addNom(self, nom):
		self.nom = nom
	
	def addNoeud(self, *args):
		# recoit une liste de mots
		self.leftHandSide.addNoeud(*args)
	
	
	def addArete(self, *args):
		# recoit une liste de mots
		self.leftHandSide.addArc(*args)
	
	
	
	# ******************************************************************
	#           right
	# ******************************************************************
	
	def addAction(self, *args):
		# recoit une liste de mots
		self.rightHandSide.addAction(*args)
	
	
	# ******************************************************************
	#          exemple
	# ******************************************************************
	def unExemple(self):
		self.leftHandSide.unExemple() 
		self.rightHandSide.unExemple() 
		
	def unExemple2(self):
		self.leftHandSide.unExemple2() 
		self.rightHandSide.unExemple2() 
