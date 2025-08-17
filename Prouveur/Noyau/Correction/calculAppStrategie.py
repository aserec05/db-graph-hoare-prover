 
import arbreFormule as af
from leVocabulaire import *
from leftHandSide import *
from arbreStrategie import *
from systemeReecriture import *

from calculAppRegle import *



class CalculAppStrategie:

	"""
	Calcule des Apply de la strategie
	"""
	 
	
	def __init__(self, arbreStrategie, lesRegles):
		
		assert(isinstance(arbreStrategie, ArbreStrategie))
		assert(isinstance(lesRegles, SystemeReecriture))
		self.arbreAppStrategie = None
		self.lesRegles = lesRegles

		self.lesReglesApp = [] # liste des règles qui vont se retrouver dans le calcul de App(s)
		
		self.arbreAppStrategie = self.calculArbreAppStrategie(arbreStrategie)
	
		
	 
	# ******************************************************************
	#                   getter           
	# ******************************************************************
	def getArbreApp(self):
		return self.arbreAppStrategie
	
	def getReglesApp(self):
		return self.lesReglesApp
	
	# ******************************************************************
	def calculArbreAppStrategie(self, arbreStrategie):
		
		 
		if arbreStrategie.estUneRegle():

			nomRegle = arbreStrategie.getLabel()
			
			laRegle = self.lesRegles.getRegle(nomRegle) # <-- doit rennomer les variable
			assert(  isinstance(laRegle, Regle) )
			
			self.lesReglesApp.append(laRegle)

			c = CalculAppRegle(laRegle.getLeftHandSide()) 
			arbreApp = c.getArbreApp()
			assert(  isinstance(arbreApp, af.ArbreFormule) )
			
			return arbreApp
		
		
		# --------------------------------------------------------------
		# --------------------------------------------------------------
		#           SINON
		# --------------------------------------------------------------
		# --------------------------------------------------------------
		label = arbreStrategie.getLabel()
		
		
		# --------------------------------------------------------------
		if label == '!':
			# il faut verifier : un seul fils et c'est une regle
			assert(   arbreStrategie.getNombreDeFils() == 1   )
			fils = arbreStrategie.getFilsUnique()
			assert(fils.estUneRegle())
			 
			return self.calculArbreAppStrategie(fils)
		
		
		# --------------------------------------------------------------
		if label == '+':
			s0 = arbreStrategie.getFilsGauche()
			s1 = arbreStrategie.getFilsDroite()
			app0 = self.calculArbreAppStrategie(s0)
			app1 = self.calculArbreAppStrategie(s1)
			return  af.AFdisjonction(app0, app1)
		
		
		# --------------------------------------------------------------
		if label == ';':
			s0 = arbreStrategie.getFilsGauche()
			return self.calculArbreAppStrategie(s0)
		
		
		# --------------------------------------------------------------
		if label == '*':
			assert(   arbreStrategie.getNombreDeFils() == 1   )
			return af.arbreTrue()
		
		
		# --------------------------------------------------------------
		if label == '?':
			# il faut verifier : un seul fils et c'est une regle
			assert(   arbreStrategie.getNombreDeFils() == 1   )
			fils = arbreStrategie.getFilsUnique()
			assert(fils.estUneRegle())
			
			return af.arbreTrue()
		
		
		
		
		
		# --------------------------------------------------------------
		#     probleme .............
		# --------------------------------------------------------------
		assert(  False )

		
		
	
	
	 
  
