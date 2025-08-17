
from action import *   
from arbreFormule import *
#~ from arbreTransformation import *




# rappel : decorateur ancien (voir ancienne version)


# decorateur 
def parcours_arbre(func):
		 
		def nouveau(self, arbreFormule, *args):
			
			# 1) transformation des fils
			les_nouveaux_fils = []
			if arbreFormule: # differnet de None -----------------------------  à revoir 
				for fils in arbreFormule.getAllFils() : # les feuilles n'ont pas de fils donc pas d'appel récursif !!! cas de base inutile
					les_nouveaux_fils.append( nouveau(self, fils, *args )  )
				
			# 2) construction d'un nouvel arbre avec les nouveaux fils
			newArbre = ArbreFormule(arbreFormule.getType(),  arbreFormule.getValeur(),  *les_nouveaux_fils) # attention ! splat etoile !!!!!
			
			# 3) traitement de la racine
			return  func(self, newArbre, *args)
			
		return nouveau


# **********************************************************************
# **********************************************************************
# ***********      classe    ARBRE TRANSFORMATION         **************
# **********************************************************************
# **********************************************************************

class ArbreTransformation():
	''' classe utilisée pour le calcul de wp
	weakest precondition '''
	
	def __init__(self):
		self.arbreFormule = None
	
	
	 
	# ******************************************************************
	# seule méthode publique
	# ******************************************************************
	def transformeArbre(self, arbreFormule, action):
		
		assert(  isinstance(arbreFormule, ArbreFormule) )
		assert(  isinstance(action, Action) )
		
		
		operation = action.getLeNom()
		#~ print(operation)
		
		
		if operation == 'add_N': # add Node
			pass
		
		elif operation == 'del_N': # delete Node
			pass
		
		if operation == 'add_C': # add Concept
			# attention à l'ordre des parametres
			newArbre = self.addConcept(arbreFormule, action.leNoeud, action.leConcept  )
		
		elif operation == 'del_C': # delete Concept
			# attention à l'ordre des parametres
			newArbre = self.delConcept(arbreFormule, action.leNoeud, action.leConcept  )
		
		elif operation == 'add_E': # add Edge
			# attention à l'ordre des parametres
			newArbre = self.addEdge(arbreFormule,  action.laSource, action.laCible, action.leRole )
		
		elif operation == 'del_E':
			# attention à l'ordre des parametres
			newArbre = self.delEdge(arbreFormule,  action.laSource, action.laCible, action.leRole )
		
		elif operation == 'redirection':
			# attention à l'ordre des parametres
			newArbre = self.redirection(arbreFormule,  action.noeudOne, action.noeudTwo )
		
		elif operation == 'merge':
			# attention à l'ordre des parametres
			# conservation du noeud 1 avec l'ensemble des labels
			newArbre = self.merge(arbreFormule, action.noeudOne, action.noeudTwo)
		
		else: # à reprendre
			raise Exception
		
		return newArbre
	
	
	
	
	# ****************************************************************** 
	# ****************************************************************** 
	
	
	# ****************************************************************** 
	#       add Concept   (predicat 1)
	# ****************************************************************** 
	@parcours_arbre
	def addConcept(self, arbreFormule, noeud_i, nomPredicat):
		# il faut ???    distinguer variables libres, liées et constantes ????????????????????????????????????????????????????
		
	 	
		if arbreFormule.getType() == 'PREDICAT_1' and arbreFormule.getValeur() == nomPredicat :  # on a trouvé 'C(x)'
			 
			noeud_x = arbreFormule.getFils().getValeur()
			
			fils1 = arbreFormule.createCopy()
			fils2 = AFarbreEgal( AFvariable(noeud_x), AFvariable(noeud_i) ) # x=i
			
			return AFdisjonction(fils1, fils2) # 'C(x) ou (x=i)'
			
			
		else : 
			return arbreFormule  # ce n'est pas une copie !!!!! ????????????????????????????????????????????????????????????????????????
			#~ return ArbreFormule(arbreFormule.letype, arbreFormule.valeur,  arbreFormule.fils) # copie !!!!!
	
	
	# ******************************************************************
	#       del Concept   (predicat 1)
	# ****************************************************************** 
	@parcours_arbre
	def delConcept(self, arbreFormule, variable, predicat):

		if arbreFormule.getType() == 'PREDICAT_1' and arbreFormule.getValeur()  == predicat :
			noeud_x = arbreFormule.fils[0].valeur
			
			fils1 = arbreFormule.createCopy()

			petit_fils2 = ArbreFormule('EGAL', None, ArbreFormule('VARIABLE',noeud_x), ArbreFormule('VARIABLE', variable) )

			fils2 = ArbreFormule('NEGATION', None, petit_fils2 )

			return ArbreFormule('CONJONCTION', None, fils1, fils2)
		
		
		else : 
			return arbreFormule   
			
			
	
	# ******************************************************************
	#       add Edge  (et role = predicat 2)
	# ******************************************************************
	@parcours_arbre
	def addEdge(self, arbreFormule,   source, cible, predicat):

		if arbreFormule.getType() == 'PREDICAT_2' and arbreFormule.getValeur() == predicat :
			fils1 = arbreFormule.createCopy() # creation d'une copie
			
			v1 = arbreFormule.getFils(1).getValeur()
			v2 = arbreFormule.getFils(2).getValeur()
			
			 
			pf1 = AFarbreEgal( AFvariable(v1), AFvariable( source) )
			pf2 = AFarbreEgal( AFvariable(v2),AFvariable( cible) )
			fils2 = AFconjonction( pf1, pf2)
			
			final = AFdisjonction(fils1, fils2)
			#~ print(arbreFormule)
			#~ print(final)
			return final
		else : 
			return arbreFormule
	
	
	
	# ******************************************************************
	#       del Edge  (et role = predicat 2)
	# ******************************************************************
	@parcours_arbre
	def delEdge(self, arbreFormule,   variable1, variable2, predicat):
		 
		if arbreFormule.getType() == 'PREDICAT_2' and arbreFormule.getValeur() == predicat :
			fils1 = arbreFormule.createCopy() # creation d'une copie
			
			v1 = arbreFormule.getFils(1).getValeur()
			v2 = arbreFormule.getFils(2).getValeur()
			pf1 = ArbreFormule('NEGATION', None, ArbreFormule('EGAL', None, ArbreFormule('VARIABLE',v1), ArbreFormule('VARIABLE', variable1) ))
			pf2 = ArbreFormule('NEGATION', None, ArbreFormule('EGAL', None, ArbreFormule('VARIABLE',v2), ArbreFormule('VARIABLE', variable2) ) )
			fils2 = ArbreFormule('DISJONCTION', None, pf1, pf2)
			
			return ArbreFormule('CONJONCTION', None, fils1, fils2)
		
		else : 
			return arbreFormule
	
	
	
	
	# ******************************************************************
	#           FUSION 
	#        noeud1 conservé, 
	#        noeud2 absorbé par noeud1
	# ******************************************************************
	@parcours_arbre
	def merge(self, arbreFormule,   noeud_i, noeud_j):
		
		if arbreFormule.getType() == 'PREDICAT_1'   :
			nomDuPredicat = arbreFormule.valeur
			
			# arbreFormule.getFils() est un noeud de type VARIABLE : toujours ???????  pourrait être un terme ???? pas dans cette logique !!!!!
			noeud_x = arbreFormule.getFils().getValeur()  # nom de la variable, i.e  'x' pour 'C(x)'
			
			
			petit_fils1 = ArbreFormule('EGAL', None, ArbreFormule('VARIABLE', noeud_x), ArbreFormule('VARIABLE', noeud_j) )
			fils1 = ArbreFormule('NEGATION', None, petit_fils1 )


			#~ copieInitial = ArbreFormule('PREDICAT_1', nomDuPredicat,  *arbreFormule.fils) # creation d'une copie : C(x)
			copieInitial = arbreFormule.createCopy()
			
			
			fils_2_2_1 = ArbreFormule('EGAL', None, ArbreFormule('VARIABLE', noeud_x), ArbreFormule('VARIABLE', noeud_i) )  # x=i
			fils_2_2_2 = ArbreFormule('PREDICAT_1' , nomDuPredicat, ArbreFormule('VARIABLE', noeud_j)  )  # C(j)
			
			petit_fils2_2 = ArbreFormule('CONJONCTION', None,  fils_2_2_1, fils_2_2_2 ) # x=i et C(j)
			
			fils2 = ArbreFormule('DISJONCTION', None,  copieInitial, petit_fils2_2 ) #   C(x) ou ( x=i et C(j) )

			return ArbreFormule('CONJONCTION', None, fils1, fils2)
			
			
			
		elif arbreFormule.getType()  == 'PREDICAT_2'  :
			 
			nomDuPredicat = arbreFormule.getValeur()
			noeud_x = arbreFormule.getFils(1).getValeur()  # nom de la variable, i.e  'x' pour 'R(x,y)'
			noeud_y = arbreFormule.getFils(2).getValeur()  # nom de la variable, i.e  'y' pour 'R(x,y)'
			
			a11 =  ArbreFormule('NEGATION', None,  ArbreFormule('EGAL', None, ArbreFormule('VARIABLE', noeud_x), ArbreFormule('VARIABLE', noeud_j) ) )
			a12 =  ArbreFormule('NEGATION', None,  ArbreFormule('EGAL', None, ArbreFormule('VARIABLE', noeud_y), ArbreFormule('VARIABLE', noeud_j) ) )
			a1 = ArbreFormule('CONJONCTION', None, a11, a12)
			
			# ****************
			a211 =  ArbreFormule('PREDICAT_2' , nomDuPredicat, ArbreFormule('VARIABLE', noeud_x) ,ArbreFormule('VARIABLE', noeud_y) )
			
			a2121 =  ArbreFormule('PREDICAT_2' , nomDuPredicat, ArbreFormule('VARIABLE', noeud_x) ,ArbreFormule('VARIABLE', noeud_j) )
			a2122 =  ArbreFormule('EGAL' , None, ArbreFormule('VARIABLE', noeud_y) ,ArbreFormule('VARIABLE', noeud_i) )
			a212 = ArbreFormule('CONJONCTION', None, a2121,  a2122)
			
			a21 = ArbreFormule('DISJONCTION', None, a211,  a212)
			
			
			a2211 =  ArbreFormule('PREDICAT_2' , nomDuPredicat, ArbreFormule('VARIABLE', noeud_j) ,ArbreFormule('VARIABLE', noeud_y) )
			a2212 =  ArbreFormule('EGAL' , None, ArbreFormule('VARIABLE', noeud_x) ,ArbreFormule('VARIABLE', noeud_i) )
			a221 = ArbreFormule('CONJONCTION', None, a2211,  a2212)
			
			
			a22211 = ArbreFormule('EGAL' , None, ArbreFormule('VARIABLE', noeud_x) ,ArbreFormule('VARIABLE', noeud_i) )
			a22212 = ArbreFormule('EGAL' , None, ArbreFormule('VARIABLE', noeud_y) ,ArbreFormule('VARIABLE', noeud_i) )
			a2221 = ArbreFormule('CONJONCTION', None, a22211,  a22212)
			
			a2222 =  ArbreFormule('PREDICAT_2' , nomDuPredicat, ArbreFormule('VARIABLE', noeud_j) ,ArbreFormule('VARIABLE', noeud_j) )
			a222 = ArbreFormule('CONJONCTION', None, a2221,  a2222)
			
			a22 = ArbreFormule('DISJONCTION', None, a221,  a222)
			a2 = ArbreFormule('DISJONCTION', None, a21,  a22)
			# ********************
			return ArbreFormule('CONJONCTION', None, a1, a2)
		
		else : 
			return arbreFormule
	
	
	# ******************************************************************
	#           REDIRECTION
	#   aretes entrantes du noeud1 sont deplacées vers noeud 2
	# ******************************************************************
	@parcours_arbre
	def redirection(self, arbreFormule,  old_target, new_target):
		
		if arbreFormule.getType() == 'PREDICAT_2'  :
			v1 = arbreFormule.getFils(1).getValeur()
			v2 = arbreFormule.getFils(2).getValeur()
			
			pfils1 = ArbreFormule(arbreFormule.letype, arbreFormule.valeur,  *arbreFormule.fils) # creation d'une copie
			pfils2 = ArbreFormule('NEGATION', None, ArbreFormule('EGAL', None, ArbreFormule('VARIABLE',v2), ArbreFormule('VARIABLE', old_target) ))
			fils1 = ArbreFormule('CONJONCTION', None, pfils1, pfils2)
			
			pfils3 = ArbreFormule(arbreFormule.letype, arbreFormule.valeur,  ArbreFormule('VARIABLE',v1), ArbreFormule('VARIABLE', old_target))
			pfils4 = ArbreFormule('EGAL', None, ArbreFormule('VARIABLE',v2), ArbreFormule('VARIABLE', new_target) ) 
			fils2 = ArbreFormule('CONJONCTION', None, pfils3, pfils4)
			
			return ArbreFormule('DISJONCTION', None, fils1, fils2)
		
		else : 
			return arbreFormule
	
	 
	
	# ****************************************************************** 
	# ****************************************************************** 
	# ****************************************************************** 
	# ****************************************************************** 
	'''
	# ****************************************************************** 
	# **************           sans decorateur                ********** 
	# ****************************************************************** 
	 
	def add_predicat_1(self, arbreFormule, predicat, variable):
		 
		
		# 1) transformation des fils
		les_nouveaux_fils = []
		for fils in arbreFormule.fils: # les feuilles n'ont pas de fils donc pas d'appel récursif !!! cas de base inutile
			les_nouveaux_fils.append(  self.action_1(fils, predicat, variable) )
			
		# 2) construction d'un nouvel arbre avec les nouveaux fils
		newArbre = ArbreFormule(arbreFormule.letype, arbreFormule.valeur,  *les_nouveaux_fils) # attention ! splat etoile !!!!!
		
		# 3) traitement de la racine
		return  self.action_1(newArbre, predicat, variable)
		
		
	# ****************************************************************** 
	
	def action_1(self, arbreFormule, predicat, variable):
		# il faut distinguer variables libres, liées et constantes ********************************
		
		if arbreFormule.letype == 'PREDICAT_1' and arbreFormule.valeur == predicat :
			#~ print("match ! : ", arbreFormule.valeur)
			# il faut chercher la variable
			v = arbreFormule.fils[0].valeur
			
			fils1 = ArbreFormule(arbreFormule.letype, arbreFormule.valeur,  *arbreFormule.fils) # attention ! splat etoile !!!!!
			
			fils2 = ArbreFormule('EGAL', None, ArbreFormule('VARIABLE',v), ArbreFormule('VARIABLE', variable) )

			return ArbreFormule('DISJONCTION', None, fils1, fils2)
			
			
		else : 
			return arbreFormule  # copie !!!!! ????????????????????????????????????????????????????????????????????????
			#~ return ArbreFormule(arbreFormule.letype, arbreFormule.valeur,  arbreFormule.fils) # copie !!!!!
	
	# ******************************************************************
	# ******************************************************************
	# ******************************************************************
	'''
	
	
	 


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
	 
	arbre_test = ArbreFormule( 'CONJONCTION', None, 
	               ArbreFormule(  'EXISTENTIEL', 'x', ArbreFormule('PREDICAT_2', 'mange', ArbreFormule('VARIABLE', 'x'), ArbreFormule('VARIABLE', 'y'))) ,
	               ArbreFormule('PREDICAT_1', 'dort',  ArbreFormule('VARIABLE', 'x')  )
	               )
	
	arbre_test2 = ArbreFormule( 'NEGATION', None, arbre_test) 
	
	
	
	print("\n\n *****************  avant *************************** \n")
	print(arbre_test)
	arbre_test.imprime_decalage()


	# transformation
	transformation_test = ArbreTransformation()
	
	action3= Action("add_R", 'i', 'j', 'cherche')
	action6= Action("add_R", 'i', 'j', 'mange')
	action4= Action("add_C", 'k',  'marche')
	action5= Action("add_C", 'k',  'dort')
	action1= Action("del_R", 'i', 'j', 'mange')
	action2= Action("del_C", 'i', 'dort')
	 
	arbre2 = transformation_test.transformeArbre(arbre_test, action5)
	arbre2 = transformation_test.transformeArbre(arbre2, action6)
	arbre2 = transformation_test.transformeArbre(arbre2, action2)
	
	print("\n\n *****************  apres *************************** \n")
	arbre2.imprime_decalage()
	print(arbre2)
	 
