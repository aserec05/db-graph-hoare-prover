

from arbreFormule import *

from datasNoyau import *
from formuleLogique import *

from leVocabulaire import *
from strategie import *


from calculWpVc import *
from solverZ3 import *



# **********************************************************************
# **********************************************************************
# **********************************************************************

class LeNoyau:
	
	def __init__(self, datas, imprimer = 0):
		self.imprimer = imprimer
		
		# recuperation des données : datas est un objet de la classe 'DatasForNoyau' 
		assert(  isinstance(datas, DatasNoyau) )
		  
		self.vocabulaire =  datas.getVocabulaire() 
		assert(isinstance(self.vocabulaire, LeVocabulaire))
		 
		self.formulePre = datas.getFormulePre()
		assert(isinstance(self.formulePre, FormuleLogique  ))
		
		self.formulePost = datas.getFormulePost()
		assert(isinstance(self.formulePost, FormuleLogique  ))
		
		self.lesRegles =  datas.getLesRegles()
		assert(isinstance(self.lesRegles, SystemeReecriture))
		
		self.strategie =  datas.getStrategie()
		assert(isinstance(self.strategie, Strategie) )
		
		
		# (4) le calcul de la correction de la formule
		self.calculComplet()
		
	
	
	
	
	# ******************************************************************
	#             getters
	# ******************************************************************
	def getArbreFormule(self):
		return self.arbreFormuleCorrection
	
	def getFormuleCompleteZ3(self):
		return self.solverZ3.getFormuleCompleteZ3()
	
	def reponseCourte(self):
		return self.solverZ3.reponseCourte()
	
	def getAnalyseur(self):
		return self.solverZ3.getAnalyseur()
		
	def affichageCompletResolution(self):
		# affiche les éléments transmis par le solver
		self.solverZ3.affichage()
	
	
	
	
	
	
	# ******************************************************************
	# ******************************************************************
	# ******************************************************************
	
	def calculComplet(self):
		VALEUR_IMPRIMER = self.imprimer
		
		
		# **************************************************************
		#   Formule  WP(s, Post)
		# **************************************************************
		# calcul conjoint des formules wp et vc :
		calculWP_VC = CalculWpVc(self.vocabulaire, self.lesRegles , self.strategie , self.formulePost.getArbre())
		
		arbreWPStrategie  = calculWP_VC.getArbreWP( )
		assert(  isinstance(arbreWPStrategie, ArbreFormule) )
		
		arbreVCStrategie  = calculWP_VC.getArbreVC( )
		assert(  isinstance(arbreVCStrategie, ArbreFormule) )
		
		
		# **************************************************************
		#      Formule de correction : Pre => ( wp(s, Post ) And vc(s, Post)
		# **************************************************************
		wpWc = AFconjonction(arbreWPStrategie,arbreVCStrategie)

		
		self.arbreFormuleCorrection = AFimplication(self.formulePre.getArbre(), wpWc)
		
		#self.arbreFormuleCorrection = AFuniversel("x", self.arbreFormuleCorrection)
		
		# **************************************************************
		#       Solveur z3   ----------------------------------------
		# **************************************************************
		
		self.solverZ3 = SolverZ3(self.vocabulaire, self.arbreFormuleCorrection)
		 
		


