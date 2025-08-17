 

from arbreFormule import *
 
from leftHandSide import *



class CalculAppRegle:
	 
	
	# ******************************************************************
	def __init__(self, lhs):
		assert(isinstance(lhs, LeftHandSide))
		self.lhs = lhs
		 
		self.computeApp() 
		
	
	# ******************************************************************
	# ************                    API                 **************
	# ******************************************************************
	def getArbreApp(self):
		return self.arbreApp
	
	
	
	# ******************************************************************
	def computeApp(self):
		self.arbreApp = None
		# peut on avoir : lhs = None ??
		
		# **************    les noeuds      ****************************
		listeDesArbresDesNoeuds = []
		listeDesNomsDesNoeuds = []
		
		for noeud in self.lhs.iterateurNoeuds():
			#~ print("noeud : ", noeud)
			
			
			arbreNoeud = self.calculeAppNoeud(noeud) 
			assert(arbreNoeud != None)
			 
			
			# on écrit sous forme logique que les noeuds sont tous différents
			# cf contre exemple 3
			listeDesArbresNegation = []
			for oldNoeud in listeDesNomsDesNoeuds:
				egalite = AFarbreEgal(  AFvariable(oldNoeud), AFvariable(noeud.nom )   )
				negation = AFnegation(egalite) 
				listeDesArbresNegation.append(negation)
			
			listeDesNomsDesNoeuds.append(noeud.nom)
			
			if len(listeDesArbresNegation) == 1:
				arbreNoeud = AFconjonction(arbreNoeud, listeDesArbresNegation[0])
			elif len(listeDesArbresNegation) >1:
				arbreNoeud = AFconjonction(arbreNoeud, AFconjonction(*listeDesArbresNegation))
			
			listeDesArbresDesNoeuds.append(arbreNoeud) 
			
		# conjonction finale
		if len(listeDesArbresDesNoeuds) == 1:
			self.arbreApp = listeDesArbresDesNoeuds[0]
		elif len(listeDesArbresDesNoeuds) >= 1:
			self.arbreApp = AFconjonction(*listeDesArbresDesNoeuds)
		 
		
		 
		# **************        les aretes           *******************
		for arc in self.lhs.iterateurArcs():
			 
			arbreArc = self.calculeAppArc(arc) 
			
			if arbreArc != None: # revoir ce cas !!!!!!!!!!!!!!!!!
				self.arbreApp = AFconjonction(self.arbreApp, arbreArc)
		 
		
		return self.arbreApp
		
	
	
	# ******************************************************************
	#   chaque noeud produit un arbreFormule
	#*******************************************************************
	def calculeAppNoeud(self, noeud):
		# if faudra verifier qu'il existe au moins un predicat !!!! à ajouter sur la construction du graphe
		
		leNom = noeud.nom
		lesPredicatsDuNoeud = list(tuple(noeud.predicats))  # ************************************************ deep copie, à reprendre
		
		if len(lesPredicatsDuNoeud)== 0:
			return  None # cas à reprendre, controle à effectuer plus tot
		
		lesArbres = [ AFconcept(predicat,  AFvariable(leNom)  )  for predicat in lesPredicatsDuNoeud]
		if len(lesArbres)>1:
			arbreFinal = AFconjonction(*lesArbres)
		elif len(lesArbres) == 1:
			arbreFinal = lesArbres[0]
		
		return arbreFinal
	
	
	# ******************************************************************
	def calculeAppArc(self, arete):
		# if faudra verifier qu'il existe au moins un predicat !!!! à ajouter sur la construction du graphe
		 
		source = arete.source
		cible = arete.cible
		predicat = arete.role
		 
		return AFrole(  predicat,  AFvariable(source) , AFvariable(cible) )
		 
 


