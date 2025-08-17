from noeud import *
  
# **********************************************************************
# **********************************************************************

class LeftHandSide:
	
	
	def __init__(self):
		
		self.lesNoeuds = {}
		self.lesArcs = {}
	
	
	
	# ******************************************************************
	def nbreNoeud(self):
		return len(self.lesNoeuds)
	
	def nbreArcs(self):
		return len(self.lesArcs)
	
	
	# ******************************************************************
	def iterateurNoeuds(self):
		for n in  self.lesNoeuds:
			yield self.lesNoeuds[n]
	
	def iterateurArcs(self):
		for a in  self.lesArcs:
			yield self.lesArcs[a]
	
	
	# ******************************************************************
	def __str__(self):
		chaine = "[LHS]\n"
		chaine += "Les noeuds : \n"
		for n in self.lesNoeuds:
			chaine +=   str(self.lesNoeuds[n]) + "\n"
		
		chaine += "Les arcs : \n"
		for a in self.lesArcs:
			chaine += str(self.lesArcs[a]) + "\n"
		return chaine
	
	 
	
	# ******************************************************************
	def imprimeVirgule(self):
		chaine = self.imprimeLesNoeudsAvecDesVirgules()
		chaine += self.imprimeLesArcsAvecDesVirgules()
		return chaine
	
	
	# ******************************************************************
	def imprimeLesNoeudsFichierAscii(self):
		chaine = str(self.nbreNoeud()) + '\n'
		chaine += self.imprimeLesNoeudsAvecDesVirgules()
		return chaine
	
	# ******************************************************************
	def imprimeLesArcsFichierAscii(self):
		chaine = str(self.nbreArcs()) + '\n'
		chaine += self.imprimeLesArcsAvecDesVirgules()
		return chaine
		
	# ******************************************************************
	def imprimeLesNoeudsAvecDesVirgules(self):
		chaine = ""
		for n in self.iterateurNoeuds():
			chaine += n.imprimeVirgule() + "\n"
		return chaine
		
		
	def imprimeLesArcsAvecDesVirgules(self):
		chaine = ""
		for a in self.iterateurArcs():
			chaine += a.imprimeVirgule() + "\n"
		return chaine
	
	
	
	
	# ******************************************************************
	def addNoeud(self, *args):
		assert(len(args) >=2)
		
		#args au format : 'i', 'pred1', 'pred2', ...
		recu = list(args)  # args est un tuple
		 
		leNom = recu.pop(0)
			
		noeud = Noeud(leNom, *recu)
		#~ assert (variable not in self.dictionnaireNoeuds) # ------------------------- doublon, à modifier 
		self.lesNoeuds[leNom] = noeud
		return noeud
	
	
	# ******************************************************************
	def addArc(self, *args):
		assert(len(args) == 4)
		#args au format : 'i', 'pred1', 'pred2', ...
		recu2 = list(args)  # args est un tuple
		  
		leNom = recu2.pop(0)
		a = Arc(leNom,*recu2)
		self.lesArcs[leNom] = a
		
	
	
	
	# ******************************************************************
	#          exemple
	# ******************************************************************
	def unExemple(self):
		self.addNoeud('v', 'ville')
		self.addNoeud('w', 'ville')
		self.addNoeud('p', 'personne')
		self.addArc('e', 'p', 'v', 'habite')
	
	
	# ******************************************************************
	def unExemple2(self):
		 
		self.addNoeud('p', 'personne')
		self.addNoeud('q', 'personne')
		
		self.addArc('e', 'p', 'q', 'est_voisin_de')
		self.addArc('f', 'q', 'p', 'est_voisin_de')


# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************

if __name__ == '__main__':
	 
	lhs = LeftHandSide()
	lhs.unExemple()
	print(lhs)
	
	i = lhs.iterateurNoeuds()
	print(i)
	print(type(i))
	for k in i:
		print(k)
	
	i = lhs.iterateurArcs()
	print(i)
	print(type(i))
	for k in i:
		print(k)
