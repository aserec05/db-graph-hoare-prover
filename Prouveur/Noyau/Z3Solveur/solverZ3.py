import z3

from leVocabulaire import *
from conversionZ3 import *
from modelAnalyseur import *


# **********************************************************************
# **********************************************************************
class SolverZ3:
	
	def __init__(self,   vocabulaireLogique, arbreFormule):
		
		assert(isinstance(vocabulaireLogique, LeVocabulaire))
		self.vocabulaireLogique = vocabulaireLogique
		
		assert(isinstance(arbreFormule, ArbreFormule))
		self.arbreFormule = arbreFormule
		 
		# declaration du type de base
		self.A = z3.DeclareSort('A') 
		
		# declaration du vocabulaire
		self.declarationDuVocabulaire()
		
		# instanciation du convertisseur de formule
		self.convertisseur = ConversionZ3(self.A, self.Z3_lesPredicats1, self.Z3_lesPredicats2)   

		self.formuleZ3 = None
		
		self.validationZ3()
	
	
	
	# ******************************************************************
	def getFormuleCompleteZ3(self):
		# renvoie un objet Z3 obtenu par conversion de l'objet ArbreFormule
		return self.formuleZ3  
	
	
	# ******************************************************************
	def getArbreFormule(self):
		# renvoie l'objet transmi lors de l'appel à SolverZ3
		return self.arbreFormule
	
	
	
	# ******************************************************************
	def reponseCourte(self): 
		"""
		Calcule le contre-exemple et renvoie le texte qui est dans le cadre réponse
		de la correction.
		"""
		if self.reponseBrute == z3.unsat:
			message = '\n[Succes] : la formule a été prouvée.\nPreuve de programme validée'
			sucess = True
		else:
			message = '\n[Echec] : la formule n\'a pas été prouvée.\nPreuve de programme non validée'
			sucess = False
			self.leSolver.set("model.compact", False)
			message += "\n\nModele (contre-exemple brute) : \n{}\n\n".format(self.leSolver.model())
			#self.leSolver.set("model.compact", True)
			
			print("ICI : ", self.leSolver.model())
		return message, sucess
	
	#***************************************************************************
	def getAnalyseur(self):
		"""
		renvoie le dictionnaire qui fait le lien entre les valeurs arbitraires et les variables
		"""
		analyseur = ModelAnalyser(self.leSolver.model(), self.vocabulaireLogique)
		analyseur.set()
		return analyseur
	
	# ******************************************************************
	# ******************************************************************
	#                privé
	# ******************************************************************
	# ******************************************************************
	def declarationDuVocabulaire(self):  
		
		# les variables sont declarées lors de la conversion des arbreFormule en formuleZ3
		
		# declaration des predicats 1
		self.lesPredicats1 = self.vocabulaireLogique.getListePredicats_1()
		self.Z3_lesPredicats1 = {}
		
		for lenom in self.lesPredicats1:
			f = z3.Function(lenom, self.A, z3.BoolSort())
			self.Z3_lesPredicats1[lenom] = f
		
		# declaration des predicats 2
		self.lesPredicats2 = self.vocabulaireLogique.getListePredicats_2()
		self.Z3_lesPredicats2 = {}
		
		for lenom in self.lesPredicats2:
			f = z3.Function(lenom, self.A, self.A, z3.BoolSort())
			self.Z3_lesPredicats2[lenom] = f
		
	 
	
	# ******************************************************************
	# ******************************************************************
	def validationZ3(self):  
		 
		self.leSolver = z3.Solver()

		# (1)   declarations des variables : effectué lors de la transformation des objets arbreFormule
		#  syntaxe : x, z, k =  z3.Consts('x z k', self.A)   
		
		# (2) l'objet de la classe ArbreFormule est converti en un objet Z3 
		self.formuleZ3 = self.convertisseur.arbre_to_z3(self.arbreFormule)
		
		#~ formuleZ3 = z3.Implies(  z3.And(preZ3, appZ3) , wpZ3) # equivalent
		self.leSolver.add(   z3.Not(self.formuleZ3)   )

		print("LLLLLLLLLLLL", z3.prove(self.formuleZ3))
		
		# (3) verification  
		self.reponseBrute = self.leSolver.check()
	
	
	
	
	
	
	# ******************************************************************
	# ******************************************************************
	def affichage(self): 
		# affichage
	 
		print("\n\n**********************************************************")
		print("les variables")
		print(self.convertisseur.lesVariables)
		
		print("\n\n**********************************************************")
		print("\n[Solveur] : ", self.leSolver)

	
		print("\nz3 analyse la négation de la formule \nReponse brute : ", self.reponseBrute)
		
		print("\n\n**********************************************************")

		#~ print("type : ", type(r))
		if self.reponseBrute == z3.unsat:
			message = '\n[Succes] : la formule a été prouvée.\nPreuve de programme validée'
			print(message)
		
		else:
			message = '\n[Echec] : la formule n\'a pas été prouvée.\nPreuve de programme non validée'
			print(message)
			print("\nModele : \n", self.leSolver.model())
		
		print("\n\n")
		#~ return message
		 
	 
 
