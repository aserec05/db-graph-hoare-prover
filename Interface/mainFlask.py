# -*- coding: utf-8 -*-
 


import sys

# **********************************************************************

"""
Ces paths facilitent les imports dans les modules.
Plus besoin de respecter les chemins de modules
Et pour faire : 

from nom_module import *
"""

sys.path.append('InterfaceFlask')

sys.path.append('InterfaceFichiers')


prefixe = '../Prouveur/'


sys.path.append( prefixe +'DatasNoyau')
sys.path.append( prefixe +'DatasNoyau/Regles')
sys.path.append( prefixe +'DatasNoyau/Strategie')


sys.path.append( prefixe +'FormuleLogique')
sys.path.append( prefixe +'FormuleLogique/AnalyseLogique')

sys.path.append( prefixe +'Noyau')
sys.path.append( prefixe +'Noyau/Correction')
sys.path.append( prefixe +'Noyau/Z3Solveur')

import interfaceFlask

# **********************************************************************

a = interfaceFlask.appliFlask()
a.run(debug = True)
 
