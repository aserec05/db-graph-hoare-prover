from regle import *
 

from arbreFormule import *
from calculAppRegle import *
from calculWpAction import *




class CalculateurWPRegle:
	def __init__(self, regle, formule ):
		
		
		assert(isinstance(regle, Regle))
		assert(isinstance(formule, ArbreFormule))
		
		self.regle = regle
		self.formule = formule
		self.calculWPRegle()
	
	
	
	# ******************************************************************
	# ******************************************************************
	
	def calculWPRegle(self ):
		VALEUR_IMPRIMER = 0
		 
		 

		# 1) calcul de APP(LeftHandSide(regle))
		
		c = CalculAppRegle(self.regle.getLeftHandSide()) 
		self.arbreApp = c.getArbreApp()
		#~ print(type(self.arbreApp))
		assert(  isinstance(self.arbreApp,  ArbreFormule) )

		
		# 2) calcul de WP( RightHandSide(regle), Formule)
		wpAction = CalculateurWPAction(self.regle.getRightHandSide(), self.formule,  imprimer = VALEUR_IMPRIMER)   
		
		arbreWp =  wpAction.calculeWP()
		assert(  isinstance(arbreWp,  ArbreFormule) )
		
		
		# 3)   calcul de l'implication : APP => WP(action, Formule) 
		self.arbreImplication = AFimplication(self.arbreApp, arbreWp)
		
		 
	def getArbreWP(self):
		return self.arbreImplication
		 
	def getAppRegle(self):
		return self.arbreApp
	
	
	 
