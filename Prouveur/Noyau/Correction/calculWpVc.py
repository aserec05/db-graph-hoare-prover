
 
from arbreFormule import *

from calculWpRegle import *
from calculAppStrategie import *

from strategie import *
from dictCompteur import *


class CalculWpVc:
	
	def __init__(self, vocabulaire, systemeReecriture, strategie, arbreFormuleFin):
		self.imprimer = 0
		
		self.vocabulaire = vocabulaire
		assert(isinstance(vocabulaire, LeVocabulaire))
		
		self.systemeReecriture = systemeReecriture
		assert(isinstance(systemeReecriture, SystemeReecriture))
		
		self.strategie = strategie
		assert(isinstance(strategie, Strategie))
		
		assert(isinstance(arbreFormuleFin, ArbreFormule))
		
		arbreStrategie = strategie.getArbreStrategie()
		

		# calculs
		self.dict_compteurs = DictCompteur(self.systemeReecriture)
		

		self.arbreWP, self.arbreVC = self.computeWpVc(arbreStrategie, arbreFormuleFin)
		assert(isinstance(self.arbreWP, ArbreFormule))
		assert(isinstance(self.arbreVC, ArbreFormule))
	
	 
	# ******************************************************************
	def getArbreWP(self):
		return self.arbreWP
	 
	def getArbreVC(self):
		return self.arbreVC
		  
	@staticmethod
	def getVarApp(regle, formule):
		"""
		Rajoute des existences de chaque noeuds du lhs devant la formule rentrée en parametre
		"""
		assert(isinstance(formule, ArbreFormule))
		assert(isinstance(regle, Regle))

		op_const = '~'

		for noeud in regle.getLeftHandSide().iterateurNoeuds():
			name = noeud.nom
			if op_const not in name:
				formule = AFexistentiel(name, formule)
		return formule
 
	# ******************************************************************
	# ******************************************************************

	
	def computeWpVc(self, arbreStrategie , formuleArbre):
		"""
		Calcule et renvoie en (0) wp(arbreStrategie, formuleArbre) 
		et en (1) vc(arbreStrategie, formuleArbre)
		"""
	
		assert(isinstance(arbreStrategie, ArbreStrategie))
		assert(isinstance(formuleArbre, ArbreFormule))
		
		label = arbreStrategie.getLabel()
		
		# --------------------------------------------------------------
		if arbreStrategie.estUneRegle():  # c'est une regle
			assert(   arbreStrategie.getNombreDeFils() == 0   )
			
			# recuperer la regle à partir de son nom
			regle = self.systemeReecriture.getRegle(label)
			
			# calcul de wp(r, Q)
			cwp = CalculateurWPRegle(regle, formuleArbre)
			arbreWP =  cwp.getArbreWP()
			arbreVC =  AFarbreTrue()
			 
			#~ print("regle : arbreWP : ", arbreWP)
			#~ print("regle : arbreVC : ", arbreVC)
			return self.dict_compteurs.get_exists(label, arbreWP), arbreVC
		
		
		
		
		# --------------------------------------------------------------
		# --------------------------------------------------------------
		#           SINON
		# --------------------------------------------------------------
		# --------------------------------------------------------------
		
		
		# --------------------------------------------------------------
		if label == '?':
			# il faut verifier : un seul fils et c'est une regle
			assert(   arbreStrategie.getNombreDeFils() == 1   )
			fils = arbreStrategie.getFilsUnique()
			assert(fils.estUneRegle())
			
			# recuperer la regle à partir de son nom
			label2 = fils.getLabel()
			regle = self.systemeReecriture.getRegle(label2)
			
			# calcul de wp(r, Q)
			cwp = CalculateurWPRegle(regle, formuleArbre)
			arbreWPpositif =  cwp.getArbreWP()
			arbreVC =  AFarbreTrue()
			appRegle = cwp.getAppRegle()
			arbreWPnegatif = AFimplication(AFnegation(appRegle), formuleArbre)
			
			arbreWPcomplet = AFconjonction(arbreWPpositif, arbreWPnegatif)
			
			return self.dict_compteurs.get_exists(label2, arbreWPcomplet), arbreVC
			
		
		# --------------------------------------------------------------
		if label == '!':
			# il faut verifier : un seul fils et c'est une regle
			assert(   arbreStrategie.getNombreDeFils() == 1   )
			fils = arbreStrategie.getFilsUnique()
			assert(fils.estUneRegle())
			 
			return self.computeWpVc(fils, formuleArbre)
		
		
		# --------------------------------------------------------------
		if label == ';':
			s0 = arbreStrategie.getFilsGauche()
			s1 = arbreStrategie.getFilsDroite()
			formuleWPDroite , formuleVCDroite = self.computeWpVc(s1, formuleArbre) # s1 ----  calcul de droite à gauche
			formuleWPGauche , formuleVCGauche = self.computeWpVc(s0, formuleWPDroite) # s0
			return formuleWPGauche,  AFconjonction(formuleVCGauche, formuleVCDroite)
		
		
		# --------------------------------------------------------------
		if label == '+':
			s0 = arbreStrategie.getFilsGauche()
			s1 = arbreStrategie.getFilsDroite()
			formuleWPDroite , formuleVCDroite = self.computeWpVc(s1, formuleArbre)
			formuleWPGauche , formuleVCGauche = self.computeWpVc(s0, formuleArbre)
			return AFconjonction(formuleWPGauche, formuleWPDroite),  AFconjonction(formuleVCGauche, formuleVCDroite)
		
		
		# --------------------------------------------------------------
		if label == '*':
			assert(   arbreStrategie.getNombreDeFils() == 1   )
			
			filsDeLEtoile = arbreStrategie.getFilsUnique()
			assert(isinstance(filsDeLEtoile, ArbreStrategie) )
			
			# recherche de l'invariant associé à la regle etoile
			indiceInvariant = arbreStrategie.indice
			invariant = self.strategie.getInvariantFromIndice(indiceInvariant) 
			assert(isinstance(invariant, FormuleLogique))
			invs = invariant.getArbre()
			assert(  isinstance( invs, ArbreFormule) )
			
			
			# calcul de wp(s, invs) et vc(s, invs)
			arbreWpFilsEtoile ,arbreVcFilsEtoile = self.computeWpVc(filsDeLEtoile, invs)
			#~ print("arbreWpFilsEtoile : ", arbreWpFilsEtoile)
			#~ print("formuleVcFilsEtoile : ", arbreVcFilsEtoile)
			assert(isinstance(arbreWpFilsEtoile, ArbreFormule))
			assert(isinstance(arbreVcFilsEtoile, ArbreFormule))
			
			
			# calcul de app(filsDeLEtoile)
			calculateur = CalculAppStrategie(filsDeLEtoile, self.systemeReecriture)
			app = calculateur.getArbreApp() 

			lesReglesApp = calculateur.getReglesApp()

			
			
			# construction de vc(s*, Q)
			arbre1 = AFimplication( AFconjonction(invs, app),   arbreWpFilsEtoile  )
			arbre2 = AFimplication( AFconjonction(invs,   AFnegation(app) ),  formuleArbre )
			arbreVC = AFconjonction( arbreVcFilsEtoile, arbre1, arbre2)
			
			
			# conclusion
			arbreWP = invs

			for r in lesReglesApp:
				arbreVC = self.dict_compteurs.get_exists(r.getLeNom(), arbreVC)
			return arbreWP, arbreVC
		
		
		# --------------------------------------------------------------
		#     probleme .............
		# --------------------------------------------------------------
		assert(  False )


