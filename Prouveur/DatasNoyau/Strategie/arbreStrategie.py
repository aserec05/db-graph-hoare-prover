

class ArbreStrategie:
	
	def __init__(self, donnee = None, indice = -1, gauche = None, droite= None):
		self.label = donnee
		self.indice = indice
		self.droite = droite
		self.gauche = gauche
	
	
	
	# ------------------------------------------------------------------
	def estUneRegle(self):
		label = self.getLabel()
		return ord(label[0]) >= 97 and  ord(label[0]) <=122  #(ascii(a) = 97 et ascii(z) = 122)
	
	
	# ------------------------------------------------------------------
	def getLabel(self):
		label = self.label
		return label
	
	
	# ------------------------------------------------------------------
	def getFilsGauche(self):
		return self.gauche
	
	
	# ------------------------------------------------------------------
	def getFilsDroite(self):
		return self.droite
	
	
	# ------------------------------------------------------------------
	def getFilsUnique(self):
		assert(self.gauche and not self.droite)
		assert(   self.getNombreDeFils() == 1   )
		return self.gauche
	
	
	# ------------------------------------------------------------------
	def getNombreDeFils(self):
		nb = 0
		if self.gauche :
			nb += 1
		if self.droite:
			nb += 1
		return nb
	
	
	# ------------------------------------------------------------------
	def __str__(self):
		return 'Noeud : '+self.label
	
	
	# ------------------------------------------------------------------
	def __repr__(self):
		return 'Noeud : '+self.label
	
	


 
 
