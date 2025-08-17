import ply.lex as lex
from ply.lex import TOKEN



class LexerException(Exception):
	pass



# **********************************************************************
# **********************************************************************
# **********************************************************************

class LexerLogic:
	"""
	A lexing class for parsetab.py files.
	"""
	# List of token names.   
	tokens = [ 
			'TRUE', 
			'FALSE',
			
			'EGAL',
			'LEFTPAR',
			'RIGHTPAR',
			'VIRGULE',
			'NEGATION',
			'DISJONCTION',
			'CONJONCTION',
			'IMPLICATION',
			'EQUIVALENCE',
			
			'EXISTENTIEL',
			'UNIVERSEL',
			'VARIABLE',
			'PREDICAT_1',
			'PREDICAT_2'
		]
	
	
	# Regular expression rules for simple tokens
	t_LEFTPAR = r'\('
	t_RIGHTPAR = r'\)'
	t_VIRGULE = r','
	t_TRUE = r'\[8868\]'
	t_FALSE = r'\[8869\]'
	t_EGAL = r'='
	t_NEGATION = r'\[172\]'
	t_DISJONCTION = r'\[8744\]'
	t_CONJONCTION = r'\[8743\]'
	t_IMPLICATION = r'\[8658\]'
	t_EQUIVALENCE = r'\[8660\]'
	t_EXISTENTIEL = r'\[8707\]' 
	t_UNIVERSEL = r'\[8704\]'
	 
	 
	# A string containing ignored characters (spaces and tabs)
	t_ignore  = ' \t'
	
	 
	
	
	# Error handling rule
	@staticmethod
	def t_error(t):
		print("Illegal character '%s'" % t.value[0])
		raise LexerException("Lexer : erreur de syntaxe--") 
		
		t.lexer.skip(1)
	
	  
	# Define a rule so we can track line numbers
	@staticmethod
	def t_newline(t):
		r'\n+'
		t.lexer.lineno += len(t.value)
	
	
	
	# ******************************************************************
	#                      init  
	# ******************************************************************
	def __init__(self, listeDesConcepts, listeDesRoles, imprimer= 0, **kwargs):
		
		listeDesPredicats = listeDesConcepts + listeDesRoles
		if not listeDesPredicats: # liste   vide
			raise Exception("Construction du Lexer : aucun predicat")
		
		else :
			self.listeDesConcepts = listeDesConcepts
			self.listeDesRoles = listeDesRoles
			self.imprimer = imprimer
			
			self.ajoutDesRegexDesPredicatsUnaires()
			self.ajoutDesRegexDesPredicatsBinaires()
			
			# instanciation à placer après l'ajout des méthodes !!!
			self.lexer = lex.lex(module=self, **kwargs)
	
	
	
	# ******************************************************************
	def ajoutDesRegexDesPredicatsUnaires(self):
		if self.listeDesConcepts:
			self.regexConcepts = "|".join(self.listeDesConcepts)
		else : 
			self.regexConcepts = "**************AucunPredicatUnaire**************"
		
		if self.imprimer : print("Les concepts : " + str(self.listeDesConcepts) )
	
		# ajout dynamique de regles : reconnaissance des predicats 1 du vocabulaire
		@staticmethod
		@TOKEN(self.regexConcepts)
		def t_PREDICAT_1(t):
			t.type = 'PREDICAT_1'
			return t
		
		setattr(LexerLogic, 't_PREDICAT_1', t_PREDICAT_1)
	
	
	
	# ******************************************************************
	def ajoutDesRegexDesPredicatsBinaires(self):
		if self.listeDesConcepts:
			self.regexRoles = "|".join(self.listeDesRoles)
		else : 
			self.regexRoles = "**************AucunPredicatBinaire**************"
		
		if self.imprimer : print("Les roles : " + str(self.regexRoles) )
	
		# ajout dynamique de regles : reconnaissance des predicats 2 du vocabulaire
		@staticmethod
		@TOKEN(self.regexRoles)
		def t_PREDICAT_2(t):
			t.type = 'PREDICAT_2'
			return t
		
		setattr(LexerLogic, 't_PREDICAT_2', t_PREDICAT_2)
		
		
		
	# ******************************************************************
	def ajoutDesRegexDesFonctions(self):
		pass
		'''
		# traitement des fonctions **************************************************  inutile
		chaine = "|".join(liste_fonctions)
		self.regex_fonctions = chaine
		
		if imprimer :
			print(chaine)
		
		# ajout dynamique de regles
		@staticmethod
		@TOKEN(self.regex_fonctions)
		def t_FONCTION(t):
			t.type = 'FONCTION'
			return t
		
		setattr(LexerLogic, 't_FONCTION', t_FONCTION)
		'''
	
	
	# ******************************************************************
	# à placer après les predicats, ... priorité des regex
	@staticmethod
	def t_VARIABLE(t):
		#~ r'[a-z]'
		r'[A-Za-z]+'
		t.type = 'VARIABLE'
		#~ print(t.type, t.value)
		return t
	
	 
	
	# ******************************************************************
	def tokenize(self, data, imprimer = 0):
		"""
		Tokenize input data to stdout for testing purposes.
		"""
		# data est une chaine de caractères
		self.lexer.input(data)
		
		while True:
			tok = self.lexer.token()
			if not tok:
				break
			if imprimer:
				print(tok)
	
	
	# ******************************************************************
	def tokenize_file(self, filepath):
		"""
	    Tokenize input file to stdout for testing purposes.
	    :param fspec: Input file to parse.
		"""
		with open(filepath, "r") as content:
			data = content.read()
		return self.tokenize(data)


