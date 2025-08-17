 
from regle import *
from analyseStrategie import *
from formuleLogique import *


class Strategie:
	 
	
	def __init__(self):
		self.formuleStrategie = ''
		self.arbreStrategie = None
		
		self.lesInvariants = [] # contient des objets FormuleLogique
	
	
	
	
	# ------------------------------------------------------------------
	# ------------------------------------------------------------------
	# ------------------------------------------------------------------
	def saisieFormuleStrategie(self, chaine):
		# analyse syntaxique et construction de l'arbre
		self.formuleStrategie = chaine
		
		lexer = LexerStrategie(chaine)
		self.listeLexemes = lexer.listeLex() 

		parser = ParserStrategie(self.listeLexemes)
		self.arbreStrategie = parser.getArbreStrategie()
	
	
	# ------------------------------------------------------------------
	def getLesInvariants(self):
		return self.lesInvariants
	
	# ------------------------------------------------------------------
	def getArbreStrategie(self):
		return self.arbreStrategie
	
	
	# ------------------------------------------------------------------
	def getFormuleStrategie(self):
		return self.formuleStrategie
	
	def imprimeLesInvariantsFichierAscii(self):
		chaine = ''
		for formule in self.lesInvariants:
			chaine += formule.getChaineFichierAscii() + "\n"
		return chaine
	
	# ------------------------------------------------------------------
	# ------------------------------------------------------------------
	# ------------------------------------------------------------------
	def addInvariant(self, formule):
		assert(isinstance(formule, FormuleLogique))
		self.lesInvariants.append(formule)
	
	
	# ------------------------------------------------------------------
	def modifieInvariant(self, indice, formule):
		assert(isinstance(formule, FormuleLogique))
		self.lesInvariants[indice] = formule
	
	# ------------------------------------------------------------------
	def getInvariantFromIndice(self, indice):
		return self.lesInvariants[indice] 
	
	
	# ------------------------------------------------------------------
	def imprimerInvariants(self):
		chaine = ""
		for indice, inv in enumerate(self.lesInvariants) :
			chaine += "[{}] {} \n".format(str(indice),  inv.getChaineUnicode() )
		return chaine
	
	
	
	
	# ------------------------------------------------------------------
	def __str__(self):
		#~ chaine =  self.strStrategie + "\n\nInvariants : " + "\n".join([i.getStr() for i in self.lesInvariants])
		chaine =  self.formuleStrategie + "\n\nInvariants : \n" + self.imprimerInvariants()
		#~ for indice, inv in enumerate(self.lesInvariants):
			#~ chaine += "[{ }] { }".format(indice, inv)
			#~ chaine += "["+str(indice)+"]  "  + str(inv)
		return chaine
	
	
	
	
	
	# ******************************************************************
	#          exemple
	# ******************************************************************
	def unExemple(self):
		#~ self.laListeActions.append(Action("add_C", 'variable_i', 'concept_c') )
		self.saisieFormuleStrategie("r" )
	
