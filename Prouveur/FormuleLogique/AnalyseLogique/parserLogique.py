 
import ply.yacc as yacc

from lexerLogique import LexerLogic
from arbreFormule import *



class ParserException(Exception):
	pass
	


# **********************************************************************
# **********************************************************************
# **********************************************************************

class ParserLogic:
	"""
	Parses parsetab.py files
	"""
	
	precedence = (
		('left', 'EQUIVALENCE'),    # moins prioritaire
		('right', 'IMPLICATION'),
		('left', 'DISJONCTION'),
		('left', 'CONJONCTION'),
		('left', 'NEGATION'),
		#('left', 'EXISTENTIEL'),   # ???????????????????????????????????
		#('left', 'UNIVERSEL'),     # ???????????????????????????????????
		
		)
	
	
	# ******************************************************************
	#                          __init__
	# ******************************************************************
	def __init__(self, listeDesConcepts, listeDesRoles,  the_lexer = None):
		
		if the_lexer is None:
			the_lexer = LexerLogic(listeDesConcepts, listeDesRoles)
		self._lexer = the_lexer
		
		self.tokens = self._lexer.tokens
	
		self._parser = yacc.yacc(module=self)




	# ******************************************************************
	# ******************************************************************
	#                       grammaire
	# ******************************************************************
	# ******************************************************************

	@staticmethod
	def p_racine(p): # à placer en premiere position
		'''
		racine : formule
			 | empty
		'''
		p[0] = p[1] # modifié
		

	# ******************************************************************
	#                       formules
	# ******************************************************************

	@staticmethod
	def p_formule(p):
		'''
		formule : EXISTENTIEL VARIABLE formule
				   |  UNIVERSEL VARIABLE formule
		'''
		conversion = {'[8704]' : 'UNIVERSEL', 
						'[8707]' : 'EXISTENTIEL'
							}
		
		p[0] =  ArbreFormule( conversion[p[1]],    p[2], p[3])
		
		
	@staticmethod
	def p_formule_quantificateur(p):
		'''
		formule : formule DISJONCTION formule
				   |  formule CONJONCTION formule
				   |  formule IMPLICATION formule
				   |  formule EQUIVALENCE formule
		'''
		conversion = {'[8744]' : 'DISJONCTION', 
						'[8743]' : 'CONJONCTION',
						'[8658]' : 'IMPLICATION',
						'[8660]' : 'EQUIVALENCE'
							}
		
		p[0] =  ArbreFormule(  conversion[p[2]], None,  p[1], p[3])


	@staticmethod
	def p_negation(p):
		'''
		formule : NEGATION formule
		'''
		p[0] = ArbreFormule('NEGATION', None,  p[2])


	@staticmethod
	def p_parentheses(p):
		'''
		formule : LEFTPAR formule RIGHTPAR
		'''
		p[0] =  p[2] 


	@staticmethod
	def p_formuleatomique(p):
		'''
		formule : formuleAtomique
		'''
		p[0] =   p[1]


	# ******************************************************************
	#                       formules atomiques
	# ******************************************************************

	@staticmethod
	def p_vrai_faux(p):
		'''
		formuleAtomique : TRUE
						| FALSE
		'''
		conversion = {'[8868]' : 'TRUE', 
						'[8869]' : 'FALSE'
							}
		p[0] = ArbreFormule(conversion[p[1]], 'cste_prop')
		
		 

	@staticmethod
	def p_predicat1(p):
		'''
		formuleAtomique : PREDICAT_1 LEFTPAR terme RIGHTPAR
		'''
		p[0] = ArbreFormule('PREDICAT_1', p[1],   p[3] )
		#~ p[0] = ArbreFormule('predicat1', p[1],   ArbreFormule('terme', p[3]) )
	
	
	@staticmethod
	def p_predicat2(p):
		'''
		formuleAtomique : PREDICAT_2 LEFTPAR terme VIRGULE terme RIGHTPAR
		'''
		p[0] = ArbreFormule('PREDICAT_2', p[1],    p[3],    p[5]  )
		#~ p[0] = ArbreFormule('predicat2', p[1],   ArbreFormule('terme', p[3]),   ArbreFormule('terme', p[5]))
	
	
	@staticmethod
	def p_egalite(p):
		'''
		formuleAtomique : terme EGAL terme
		'''
		p[0] = ArbreFormule('EGAL', None,    p[1],   p[3]  )
		#~ p[0] = ArbreFormule('EGAL', None,  ArbreFormule('terme',   p[1]),  ArbreFormule('terme',   p[3]))


	# ******************************************************************
	#                       termes
	# ******************************************************************

	@staticmethod
	def p_terme_variable(p):
		'''
		terme : VARIABLE
		'''
		p[0] = ArbreFormule('VARIABLE',   p[1])
		 
 
	
	
	# ******************************************************************
	#                       fin
	# ******************************************************************

	@staticmethod
	# Error rule for syntax errors
	def p_error(p):
		raise ParserException("Parser : erreur de syntaxe") 
		#~ print("Syntax error found !!")
 

	@staticmethod
	def p_empty(p):
		'''
		empty :
		'''
		p[0] = None
	

	# ******************************************************************
	# ******************************************************************
	# ******************************************************************
	def parse(self, data):
		"""
		Parses input data.
		"""
		 
		
		return self._parser.parse(data)

	
	def parse_file(self, filepath):
		"""
	    Parses data stored in file.
	    """
		with open(filepath, "r") as content:
			data = content.read()
			result = self._parser(data)
		return result
	

