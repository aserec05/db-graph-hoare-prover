from arbreStrategie import *
 

class LexerStrategie:
	symboles = [';', '+', '(', ')', '*', '?', '!']
	
	def __init__(self, chaine):
		self.formuleStrategie = chaine
	
	
	def listeLex(self):
		# lecture de gauche à droite
		self.lexemes = []
		mot = ''
		compteurEtoile = 0
		for caractere in self.formuleStrategie :
			if caractere in self.symboles:
				if mot :
					self.lexemes.append(mot) # il faut verifier que 'mot' correspond à une regle
					mot = ''
				if caractere ==  '*':
					self.lexemes.append(('*', compteurEtoile))
					compteurEtoile += 1
				else :
					self.lexemes.append(caractere)
			else : # à proteger
				mot += caractere
		if mot:
			self.lexemes.append(mot) # il faut verifier que 'mot' correspond à une regle
		
		return self.lexemes
		

# **********************************************************************
# **********************************************************************

class ParserStrategie:
	
	def __init__(self, listeLexemes):
		
		self.listeLexemes = listeLexemes
		
	
	
	def getArbreStrategie(self):
		self.operateurs = []
		self.pile = []
		self.symboles = [';', '+']
		
		for jeton in self.listeLexemes:
			#~ print("---", jeton, self.pile, self.operateurs)
			
			if ord(jeton[0]) >= 97 and  ord(jeton[0]) <=122: # jeton est le nom d'une regle  (ascii(a) = 97 et ascii(z) = 122)
				self.pile.append(ArbreStrategie(jeton))
				continue
			
			if type(jeton) == tuple:
				assert(jeton[0] == '*')
				if self.operateurs and self.operateurs[-1] == ')':
					pass # cela n'arrive jamais car ...
				else:
					indice = jeton[1]
					fils = self.pile.pop(-1)   
					noeud = ArbreStrategie('*', indice , fils, None)
					self.pile.append(noeud)
				continue
				
			if jeton == '?':
				fils = self.pile.pop(-1)   
				noeud = ArbreStrategie('?', -1 , fils, None)
				self.pile.append(noeud)
				continue
				
			if jeton == '!':
				fils = self.pile.pop(-1)   
				noeud = ArbreStrategie('!', -1 , fils, None)
				self.pile.append(noeud)
				continue
			
			if jeton == '(':
				self.operateurs.append(jeton)
				continue
			
			if jeton ==')':
				while len(self.operateurs)>0 and self.operateurs[-1] != '(':  
					self.nouvelle_operation()
				self.operateurs.pop(-1)
				continue
				
			if jeton in self.symboles:
				if len(self.operateurs)>0 and self.operateurs[-1] != '(':  # un seul calcul
					self.nouvelle_operation()
				self.operateurs.append(jeton)
				continue
			
		while len(self.operateurs)>0 :
			self.nouvelle_operation()
			
		if len(self.pile) == 1:
			self.racine = self.pile.pop(-1)
		
		
		return self.racine
 
	
	
	def nouvelle_operation(self):
		sommet = self.operateurs.pop(-1)
		droite = self.pile.pop(-1)  # attention à l'ordre : on dépile !!!
		if sommet not in ['*', '?', '!']:
			gauche = self.pile.pop(-1)
		else :
			print('**************************  probleme  *****************')
			gauche = None
		noeud = ArbreStrategie(sommet, -1, gauche, droite)
		self.pile.append(noeud)
	




# **********************************************************************
# **********************************************************************

if __name__ == "__main__":
	
	ch = '(r1;r2)+r3*;r4'
	
	lexer = LexerStrategie(ch)
	listeLexemes = lexer.listeLex() 
	print("liste des lexemes : ")
	print(listeLexemes)
	#~ l = ['(', 'r1', ';', 'r2', ')', '+', 'r3', ';', 'r4']
	
	
	parser = ParserStrategie(listeLexemes)
	
	
	arbre = parser.getArbreStrategie()
	print(type(arbre))
	
	
	c = arbre.lectureSrategie('F')
	print(c)
 
