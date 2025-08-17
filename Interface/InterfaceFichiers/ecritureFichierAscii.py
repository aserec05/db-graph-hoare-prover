
from datasNoyau import *
from formuleLogique import *



class EcritureFichierAscii:
	
	def __init__(self, nameFile, datas):
		self.nameFile = nameFile
		self.datasNoyau = datas
		assert(isinstance(datas, DatasNoyau))
		
		self.ouverture()
		self.ecritVocabulaire()
		self.ecritFormule(  self.datasNoyau.getFormulePre(), 'formule Pre'  )
		self.ecritFormule(  self.datasNoyau.getFormulePost(), 'formule Post'  )
		self.ecritRegles()
		self.ecritStrategie()
		self.fermeture()
		 
		 
	# ****************************************************************** 
	# ****************************************************************** 
	# ****************************************************************** 
	def ouverture(self):
		self.fichier = open(self.nameFile, 'w')
	
	# ******************************************************************
	def fermeture(self):
		self.ligneVide()
		self.fichier.write('#   fin')
		self.fichier.close()
	
	# ******************************************************************
	def ligneVide(self):
		self.fichier.write('#\n')
	
	# ******************************************************************
	def ligneSperation(self):
		self.fichier.write('# ----------------------------------------------------------------------\n')
	
	# ******************************************************************
	def ligneTitre(self, titre):
		self.fichier.write('#             {} \n'.format(titre))
	
	# ******************************************************************
	def ecritTitre(self, titre):
		self.ligneVide()
		self.ligneSperation()
		self.ligneTitre(titre)
		self.ligneSperation()
		self.ligneVide()
	
	# ******************************************************************
	def ligneData(self, data):
		self.fichier.write( '{}\n'.format(data))
	
	# ******************************************************************
	def ecritVocabulaire(self):
		self.ecritTitre('predicats')
		
		v = self.datasNoyau.getVocabulaire()
		
		p1 = v.getListePredicats_1()
		chaine1 = ' , '.join(p1)
		self.ligneData(chaine1)
		
		p2 = v.getListePredicats_2()
		chaine2 = ' , '.join(p2)
		self.ligneData(chaine2)
		self.ligneVide()
	
	# ******************************************************************
	def ecritFormule(self, formule, titre =''):
		assert(isinstance(formule, FormuleLogique))
		
		if titre :
			self.ecritTitre(titre)
		 
		#~ self.fichier.write(formule.getChaineAscii() + "\n")
		self.fichier.write(formule.getChaineFichierAscii() + "\n")
	
	# ******************************************************************
	def ecritRegles(self):
		self.ecritTitre('les Regles')
		
		lesRegles = self.datasNoyau.getLesRegles()
		# iterateur à modifier ********************************************************
		nbreRegles = lesRegles.getNombreRegles()
		self.ligneData(nbreRegles)
		self.ligneVide()
		
		for nomRegle in lesRegles:
			self.ligneSperation()
			
			regle = lesRegles.getRegle(nomRegle)
			nom = regle.getLeNom()
			assert(nom == nomRegle)
			self.ligneData(nom)
			self.ligneSperation()
			
			chaine = regle.imprimeLesNoeudsFichierAscii()
			self.fichier.write(chaine)
			self.ligneSperation()
			
			chaine = regle.imprimeLesArcsFichierAscii()
			self.fichier.write(chaine)
			self.ligneSperation()
			
			chaine = regle.imprimeLesActionsFichierAscii()
			self.fichier.write(chaine)
			self.ligneSperation()
			self.ligneVide()
	
	# ******************************************************************
	def ecritStrategie(self):
		self.ecritTitre('strategie')
		
		laStrategie = self.datasNoyau.getStrategie()
		self.ligneData(laStrategie.getFormuleStrategie())
		self.ligneVide() 
		
		self.ecritTitre('invariants')
		chaine = laStrategie.imprimeLesInvariantsFichierAscii()
		self.fichier.write(chaine)
		self.ligneSperation()

# **********************************************************************
 
