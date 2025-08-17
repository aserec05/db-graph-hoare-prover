  

from regle import *



class SystemeReecriture:
	 
	
	def __init__(self):
		
		self.lesRegles = { } # ensemble des règles sous le format nom_regle : Objet_de_la_regle
		
	def getNombreRegles(self):
		return len(self.lesRegles)
	
	
	# ******************************************************************
	def __str__(self):
		chaine = "Nombre de règle(s) = " + str(len(self.lesRegles)) +"\n"
		for r in self.lesRegles:
			chaine += str(self.lesRegles[r])
		 
		return chaine
	
	
	# ******************************************************************
	
	def __iter__(self): #ordre à verifier ****************************************************
		# dictionnaire donc retourne un iterateur sur les clés !!
		return iter(self.lesRegles)
	
	
	# ******************************************************************
	def imprimeVirgule(self):
		chaine = "Nombre de règle(s) = " + str(len(self.lesRegles)) +"\n"
		for r in self.lesRegles:
			chaine += self.lesRegles[r].imprimeVirgule()
		 
		return chaine
	
	
	
	# ******************************************************************
	def lesNomsDesregles(self):
		l = []
		for r in self.lesRegles:
			l.append(r)
		return l
	
	
	
		
	
	# ******************************************************************
	def addRegle(self, regle):
		"""
		Ajoute une regle au systeme de réécriture
		Important: si la regle existe déjà, elle est remplacée.
		"""
		assert(isinstance(regle, Regle))
		self.lesRegles[regle.nom] = regle
	
	
	# ******************************************************************
	def delRegle(self, nomRegle):
		if nomRegle in self.lesRegles:
			del   self.lesRegles[nomRegle] 
		else : 
			print("element non trouvé dans le systeme de reecriture") 
	
	
	# ******************************************************************
	def getRegle(self, nom):
		return self.lesRegles[nom] 
	
	
	
	# ******************************************************************
	def unExemple(self):
		r = Regle('r')
		r.unExemple()
		self.addRegle(r)
		
		r2 = Regle('r2')
		r2.unExemple2()
		self.addRegle(r2)
