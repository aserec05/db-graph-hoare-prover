import z3
from arbreFormule import *


# **********************************************************************
# **********************************************************************

class ConversionZ3:
	''' permet de convertir un objet de la classe ArbreFormule 
	en un objet Z3'''
	def __init__(self, type_A, predicats1_z3, predicats2_z3):
		self.lesVariables = {}
		self.lesConstantes = {}
		
		# dictionnaires
		self.lesPredicats_1 = predicats1_z3
		self.lesPredicats_2 = predicats2_z3
		
		#~ self.A = z3.DeclareSort('A')
		self.A = type_A
		 
	
	
	
	# ******************************************************************
	# ******************************************************************
	def arbre_to_z3(self, arbre):
		
		assert(isinstance(arbre, ArbreFormule))
		
		
		
		if arbre.letype == 'EXISTENTIEL':
			nomDeLaVariable = arbre.valeur
			variableX = self.traitementVariable(nomDeLaVariable)
			laFormule = arbre.fils[0]
			formuleZ3 = z3.Exists(variableX, self.arbre_to_z3(laFormule) )
			return formuleZ3
		
		
		elif arbre.letype == 'UNIVERSEL':
			variableX = self.traitementVariable(arbre.valeur)
			return z3.ForAll(variableX, self.arbre_to_z3(arbre.fils[0]) )
		
		
		elif arbre.letype == 'DISJONCTION':
			#~ return z3.Or(self.arbre_to_z3(arbre.fils[0]), self.arbre_to_z3(arbre.fils[1]) )
			a = self.arbre_to_z3(arbre.fils[0])
			b = self.arbre_to_z3(arbre.fils[1])
			return z3.Or(self.arbre_to_z3(arbre.fils[0]), self.arbre_to_z3(arbre.fils[1]) )
		
		
		elif arbre.letype == 'CONJONCTION':
			return z3.And(self.arbre_to_z3(arbre.fils[0]), self.arbre_to_z3(arbre.fils[1]) )
		
		
		elif arbre.letype == 'IMPLICATION':
			return z3.Implies(self.arbre_to_z3(arbre.fils[0]), self.arbre_to_z3(arbre.fils[1]) )
		
		
		elif arbre.letype == 'EQUIVALENCE':
			return  self.arbre_to_z3(arbre.fils[0]) == self.arbre_to_z3(arbre.fils[1]) 
		
		
		elif arbre.letype == 'NEGATION':
			return z3.Not( self.arbre_to_z3(arbre.fils[0]) ) 
		
		
		elif arbre.letype == 'TRUE':
			return True
		
		
		elif arbre.letype == 'FALSE':
			return False
		
		
		elif arbre.letype == 'VARIABLE':
			return self.traitementVariable(arbre.valeur)
		
		
		# predicats
		elif arbre.letype == 'PREDICAT_1':
			predicatNow = self.traitementPredicat_1(arbre.valeur) # objet z3 ...
			return  predicatNow (self.arbre_to_z3(arbre.fils[0]) )  # objet de type formule de z3 ...
		
		
		elif arbre.letype == 'PREDICAT_2':
			predicatNow = self.traitementPredicat_2(arbre.valeur)
			f =  predicatNow (self.arbre_to_z3(arbre.fils[0]), self.arbre_to_z3(arbre.fils[1]))
			return f
		
		
		elif arbre.letype == 'EGAL':
			f =   self.arbre_to_z3(arbre.fils[0])   ==   self.arbre_to_z3(arbre.fils[1])
			return f
		
		
		else:
			print("vide")
			return None
	
	
	
	
	
	
	# ******************************************************************
	# ******************************************************************

	def traitementVariable(self, nomDeLaVariable):

		nomDeLaVariable = nomDeLaVariable.replace('~', '')
			
		if nomDeLaVariable in self.lesVariables :
			#~ print("ancienne variable")
			variableX = self.lesVariables[nomDeLaVariable]
		
		else : 
			#~ print("nouvelle variable")
			variableX = z3.Const(nomDeLaVariable, self.A)
			self.lesVariables[nomDeLaVariable] = variableX
		
		return variableX
	 
	
	
	# ******************************************************************
	def traitementPredicat_1(self, nomDuPredicat):
		
		if nomDuPredicat in self.lesPredicats_1 :
			predicatNow = self.lesPredicats_1[nomDuPredicat] # objet de type fonction de z3 ...
		
		else : 
			print("[conversion_z3.py/traitementPredicat_1()] : ", nomDuPredicat)
			raise Exception # *************************************************
		
		return predicatNow
	
	
	
	# ******************************************************************
	def traitementPredicat_2(self, nomDuPredicat):
		
		if nomDuPredicat in self.lesPredicats_2 :
			#~ print("ancien predicat")
			predicatNow = self.lesPredicats_2[nomDuPredicat]
		
		else : 
			raise Exception # *************************************************
		
		return predicatNow
		
