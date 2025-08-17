
class Noeud:
	
	def __init__(self, nom, *args):
		self.nom = nom
		self.predicats = list(args)
		assert(len(self.predicats)>0)
	
	
	def __str__(self):
		chaine =  "[{}] ".format(self.nom)
		chaine +=  ' - '.join( self.predicats)
		return chaine
	
	
	def imprimeVirgule(self):
		liste = [self.nom] + self.predicats
		chaine =   ", ".join(liste)
		return chaine


# **********************************************************************
# **********************************************************************
class Arc:
	
	def __init__(self, nom, source, cible, role):
		self.nom = nom
		self.source = source
		self.cible = cible
		self.role = role
	
	
	def __str__(self):
		chaine = "[{}] {} - {} - {}".format(self.nom , self.source, self.cible , self.role)
		return chaine
	
	
	def imprimeVirgule(self):
		liste = [self.nom , self.source , self.cible , self.role] 
		chaine =   ", ".join(liste)
		return chaine




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
	
	n = Noeud('i', 'predicat1', 'pred2')
	print(n)
	print(n.printVirgule() )
	
	
	a = Arc('i', 'n', 'm', 'role')
	print(a)
	print(a.printVirgule() )
	


 
