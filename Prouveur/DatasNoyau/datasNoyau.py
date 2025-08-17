from  leVocabulaire import *

from formuleLogique import *
from strategie import *
from systemeReecriture import *


 

class DatasNoyau:
	def __init__(self):
		
		self.vocabulaire = LeVocabulaire()
		
		self.formulePre = None
		self.formulePost = None
		
		self.lesRegles = SystemeReecriture()
		self.strategie = Strategie()
	
	
	# ********************************************************************
	def __str__(self):
		chaine = "[Vocabulaire] : \n" + str(self.vocabulaire) 
		 
		chaine +=  "\n\n[Pre] : "
		if self.formulePre :
			chaine += self.formulePre.getChaineUnicode()
			
		chaine += "\n\n[Post] : " 
		if self.formulePost :
			chaine += self.formulePost.getChaineUnicode()
		
		chaine += "\n\n[Systeme réécriture] : " + str(self.lesRegles) 
		
		chaine += "\n\n[Strategie] : " + str(self.strategie)
		return chaine
	
	
	
	# utilisé pour affichage console , ou ??????
	def imprimeFichierTexte(self):
	
		chaine = "[Vocabulaire] : \n" + str(self.vocabulaire) 
		 
		chaine +=  "\n\n[Pre] : "
		if self.formulePre :
			chaine += self.formulePre.getChaineUnicode()
			
		chaine += "\n\n[Post] : " 
		if self.formulePost :
			chaine += self.formulePost.getChaineUnicode()
		
		chaine += "\n\n[Systeme réécriture] : " + self.lesRegles.imprimeVirgule()
		chaine += "\n\n[Strategie] : " + str(self.strategie)
		return chaine
	
	
	
	# ******************************************************************
	#             un exemple
	# ******************************************************************
	def unExemple(self):
		
		self.vocabulaire.unExemple() 
		
		self.formulePre = unExempleFormuleLogique()
		self.formulePost = unExempleFormuleLogique()
		
		self.lesRegles.unExemple() 
		self.strategie.unExemple() 
		 
	
	
	
	
	
	# ******************************************************************
	#             getters
	# ******************************************************************
	def getVocabulaire(self):
		assert(isinstance(self.vocabulaire, LeVocabulaire))
		return self.vocabulaire
	
	def getFormulePre(self):
		if self.formulePre :
			assert(isinstance(self.formulePre, FormuleLogique))
		return self.formulePre
	
	def getFormulePost(self):
		if self.formulePost :
			assert(isinstance(self.formulePost, FormuleLogique))
		return self.formulePost
	
	def getLesRegles(self):
		assert(isinstance(self.lesRegles, SystemeReecriture))
		return self.lesRegles
	
	def getStrategie(self):
		assert(isinstance(self.strategie, Strategie))
		return self.strategie
	
	
	
	# ******************************************************************
	#     saisie des données
	# ******************************************************************
	# vocabulaire
	def addPredicat1(self, predicat):
		assert(isinstance(predicat, str))
		self.vocabulaire.addPredicat1(predicat)
	
	
	def addPredicat2(self, predicat):
		assert(isinstance(predicat, str))
		self.vocabulaire.addPredicat2(predicat)
	
	def remplaceVocabulaire(self, vocabulaire):
		assert(isinstance(vocabulaire, LeVocabulaire))
		self.vocabulaire = vocabulaire
	
	
	# regle
	def addRegle(self, regle):
		#~ print(type(regle)) **************************************************************
		#~ assert(isinstance(regle, Regle))
		self.lesRegles.addRegle(regle)
	 
	 
	def delRegle(self, nomRegle):
		self.lesRegles.delRegle(nomRegle)
	
	
	# strategie
	def saisieStrategie(self, chaine):
		assert(isinstance(chaine, str))
		self.strategie.saisieFormuleStrategie(chaine)
		
	def addInvariantStrategie(self, chaine):
		assert(isinstance(chaine, FormuleLogique))
		self.strategie.addInvariant(chaine)
		
	def modifieInvariantStrategie(self, indice, chaine):
		assert(isinstance(chaine, FormuleLogique))
		self.strategie.modifieInvariant(indice, chaine)
	 
	 
	# Pre  
	def addFormulePre(self, f):
		assert(isinstance(f, FormuleLogique))
		self.formulePre = f
	
	
	# Post  
	def addFormulePost(self, f):
		assert(isinstance(f, FormuleLogique))
		self.formulePost = f
	
	 
	 
