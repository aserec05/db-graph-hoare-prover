
from datasNoyau import *
from formuleLogique import *



class LectureFichierAscii:
	
	def __init__(self, fileName):
		self.nameFile = fileName
		self.datas = DatasNoyau()
		
		self.lectureFichier()
		
		self.lectureVocabulaire()
		self.vocabulaire = self.datas.getVocabulaire()
		
		self.lecturePre()
		self.lecturePost()
		
		self.lectureRegles()
		self.lectureStrategie()
		 
	
	def getDatasForNoyau(self):
		return self.datas
	
	
	
	
	# ******************************************************************
	# *****************          prive            **********************
	# ******************************************************************
	def enleveParasites(self, mot):
		''' enleve espace et saut de ligne'''
		listeC = list(mot)
		
		caractereParasite = [' ', '\n']
		for c in caractereParasite :
			while c in listeC:
				listeC.remove(c)

		motFinal = ''.join(listeC)
		return motFinal
	
	
	# ******************************************************************
	def ligneSuivante(self):
		 
		while 1:
			self.ligneCourante = self.lesLignes.pop(0)
			if self.ligneCourante[0] == '#':
				pass
			else :
				break
	
	
	# ******************************************************************
	def lectureFormule(self):
		''' les caracteres speciaux sont codes par des entiers '''
		listeMots = self.ligneCourante.split('-')
		laliste = []
		for mot in listeMots:
			mot2 = self.enleveParasites(mot)
			
			try :
				mot2 = int(mot2)
			except Exception as e:
				pass
			laliste.append( mot2)
		 
		chaineUnicode = contruitChaineUnicodeFromListe( *laliste  )
		 
		formule  = FormuleLogique(chaineUnicode ,self.vocabulaire  )
		
		return formule
	
	 
	# ******************************************************************
	#             
	# ******************************************************************
	
	def lectureFichier(self):
		fichier = open(self.nameFile)
		self.lesLignes = fichier.readlines()
		fichier.close()
	 
	
	# ------------------------------------------------------------------
	def lectureVocabulaire(self):
		# 1)  predicats1
		self.ligneSuivante()
		listeMots = self.ligneCourante.split(',')
		for mot in listeMots:
			self.datas.addPredicat1(self.enleveParasites(mot) )
		 
		# 2)  predicats2
		self.ligneSuivante()
		listeMots = self.ligneCourante.split(',')
		for mot in listeMots:
			self.datas.addPredicat2(self.enleveParasites(mot) )
	
	
	# ------------------------------------------------------------------
	def lecturePre(self):
		# 6) pre
		self.ligneSuivante()
		formulePre = self.lectureFormule()  

		self.datas.addFormulePre( formulePre )
	
	# ------------------------------------------------------------------
	def lecturePost(self):	
		# 7) post
		self.ligneSuivante()
		formulePost  = self.lectureFormule()  

		self.datas.addFormulePost( formulePost )
		
		
	# ------------------------------------------------------------------
	def lectureRegles(self):
		# 3) systeme reecriture
		self.ligneSuivante()
		nombreRegles = int(self.ligneCourante)
		
		for i in range(nombreRegles):
			
			# lecture du nom
			self.ligneSuivante()
			nom = self.enleveParasites(self.ligneCourante)
			
			# instanciation de la nouvelle regle
			newRegle = Regle(nom)
			
			# 4a)  dictionnaire des noeuds
			self.ligneSuivante()
			nombre = int(self.ligneCourante)
			for k in range(nombre):
				self.ligneSuivante()
				listeMots = self.ligneCourante.split(',')
				listeMots = [self.enleveParasites(m) for m in listeMots]
				
				newRegle.addNoeud(*listeMots)
			
			# 4b)  dictionnaire des aretes
			self.ligneSuivante()
			nombre2 = int(self.ligneCourante)
			for k in range(nombre2):
				self.ligneSuivante()
				listeMots = self.ligneCourante.split(',')
				listeMots = [self.enleveParasites(m) for m in listeMots]
				
				newRegle.addArete(*listeMots)
		
			# 5) liste des actions 
			self.ligneSuivante()
			nombre3 = int(self.ligneCourante)
			
			for k in range(nombre3):
				self.ligneSuivante()
				listeMots = self.ligneCourante.split(',')
				listeMots = [self.enleveParasites(m) for m in listeMots]
			
				newRegle.addAction(*listeMots )
			
			# *** ajout de la regle
			self.datas.addRegle(newRegle)
		
		
		
	# ------------------------------------------------------------------
	def lectureStrategie(self):
		# 5) strategie
		self.ligneSuivante()
		chaine = self.enleveParasites(self.ligneCourante)
		
		
		self.datas.saisieStrategie(chaine)
		nbInvariants = chaine.count("*")
		#~ print(nbInvariants)
		for invariant in range(nbInvariants):
			self.ligneSuivante()
			
			formuleInvariant = self.lectureFormule() 
			self.datas.addInvariantStrategie( formuleInvariant )
		
		 



# **********************************************************************
 
