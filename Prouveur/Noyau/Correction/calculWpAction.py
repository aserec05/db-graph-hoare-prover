

from calculWpActionElementaire import *

from rightHandSide import *



''' 
classe qui prend en charge le calcul de wp(action, formule) à partir de :

1) de la liste des actions elementaires (objet de la classe RighthandSide)
2) une formule logique (objet de la classe ArbreFormule)

utilise un objet de la classe ArbreTransformation
enregistre les étapes intermédiaires sous forme de liste.......
'''

class CalculateurWPAction:
	 
	
	def __init__(self,  lesActions,  arbreFormule, imprimer = 0):
		
		assert(  isinstance(lesActions, RightHandSide) )
		assert(  isinstance(arbreFormule, ArbreFormule) )

		self.arbrePostInitial = arbreFormule
		self.rightHandSide = lesActions
		self.imprimer = imprimer
 
	
	
	# ******************************************************************
	# ************            getter                      **************
	# ******************************************************************
	  
	def getListeEtapesCalculArbreWp(self):
		return self.listeEtapesCalculArbreWp
	
	
	def getArbreWp(self, k):
		# renvoie arbre_wp obtenu après k étapes de calcul
		# compteur k commence à 0 : postInitial, action1, action2, ..., action N
		try:
			return self.listeEtapesCalculArbreWp[k]
		except : # preciser exception pourindex invalide ...................................
			print("probleme d'index ...")

	
	def getStrWp(self, k):
		# renvoie chaine_wp obtenue après k étapes de calcul
		return self.getArbreWp(k).construit_str()  
	
	
	# ******************************************************************
	# ******************************************************************
	# ******************************************************************
	def calculeWP(self):
		''' effectue le calcul de wp pour l'ensemble des actions élémentaires
		 chaque étape de calcul (sous forme d'arbre) est placée dans une liste 
		 imprime pour debuggage'''
		
		
		# 1) validation de l'arbre Post 
		 
		#    *****  ajout d'un controle pour validité de post, à completer ************
		if self.arbrePostInitial in ['', ' ', None]:
			print("probleme de validité de Post")
			return 
		#~ self.arbrePostInitial = self.noyau.getArbreFormule('Post') # objet de la classe Arbre
		
		
		
		# 2) validation du dictionnaire des actions
		 
		if self.rightHandSide in [ [], None]:
			print("probleme de validité pour la liste des actions")
			return
		#~ self.listeDesActions = self.noyau.getListeActions() # objet de la classe ListeActions

		
		
		# 3) instanciation de l'objet qui effectue le calcul
		arbre_transformation = ArbreTransformation() 
		
		self.arbre_wp = self.arbrePostInitial
		self.listeEtapesCalculArbreWp = []
		self.listeEtapesCalculArbreWp.append(self.arbre_wp)
		
		# iterartion sur les actions (respecte priorité de gauche à droite)
		for action in self.rightHandSide :
			if self.imprimer:
				print("calcule_wp : action = ", action, "\n")
			
			self.arbre_wp = arbre_transformation.transformeArbre(self.arbre_wp, action)
			self.listeEtapesCalculArbreWp.append(self.arbre_wp)
			
			if self.imprimer:
				print(self.arbre_wp, "\n\n")
				self.arbre_wp.imprime_decalage()
				print("\n\n\n")
		
		
		
		# fin : à reprendre
		self.arbre_wp_final = self.arbre_wp # inutile mais ...
		
		del arbre_transformation
		
		
		# **************************************************************
		return self.arbre_wp_final 
	
	
	 






# **********************************************************************
# ****************           à reprendre           *********************
# **********************************************************************
if __name__ == '__main__':
	
	arbre_test = ArbreFormule( 'CONJONCTION', None, 
	               ArbreFormule(  'EXISTENTIEL', 'x', ArbreFormule('PREDICAT_2', 'habite', ArbreFormule('VARIABLE', 'x'), ArbreFormule('VARIABLE', 'y'))) ,
	               ArbreFormule('PREDICAT_1', 'personne',  ArbreFormule('VARIABLE', 'x')  )
	               )
	
	
	test_actions = [  Action("add_C", 'k', 'personne'), Action("add_R", 'k', 'i', 'habite')  ]
	  
	
	c = CalculWp(arbre_test, test_actions)
	
	
	for k in range(2):
		print(str(k) + " ****************")
		print(c.getStrWp(k) + "\n")
	
	for k in range(2):
		print(str(k) + " ****************")

		c.getArbreWp(k).imprime_decalage() 
		print( "\n")
