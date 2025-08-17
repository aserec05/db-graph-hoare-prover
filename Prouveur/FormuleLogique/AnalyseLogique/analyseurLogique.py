
import sys

from leVocabulaire import *
#~ from formuleTexte import *
from arbreFormule import *

from lexerLogique import *
from parserLogique import *



class AnalyseurLogique:
	'''
	transforme une formule logique (en mode texte)
	pour obtenir une representation sous forme d'arbre 
	''' 
	
	# attention : redondant
	 
	
	# ******************************************************************
	def __init__(self, vocabulaireLogique):
		
		assert(isinstance (vocabulaireLogique, LeVocabulaire))
		self.logique = vocabulaireLogique
		
		#~ self.caracteresSpeciaux = self.logique.getListeCaracteres()
		#~ self.caracteresSpeciaux = self.caracteres
		self.lesPredicats1 = self.logique.getListePredicats_1()
		self.lesPredicats2 = self.logique.getListePredicats_2()
		
		
		# instanciation
		#~ self.lexer = LexerLogic(self.lesPredicats1, self.lesPredicats2)
		self.parser = ParserLogic(self.lesPredicats1, self.lesPredicats2)
	
	
 
	# ******************************************************************
	def analyseFormule(self, formuleAscii, imprimer = 0):
		
		assert(isinstance(formuleAscii, str) ) # ***************************************************
		
		# (1) analyse lexicale : appelée par le parseur

		# (2) analyse syntaxique
		try:
			self.formule_arbre = self.parser.parse(formuleAscii ) 
		
		except ParserException:
			print("ParserException")
			print(formuleAscii)
			print("\n\n")
			sys.exit()
			
			 
		
		# (3) retourne un objet ArbreFormule
		assert(  isinstance(self.formule_arbre, ArbreFormule) )
		return self.formule_arbre
  
   
