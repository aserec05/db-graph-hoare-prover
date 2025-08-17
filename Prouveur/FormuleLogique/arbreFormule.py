import os
 

# **********************************************************************
# **********************************************************************
# ***********      classe    ArbreFormule    ***************************
# **********************************************************************
# **********************************************************************

class ArbreFormule():
	''' classe utilisée pour representer une formule de la logique du premier ordre'''
	
	dictionnaire = { 
			"EXISTENTIEL" :  chr(8707), 
			"UNIVERSEL" : chr(8704),
			"DISJONCTION" : chr(8744),
			"CONJONCTION" : chr(8743),  
			"NEGATION" : chr(172),  
			"IMPLICATION" : "=>",    
			"EQUIVALENCE" : "<=>",    
			"TRUE" : "vrai",    
			"FALSE" : "faux",   
			"PREDICAT_1" : None, 
			"PREDICAT_2" : None, 
			"VARIABLE" : None ,
			"EGAL" : None 
		}

	
	
	# ******************************************************************
	def __init__(self, letype, valeur, *args):
		''' vocabulaire issu du lexer/parser et representation textuelle '''
		
		
		self.letype = letype
		assert(letype in self.dictionnaire.keys() )
		
		self.valeur = valeur
		assert(  isinstance(valeur, str) or valeur == None)

		# verification du nombre de fils à ajouter
		self.fils = list(args)
		#~ for elt in args:
			#~ assert(  isinstance(elt, ArbreFormule) )
			 

	# ******************************************************************
	def getType(self):
		return self.letype
	
	# ******************************************************************	
	def getValeur(self):
		return self.valeur
	
	# ******************************************************************
	def getNbFils(self):
		return len(self.fils)
	
	# ******************************************************************
	def getAllFils(self):
		return self.fils
	
	# ******************************************************************	
	def getFils(self, indiceFils = 1):
		# indiceListe = indiceFils-1
		if len(self.fils)>= indiceFils:
			return self.fils[indiceFils-1]
		else :
			return None
	
	# ******************************************************************
	def createCopy(self):
		newArbre = ArbreFormule(self.getType(), self.getValeur(), *self.fils) # splat 
		return newArbre
	
	# ******************************************************************
	def __repr__(self):
		''' non récursif : uniquement la racine 
		affichage en console '''
		return "ArbreFormule : {0} - {1} - nombre de fils = {2}".format(self.letype, self.valeur,   len(self.fils))
	
	
	
	# ******************************************************************
	# ************       écriture en ligne        **********************
	# ******************************************************************
	def __str__(self):
		''' utilisé par la fonction print 
		renvoie une représentation textuelle de l'objet '''
		return self.imprimeLigne()
	
	
	# ******************************************************************
	def imprimeLigne(self):
		''' affichage en mode texte de l'arbre
		appelé par __str__
		'''
		d = self.dictionnaire 
		operateur = self.letype
		
		if operateur in ["DISJONCTION", "CONJONCTION", "IMPLICATION", "EQUIVALENCE"]:
			return "(" + self.fils[0].imprimeLigne() + ")" + d[operateur]  + "("+ self.fils[1].imprimeLigne() +")"

		elif  operateur in ["UNIVERSEL", "EXISTENTIEL"]:
			return d[operateur] + self.valeur + " " + self.fils[0].imprimeLigne()

		elif  operateur in ["TRUE", "FALSE"]:
			return d[operateur] 

		elif  operateur == "NEGATION" : 
			return d[operateur]  +" " + self.fils[0].imprimeLigne()
		
		elif  operateur == "PREDICAT_1" : 
			return self.valeur  +" (" + self.fils[0].imprimeLigne() + ")"

		elif  operateur == "PREDICAT_2" : 
			return self.valeur  +" (" + self.fils[0].imprimeLigne() +", " + self.fils[1].imprimeLigne() +  ")"
			
		elif  operateur == "EGAL" : 
			return  " (" + self.fils[0].imprimeLigne() +"=" + self.fils[1].imprimeLigne() +  ")"
		 
		elif  operateur == "VARIABLE" : 
			return self.valeur   
		 
		else : # à remplacer par une exception : ce cas ne doit pas se produire
			return self.letype
		 
	
	
	# ******************************************************************
	# ************           arbre_str()              ******************
	# ******************************************************************

	def imprimeArbre(self,  profondeur=0):
		''' renvoie une chaine de caractères
		pour affichage de l'objet ArbreFormule avec decalage selon profondeur'''
		laliste = []
		self.construitListe(laliste)
		return "\n".join(laliste)
	
	
	# ******************************************************************
	def construitListe(self,  liste,  profondeur=0):
		''' representation textuelle d'un arbre
		renvoie une liste de chaines de caractères
		
		appel recursif donc la liste est passée en parametre
		'''
		decalage = " " * profondeur * 7
		
		if self.valeur == None:
			nouvelleLigne = decalage + "{0} ".format(self.letype)
		else:
			nouvelleLigne = decalage + "{0} : {1}".format(self.letype, self.valeur)
		liste.append( nouvelleLigne)
		
		profondeur += 1
		if self.fils:
			for fils in self.fils:
				fils.construitListe( liste, profondeur)
	
	
	
	# ******************************************************************
	# ******************************************************************
	# ************             INUTILES               ******************
	# ******************************************************************
	# ******************************************************************
	
	def imprime_decalage(self,  profondeur=0):
		''' réalise l'affichage hierarchique en mode texte de l'arbre
		Equivalent à print(monArbre.arbre_str())
		donc INUTILE '''
		decalage = " "*profondeur * 7
		if self.valeur == None:
			print(decalage + "{0} ".format(self.letype))
		else:
			print(decalage + "{0} : {1}".format(self.letype, self.valeur))
		profondeur += 1
		if self.fils:
			for fils in self.fils:
				fils.imprime_decalage(profondeur)
	
	
	# ******************************************************************
	 
	def enregistre(self, filename):
		''' enregistre un arbre dans un fichier
		avec indentation pour lecture facile de la structure de l'arbre'''
		
		laliste=[]
		self.construitListe(laliste)
		
		#~ print("verif")
		#~ print(laliste)
		
		#~ os.chdir("arbres_FOL")
		#~ print(os.getcwd())
		
		lefichier  = open(filename, 'w')
		for ligne in laliste:
			lefichier.write(ligne+"\n")
		lefichier.close()
		
		#~ os.chdir("..")
	
	 


