 
import sys
#~ sys.path.append('.')
#~ sys.path.append('./Objets')
sys.path.append('./Noyau')

from DatasForNoyau.datasNoyau import *

from datasFromFile import *
from leNoyau import *



class TestNoyau:
	
	def __init__(self, fileName, imprimer = 0):
		
		#~ print("*******************************\n\n\n", sys.path)
		
		# --------------------------------------------------------------
		#     recuperation des données depuis fichier
		# --------------------------------------------------------------
		dff = DatasFromFile("./[Exemples]/"+fileName)
		datas = dff.getDatasForNoyau()
		
		if imprimer :
			print("\nLes données de l'exemple : ")
			print(datas)
		 
		
		
		# **************************************************************
		# validation
		lenoyau = LeNoyau(datas, imprimer)
		
		f = lenoyau.getFormuleCompleteZ3() 
		assert(  isinstance(f, z3.BoolRef) )

		print("\n[Formule à valider] \n\n    {}\n\n".format(f) )
		
		print("\n[Reponse courte] : \n")
		print(lenoyau.reponseCourte() )
		print("\n\n \n")
	 
		# **************************************************************
		if imprimer :
			#~ triple = lenoyau.getAllFormulesZ3()  a été modifié ***************
			#~ print(type(triple))
			#~ print(triple)
			
			#~ print("\n[Pre] \n{}\n".format(triple[0]))
			#~ print("\n[App] \n{}\n".format(triple[1]))
			#~ print("\n[Wp] \n{}\n".format(triple[2]))
		
			print("\n[Etapes de calul de wp] \n")
			listeCalcul = lenoyau.getListeEtapesCalculArbreWp()
			for elt in listeCalcul:
				print(elt.construit_str() ) 
		 
	


# **********************************************************************
# **********************************************************************
# **********************************************************************
# **********************************************************************
	 
if __name__ == "__main__":
	
	if len(sys.argv)<2 :
		print("\nusage :     python testNoyauFromFile.py fileName [imprimer]\n\n")
		sys.exit()
	
	fileName = sys.argv[1]
	imprimer = 0
	
	if len(sys.argv) == 3:
		imprimer = sys.argv[2]
		 
	t = TestNoyau(fileName, imprimer)

