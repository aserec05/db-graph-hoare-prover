
import sys
sys.path.append('..')

from analyseStrategie import *
from dessineArbreStrategie import *
 
 


# pour un test d'affichage
# inutile
def lectureSrategie_0(self, formule):
	
	if self.donnee == ';':
		d = self.droite.lectureSrategie(formule)	
		g = self.gauche.lectureSrategie( d)
		return g
	
	elif self.donnee == '+':
		d = self.droite.lectureSrategie(formule)	
		g = self.gauche.lectureSrategie(formule)
		return g+' et '+d
	
	elif self.donnee == '*':
		return 'inv('+str(self.gauche)+')'
		
	else:
		assert(not(self.droite) and not(self.gauche))
		return 'wp('+self.donnee+','+formule+')'



# **********************************************************************
def imprimeCalculWP(racine, formuleLogique):
	''' realise un affichage ...  '''
	
	assert(isinstance(racine, ArbreStrategie))
	
	if racine.label == ';':
		d = imprimeCalculWP(racine.droite, formuleLogique)	
		g = imprimeCalculWP(racine.gauche, d)
		return g
	
	elif racine.label == '+':
		d = imprimeCalculWP(racine.droite, formuleLogique)	
		g = imprimeCalculWP(racine.gauche, formuleLogique)
		return g+'et'+d
	
	elif racine.label == '*':
		return 'inv('+str(racine.gauche)+')'
		
	else:
		assert(not(racine.droite) and not(racine.gauche))
		return 'wp(' + racine.label + ',' + formuleLogique + ')'


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
def testComplet(formuleStrategie):
	print('[formuleStrategie] \n ', formuleStrategie)

	lexer = LexerStrategie(formuleStrategie)
	listeLexemes = lexer.listeLex() 
	print('\n[listeLexemes] \n ', listeLexemes)

	parser = ParserStrategie(listeLexemes)
	arbre = parser.getArbreStrategie()
	
	print("\n[imprime] ")
	m = imprimeCalculWP(arbre, 'F')
	 
	
	print(m)



# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
ch = '((r1;r2)+r3)*;r4'
ch2 = 'r2;r3*'
testComplet(ch)