# **********************************************************************
# **********************************************************************
#                     constructeurs
# **********************************************************************
# **********************************************************************

def AFvariable(v):
	assert(isinstance(v, str))
	
	return ArbreFormule( 'VARIABLE', v)


# **********************************************************************
def AFconcept(c, variable): # predicat unaire
	assert(isinstance(c, str))
	assert(isinstance(variable, ArbreFormule))
	
	return ArbreFormule( 'PREDICAT_1', c, variable)


# **********************************************************************
def AFrole(r, variable, var2): # predicat binaire
	assert(isinstance(r, str))
	assert(isinstance(variable, ArbreFormule))
	assert(isinstance(var2, ArbreFormule))
	
	return ArbreFormule( 'PREDICAT_2', r, variable, var2)


# **********************************************************************
def AFexistentiel(variable, formule): # predicat unaire
	assert(isinstance(variable, str))
	assert(isinstance(formule, ArbreFormule))
	
	return ArbreFormule( 'EXISTENTIEL', variable, formule)


# **********************************************************************
def AFuniversel(variable, formule): # predicat unaire
	assert(isinstance(variable, str))
	assert(isinstance(formule, ArbreFormule))
	
	return ArbreFormule( 'UNIVERSEL', variable, formule)


# **********************************************************************
def AFconjonction(*arbres):
	assert(len(arbres) >= 2)
	
	#~ for arbre in arbres:
		#~ assert(isinstance(arbre, ArbreFormule))
		#~ print(type(arbre))
		#~ print(arbre)
		
	listeArbres = list(arbres)
	arbre1 = listeArbres.pop()
	arbre2 = listeArbres.pop()
	arbreConjonction = ArbreFormule( 'CONJONCTION', None, arbre1, arbre2)
	
	while listeArbres :
		arbre = listeArbres.pop()
		arbreConjonction = ArbreFormule( 'CONJONCTION', None, arbre, arbreConjonction)
	
	return arbreConjonction


# **********************************************************************
def AFdisjonction(*arbres):
	assert(len(arbres) >= 2)
	
	for arbre in arbres:
		assert(isinstance(arbre, ArbreFormule))
		
	listeArbres = list(arbres)
	arbre1 = listeArbres.pop()
	arbre2 = listeArbres.pop()
	arbreDisjonction = ArbreFormule( 'DISJONCTION', None, arbre1, arbre2)
	
	while listeArbres :
		arbre = listeArbres.pop()
		arbreConjonction = ArbreFormule( 'DISJONCTION', None, arbre, arbreDisjonction)
	
	return arbreDisjonction


# **********************************************************************
def AFnegation(arbre):
	assert(isinstance(arbre, ArbreFormule))
	
	return ArbreFormule( 'NEGATION', None, arbre)


# **********************************************************************
def AFimplication(arbre1, arbre2):
	assert(isinstance(arbre1, ArbreFormule))
	assert(isinstance(arbre2, ArbreFormule))
	
	return ArbreFormule( 'IMPLICATION', None, arbre1, arbre2)



# **********************************************************************
def AFarbreTrue( ):
	return ArbreFormule( 'TRUE', None )


# **********************************************************************
def AFarbreFalse( ):
	return ArbreFormule( 'FALSE', None )


# **********************************************************************
def AFarbreEgal(arbre1, arbre2 ):
	assert(isinstance(arbre1, ArbreFormule))
	assert(isinstance(arbre2, ArbreFormule))
	
	return ArbreFormule( 'EGAL', None, arbre1, arbre2)





