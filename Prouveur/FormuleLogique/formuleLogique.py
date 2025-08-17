
from analyseurLogique import *

from leVocabulaire import *

from symbolesLogique import *



class FormuleLogique:
	
	

	def __init__(self, chaineUnicode, vocabulaire):
		
		assert(isinstance(vocabulaire, LeVocabulaire) )
		self.vocabulaire = vocabulaire
		
		assert(isinstance(chaineUnicode, str) )
		self.chaineUnicode = chaineUnicode
		
		self.arbreFormule = None
		
		self.calculChaineASCII()
		
		self.calculArbre()
	
	
	
	# ******************************************************************
	def calculChaineASCII(self):
		# les caracteres speciaux sont remplacés par : [identifiant Unicode] 
		# pour faciliter l'analyse lexicale : identifiant numerique = unicode (grand valeur)
		
		laListe1 =[]
		laListe2 =[]
		chaineCourante = ''
		
		for car in self.chaineUnicode :
			if car in ['\n', ' ']:
				pass
			
			elif estUnSymboleLogique(car) :
				#~ print(car)
				laListe1.append('['+str(ord(car))+']')
				
				entier = codeEntierSymbole(car)
				if chaineCourante:
					laListe2.append( chaineCourante )
					chaineCourante = ''
				laListe2.append( str(entier) )
			
			else:
				laListe1.append(car)
				chaineCourante += car
			
		if chaineCourante:
			laListe2.append( chaineCourante )
			chaineCourante = ''
		
		self.chaineASCII = ''.join(laListe1) # str
		self.chaineFichierAscii = ' - '.join(laListe2) # str
	
	
	
	# ******************************************************************
	def calculArbre(self):
		
		analyseurLogique = AnalyseurLogique(self.vocabulaire)
		
		try:
			self.arbreFormule =  analyseurLogique.analyseFormule( self.chaineASCII  )
		except Exception as e:
			print(e)
		
		assert(  isinstance( self.arbreFormule, ArbreFormule) )
	
	
	
	# ******************************************************************
	def __str__(self):
		return self.chaineUnicode + '\n'
	
	def getArbre(self):
		return self.arbreFormule
	
	def getChaineUnicode(self):
		return self.chaineUnicode
	
	def getChaineAscii(self):
		''' [8704]x (ville(x) )'''
		return self.chaineASCII
	
	def getChaineFichierAscii(self):
		'''1 - x (ville(x))'''
		return self.chaineFichierAscii
	
	  
# ********************************************************************** 
# ********************************************************************** 
# ********************************************************************** 


def contruitChaineUnicodeFromListe( *arg):
	'''
	contruitChaineUnicodeFromListe(   1, "x(personne(x)", 6, 2,  "z  (ville(z)", 4, "habite(x,Tom)))" )
	'''
	 
	chaineUnicode = ""

	for element in arg : 
		if isinstance(element, int): # un entier est transformé en caractere unicode (1 devient 'universel' ... )
			chaineUnicode += chr(unicodeSymbole(element))
		else : 
			chaineUnicode += element
	
	return chaineUnicode



def contruitChaineAsciiFromChaineUnicode( chaineUnicode):
	'''
	reprend le code de la méthode
	def calculChaineASCII(self):
	utilisé pour les tests uniquement
	'''
	# attention : doublon
	 
	laListe =[]
	
	for car in chaineUnicode :
		if car in ['\n', ' ']:
			#print("saut de ligne")
			pass
		elif estUnSymboleLogique(car)  :
			#~ print(car)
			laListe.append('['+str(ord(car))+']')
		else:
			laListe.append(car)
	
	chaine_finale = ''.join(laListe) # str
	return chaine_finale
	

def unExempleFormuleLogique():
	v = LeVocabulaire()
	v.unExemple()
	chaineUnicode =   contruitChaineUnicodeFromListe(   1, "x(personne(x)", 6, 2,  "z(ville(z)", 4, "habite(x,z)))" )
	return FormuleLogique(chaineUnicode, v)
