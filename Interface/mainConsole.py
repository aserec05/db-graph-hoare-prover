
 

import sys
sys.path.append('..')
sys.path.append( 'Console')
sys.path.append( 'Prouveur/Noyau')
sys.path.append( 'Prouveur/FormuleLogique')
sys.path.append( 'Prouveur/FormuleLogique/AnalyseLogique')
sys.path.append( 'Prouveur/TypesDonnees')
sys.path.append( 'Prouveur/TypesDonnees/Regles')
sys.path.append( 'Prouveur/TypesDonnees/Strategie')
sys.path.append( 'Prouveur/Correction')
sys.path.append( 'Prouveur/Z3Solveur')


from lectureFichierAscii import *
from leNoyau import *
 

 


# **********************************************************************
# **********************************************************************
# **********************************************************************

#~ nameFile = "test1"
nameFile = "test_damier"

l = LectureFichierAscii(nameFile)
datas = l.getDatasForNoyau()
print(datas)


imprimer = 0
lenoyau = LeNoyau(datas, imprimer)

f = lenoyau.getFormuleCompleteZ3() 
assert(  isinstance(f, z3.BoolRef) )

reponse = "[Formule à valider] ----------------------  \n\n    {}\n\n".format(f)
reponse += "\n[Calcul de la correction avec Z3] ---------------------- \n"
reponse += str(lenoyau.reponseCourte()) + "\n\n"

print(reponse)

nameFileReponse = "test_damier" + "_[preuve]"

fichier = open(nameFileReponse, "w")
fichier.write(str(datas))
fichier.write("\n\n\n")
fichier.write(reponse)
fichier.close()


