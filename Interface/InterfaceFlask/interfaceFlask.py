# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

from os import listdir
from os.path import isfile, join

# **********************************************************************
from lectureFichierAscii import *
from ecritureFichierAscii import *
from formuleLogique import *
from datasNoyau import *
from leNoyau import *




# **********************************************************************
#  variables globales
datasNoyau = DatasNoyau()
reponseZ3 = ''
formuleCorrectionZ3 = ''




# **********************************************************************
def appliFlask():
	
	app = Flask(__name__)
	
	
	
	cheminVersRepertoire = '../Exemples/'
	caracteres = [172, 8743, 8744, 8868, 8869, 8707, 8704,  8660, 8658, 8868, 8869] 
	caracteres = [chr(k) for k in caracteres]
	 
	
	# **********************************************************************
	# **********************************************************************
	@app.route("/")
	def hello():
		global datasNoyau # à modifier
		return render_template("accueil.html")
	
	
	# **********************************************************************
	@app.route("/central")
	def central():
		global datasNoyau # à modifier
		return render_template("central.html", datasNoyau = datasNoyau)
	
	
	# **********************************************************************
	@app.route("/exemple_defaut")
	def exemple_defaut():
		global datasNoyau # à modifier
		datasNoyau.unExemple() # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	
		return render_template("central.html", datasNoyau = datasNoyau)
	
	
	 
	
	# **********************************************************************
	#            saisie complete
	# **********************************************************************
	@app.route('/saisie_complete')
	def saisie_complete():
		global datasNoyau # à modifier
		datasNoyau = DatasNoyau()
		return render_template("central.html", datasNoyau = datasNoyau)
	
	
	
	# **********************************************************************
	#               lecture d'un fichier 
	# **********************************************************************
	@app.route("/lire_fichier")
	def lire_fichier():
		
		repertoire = cheminVersRepertoire + '[ascii]/'
		lesFichiers = [f for f in listdir(repertoire) if isfile(join(repertoire, f))]
		nbFichiers = len(lesFichiers)
		
		return render_template("lire_fichier.html", lesFichiers = lesFichiers)
	
	
	# **********************************************************************
	@app.route("/lire_fichier_suite", methods=[ 'POST'])
	def lire_fichie_suite():
		global datasNoyau # à modifier
	
		if request.form['FileName'] :
				fileName = request.form['FileName']
				cheminComplet = cheminVersRepertoire + '[ascii]/' + fileName
				l = LectureFichierAscii(cheminComplet)
				datasNoyau = l.getDatasForNoyau()
		return render_template("central.html", datasNoyau = datasNoyau)
	
	
	# **********************************************************************
	#               enregistrer donnees dans un fichier 
	# **********************************************************************
	@app.route("/enregistrer_fichier")
	def enregistrer_fichier():
		 
		return render_template("enregistrer_fichier.html" )
	
	
	
	# **********************************************************************
	@app.route("/enregistrer_fichier_suite", methods=[ 'POST'])
	def enregistrer_fichier_suite():
		global datasNoyau # à modifier
		if request.form['nomDuFichier']:
			fileName = request.form['nomDuFichier']
			repertoire = cheminVersRepertoire + '[ascii]/'
			e = EcritureFichierAscii(repertoire + fileName, datasNoyau)
			message = 'Enregistrement terminé'
		
		else:
			message = 'Nom de fichier non valide'
		
		return render_template("validation_enregistrement_fichier.html", message = message)
	
	
	
	# **********************************************************************
	@app.route("/validation_enregistrement_fichier")
	def validation_enregistrement_fichier():
		global datasNoyau # à modifier
	
		return render_template("validation_enregistrement_fichier.html", datasNoyau = datasNoyau)
	
	
	
	# **********************************************************************
	#               enregistrer reponse dans un fichier 
	# **********************************************************************
	@app.route("/enregistrer_reponse_fichier")
	def enregistrer_reponse_fichier():
		 
		return render_template("enregistrer_reponse_fichier.html" )
	
	
	# **********************************************************************
	@app.route("/enregistrer_reponse_fichier_suite", methods=[ 'POST'])
	def enregistrer_reponse_fichier_suite():
		global datasNoyau # à modifier
		
		if request.form['nomDuFichier']:
			fileName = request.form['nomDuFichier']
		
			repertoire = cheminVersRepertoire + '[reponses]/'
			
			fichier = open(repertoire + fileName, 'w')
			
			fichier.write('Réponse donnée par Z3\n\n\n\n')
			fichier.write(reponseZ3)
			fichier.write('\n\n***************************\n\n')
			fichier.write(str(formuleCorrectionZ3))
			
			fichier.close()
			 
		
		return render_template("central.html", datasNoyau = datasNoyau)
	
	
	
	
	
	
	# **********************************************************************
	#            saisie du vocabulaire
	# **********************************************************************
	@app.route('/saisie_vocabulaire')
	def saisie_vocabulaire():
		global datasNoyau # à modifier
		
		vocabulaire = datasNoyau.getVocabulaire()
		concepts = vocabulaire.getListePredicats_1()
		concepts = '\n'.join(concepts)
		
		roles = vocabulaire.getListePredicats_2()
		roles = '\n'.join(roles)
	
		return render_template("saisie_vocabulaire.html", concepts = concepts, roles = roles)
	
	
	
	# **********************************************************************
	@app.route('/traitement_saisie_vocabulaire', methods=['POST'])
	def traitement_saisie_vocabulaire():
		global datasNoyau # à modifier
		
		lesConcepts = request.form["lesConcepts"]
		laliste = lesConcepts.split('\n')
		laliste2 = [enleveParasites(elt) for elt in laliste]
		lalisteConcepts = [elt for elt in laliste2 if len(elt)>0]
		
		lesRoles = request.form["lesRoles"]
		laliste4 = lesRoles.split('\n')
		laliste5 = [enleveParasites(elt) for elt in laliste4]
		lalisteRoles = [elt for elt in laliste5 if len(elt)>0]
		
		voca = LeVocabulaire()
		voca.initPredicat1()
		voca.addListePredicat1(lalisteConcepts)
		voca.initPredicat2()
		voca.addListePredicat2(lalisteRoles)
		datasNoyau.remplaceVocabulaire(voca) 
		
		return render_template("central.html", datasNoyau = datasNoyau)
	
	
	
	# **********************************************************************
	#            saisie d'une formule
	# **********************************************************************
	@app.route('/saisie_formule/<variable>', methods=[ 'POST'])
	def saisie_formule(variable):
		global datasNoyau # à modifier
		
		formule = request.form['formule']
		#~ formule = getattr(datasNoyau, variable) 
		#  formule = enleveParasites(formule) # si caractere espace rencontré, la formule est tronquée dans la zone de saisie
		
		#~ lesCaracteres = enumerate( caracteres)
		#~ identifiantsCaracteres = ['car'+str(k) for k in range( len(caracteres))]
		identifiantsCaracteres = [100+k for k in range( len(caracteres))]
		lesCaracteres = zip(identifiantsCaracteres, caracteres)
		
		lesConcepts = datasNoyau.getVocabulaire().getListePredicats_1()
		identifiantsConcepts = [200+k for k in range( len(lesConcepts))]
		generateurConcepts = zip(identifiantsConcepts, lesConcepts)
		
		lesRoles = datasNoyau.getVocabulaire().getListePredicats_2()
		identifiantsRoles = [300+k for k in range( len(lesRoles))]
		generateurRoles = zip(identifiantsRoles, lesRoles)
		
		return render_template("saisie_formule.html", 
								caracteres = lesCaracteres, 
								variable = variable , 
								concepts = generateurConcepts,
								roles = enumerate(datasNoyau.getVocabulaire().getListePredicats_2()),
								formule = formule, 
								datasNoyau = datasNoyau)
	
	
	
	# **********************************************************************
	@app.route('/traitement_saisie_formule/<variable>' , methods=['POST'])
	def gestion_saisie(variable):
		global datasNoyau # à modifier
		#~ setattr(datasNoyau, variable, request.form[variable])
		assert(variable in ["formulePre", "formulePost"] )
		vocabulaire = datasNoyau.getVocabulaire()
		formuleBrute = request.form["laFormule"]
		vocabulaire.addPredicat2("_____") # corrige un bug du lexer, qui veut forcément au moins un role # A MODIFIER!
		
		try :
			formule = FormuleLogique(formuleBrute, vocabulaire)
			if variable == "formulePre":
				datasNoyau.addFormulePre(formule)
			else :
				datasNoyau.addFormulePost(formule)
		
		except :
			return render_template("probleme_saisie.html", formuleBrute = formuleBrute, variable = variable)
		
		return render_template("central.html", datasNoyau = datasNoyau)
	
	
	
	# **********************************************************************
	#            saise et modification des regles
	# **********************************************************************
	@app.route('/supprime_regle/<variable>' , methods=['POST'])
	def supprime_regle(variable):
		global datasNoyau # à modifier
		
		return render_template("supprime_regle.html", nomRegle = variable, datasNoyau = datasNoyau)
	
	#***********************************************************************
	@app.route("/modifier_regle/<variable>", methods=['POST'])
	def modifier_regle(variable):
		"""
		Ajout version 3

		Lance une template pour modifier une regle. Inspiré de supprimer_regle et saisir_regle
		Fonction de route appelé à chaque bouton appuyé pour modifier une règle
		"""
		global datasNoyau # à modifier

		noeuds_string = ""
		arcs_string = ""
		actions_string = ""

		lesRegles = datasNoyau.getLesRegles()



		r = lesRegles.getRegle(variable) # acces à la regle qu'on veut modifier


		#************************************************************************
		# Modifcation du leftHandSide (noeud et arc)
		#************************************************************************
		lhs = r.getLeftHandSide() # l'ensemble de ces noeuds et de ces arc

		# l'idée est de reconstituer le input du formulaire de saisie d'une regle
		#
		# pour les noeuds dans le textearea, on fait pour chaque noeud
		# nom_noeud, predicat1, predicat2, ..., predicatn \n
		for n in lhs.iterateurNoeuds(): 
			noeuds_string += n.nom
			for c in n.predicats:
				noeuds_string += ',' + c
			noeuds_string += '\n'

		# pour le textarea des edges on fait pareil mais sous le format:
		# nom_arc, noeud_source, noeud_cible, role
		# rappel un edge n'a qu'un role
		for e in lhs.iterateurArcs():
			arcs_string += f"{e.nom},{e.source},{e.cible},{e.role}\n"

		
		#************************************************************************
		# Modifcation du rightHandSide (ACTIONS)
		#************************************************************************
		rhs = r.getRightHandSide()

		for a in rhs.laListeActions:
			actions_string = a.leNom
			for arg in a.lesArguments:
				actions_string += "," + arg
			actions_string += "\n"

		


		return render_template("modifier_regle.html", nom_regle=variable, noeuds_string=noeuds_string, arcs_string=arcs_string, actions_string=actions_string)	 


	
	
	# **********************************************************************
	@app.route('/supprime_regle_suite/<variable>' , methods=['POST'])
	def supprime_regle_suite(variable):
		global datasNoyau # à modifier
		datasNoyau.delRegle(variable)
		
		return render_template("central.html", datasNoyau = datasNoyau)	 
	
	
	
	# **********************************************************************
	@app.route('/saisie_regle', methods=['POST'])
	def saisie_regle():
		global datasNoyau # à modifier
		return render_template("modifier_regle.html", nom_regle="", noeuds_string="", arcs_string="", actions_string="")
	
	
	
	# **********************************************************************
	@app.route('/traitement_saisie_regle', methods=['POST'])
	def traitement_saisie_regle():
		global datasNoyau # à modifier
		
		leNom = request.form["nomRegle"]
		lesNoeuds = request.form["noeuds"]
		lesArcs = request.form["arcs"]
		lesActions = request.form["actions"]
		
		if not leNom :
			return render_template("saisie_regle.html")
			
			
		laRegle = Regle(leNom)
		
		
		laliste = lesNoeuds.split('\n')
		laliste2 = [enleveParasites(elt) for elt in laliste]
		laliste3 = [elt for elt in laliste2 if len(elt)>0]
		print(laliste3)
		for elt in laliste3:
			l = elt.split(',')
			laRegle.addNoeud(*l)
		
		
		laliste = lesArcs.split('\n')
		laliste2 = [enleveParasites(elt) for elt in laliste]
		laliste3 = [elt for elt in laliste2 if len(elt)>0]
		print(laliste3)
		for elt in laliste3:
			l = elt.split(',')
			laRegle.addArete(*l)
		
		
		laliste = lesActions.split('\n')
		laliste2 = [enleveParasites(elt) for elt in laliste]
		laliste3 = [elt for elt in laliste2 if len(elt)>0]
		print(laliste3)
		for elt in laliste3:
			l = elt.split(',')
			laRegle.addAction(*l)
		
		
		datasNoyau.addRegle(laRegle)
		return render_template("central.html", datasNoyau = datasNoyau)
	
	
	
	# **********************************************************************
	#            saisie de la strategie
	# **********************************************************************
	@app.route('/saisie_strategie', methods=['POST'])
	def saisie_strategie():
		global datasNoyau # à modifier
		return render_template("saisie_strategie.html",
						 		temp_strategie='',
								datasNoyau = datasNoyau)
	
	
	
	
	
	# **********************************************************************
	@app.route('/traitement_saisie_strategie' , methods=['POST'])
	def traitement_saisie_strategie():
		"""
		Route qui gère les direcctions vers les saisies d'invariant et aussi vers les traitements de strategie,
		cette template redirectionne vers le page principale après l'envoie de la stratégie
		"""
		global datasNoyau # à modifier
		formule  = request.form["formuleStrategie"] # la strategie en string
		datasNoyau.saisieStrategie(formule)
		saisieInvariant = request.form['boolLancementSaisieInvariant'] 
		
		if saisieInvariant == "FALSE": # envoie d'une strategie
			return render_template("central.html", datasNoyau = datasNoyau)
		else: # demande de saisir un invariant
			return render_template("saisie_invariant.html", 
						 		strategie = formule,
								datasNoyau = datasNoyau, 
								caracteres = enumerate(caracteres), 
								vocabulaire = datasNoyau.getVocabulaire(),
								alert=''  ,
								variable='')
	
	
	# **********************************************************************
	@app.route('/traitement_saisie_invariant' , methods=['POST'])
	def traitement_saisie_invariant():
		global datasNoyau # à modifier
		variable = request.form["formuleStrategie"] 
		formule  = request.form["invariant"]
		vocabulaire = datasNoyau.getVocabulaire()
		
		
		try : 
			# on vérfie que la strategie est bien conforme 
			invariant = FormuleLogique(formule, vocabulaire)
			datasNoyau.addInvariantStrategie(invariant)
		except : 
			# sinon on r'affiche la page de saisie avec un message d'alerte
			return render_template("saisie_invariant.html", 
						 		strategie = variable,
								datasNoyau = datasNoyau, 
								caracteres = enumerate(caracteres), 
								vocabulaire = datasNoyau.getVocabulaire(),
								alert="La saisie de l invariant n a pas été validé.",
								variable = formule)
		
		# return si tout c"est bien passé. On reviens vers la page précédente en ayant changé les données en amont dans le "try"
		return render_template("saisie_strategie.html", datasNoyau = datasNoyau, temp_strategie=variable)
	
	
	
	# **********************************************************************
	#            calcul de la correction 
	# **********************************************************************
	@app.route("/calcul_correction")
	@app.route("/calcul_correction")
	def calcul_correction():
		"""
		Template du résultat de la preuve
		Affiche tout le temps un message de résultat
		Affiche la formule à prouve
		Et aussi, en cas d'échec affiche, des contre-exemples
		"""
		global datasNoyau # à modifier
		global formuleCorrectionZ3, reponseZ3 # à modifier
		
		n = LeNoyau(datasNoyau)
		
		# formule initiale
		arbreFormule = n.getArbreFormule()
	
		# construction de la formule de correction pour affichage html
		formuleCorrectionZ3 = n.getFormuleCompleteZ3()
		formuleZ3 = str(formuleCorrectionZ3)
		formuleZ3 = formuleZ3.split('\n')
		listeFormuleHtml = []
		for elt in formuleZ3:
			compteur = 0
			while elt[compteur] == ' ':
				compteur += 1
			listeFormuleHtml.append([compteur, elt])
		
		# reponse de z3
		reponseCourteZ3 = n.reponseCourte()
		sucess = reponseCourteZ3[1]
		reponseZ3 = reponseCourteZ3[0]
		reponseHtml = reponseZ3.split('\n')

		# analyseur 
		if not sucess: 
			# la formule n'a pas été validé ; on doit trouver un contre-exemple
			analyseur = n.getAnalyseur()
			assignations = analyseur.print_assignation_arbitral_values().split('\n')
			predicats_faciles = analyseur.liste_nonvariable_predicate
			assignations_dict = analyseur.arbitral_values_map
			liste_else_variables_predicate = analyseur.liste_else_variables_predicate
			est_bin = analyseur.est_bin
		else:
			# la formule valide ; on initialise juste les variables à vide
			liste_else_variables_predicate = {}
			assignations_dict = []
			assignations = []
			predicats_faciles = {}
			est_bin = {}

		return render_template("calcul_correction.html",
							formuleCorrectionHtml = listeFormuleHtml, 
							sucess = sucess,
							liste_else_variables_predicate= liste_else_variables_predicate,
							assignations = assignations,
							predicats_faciles = predicats_faciles,
							assignations_dict = assignations_dict,
							arbreFormule = arbreFormule,
							reponse = reponseHtml,
							datasNoyau = datasNoyau,
							est_bin = est_bin)
	
	
	
	
	
	
	# ******************************************************************
	#       utilitaires
	# ******************************************************************
	
	def transformeChaine(chaine):
		''' remplace saut de ligne par <br> '''
		nouvelleChaine = ''
		for caractere in chaine :
			if ord(caractere) == 10:
				nouvelleChaine += '<br>'
			else :
				nouvelleChaine += caractere
	
	def enleveParasites(chaine):
		''' enleve espace et saut de ligne'''
		listeCaracteres = list(chaine)
		
		caractereParasite = [' ', '\n', '\r']
		for c in caractereParasite :
			while c in listeCaracteres:
				listeCaracteres.remove(c)
	
		chaineFinale = ''.join(listeCaracteres)
		return chaineFinale
	
	
	# **********************************************************************
	#         ?????????????????????????????
	# **********************************************************************
	# **********************************************************************
	@app.route('/affichage/<variable>' , methods=['POST'])
	def affichage(variable):
		if variable == 'pre':
			if request.form['pre'] :
				datasNoyau.pre = request.form['pre']
				chaine = enleveParasites(request.form['pre'])
				try:
					formuleLogique = FormuleLogique(chaine, vocabulaire)
					print(formuleLogique.getArbre()  )
					#~ a = DessineArbre(formuleLogique.getArbre() )
					#~ a.enregistre_png(".","arbre4.png")
	
				except Exception as e:
					print(e)
				
			
		elif variable == 'post':
			if request.form['post'] :
				datas.post = request.form['post']
		
		return render_template("central.html", datasNoyau = datasNoyau)
	
	
	
	
	return app
 
	
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)
