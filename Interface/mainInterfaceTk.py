
from tkinter import *
 
import sys

sys.path.append('..')
sys.path.append( 'Interface')
sys.path.append( 'Prouveur/Noyau')
sys.path.append( 'Prouveur/FormuleLogique')
sys.path.append( 'Prouveur/FormuleLogique/AnalyseLogique')
sys.path.append( 'Prouveur/TypesDonnees')
sys.path.append( 'Prouveur/TypesDonnees/Regles')
sys.path.append( 'Prouveur/TypesDonnees/Strategie')
sys.path.append( 'Prouveur/Correction')
sys.path.append( 'Prouveur/Z3Solveur')


from interfaceTk import *
 

 


# **********************************************************************
# **********************************************************************
# **********************************************************************

fenetre = Tk()
fenetre.geometry('1400x900+100+100')

s = Interface(fenetre)

fenetre.mainloop()

