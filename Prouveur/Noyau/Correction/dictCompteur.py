from arbreFormule import *


class DictCompteur:
    """
    Classe qui sert à renommer les variables lors des applications (prédicat App) des règles
    et/ou des stratégies.
    - Il compte le nomre de fois qu'une variable a pu être rennomé
    - Et renomme récursivement tous les variables d'une formule 
    sous le format "(nom de la regle)_(nom du noeud)_(nombre de fois renomé)"
    """
    
    def __init__(self,systemeReecriture) -> None:
        
        """
		Initialise à 0 les compteur des variables recencés selon les règles
		ex:
		{
			r1: {
				'x':0,
				't':0
			},
			r2: {
				'x':0
				'x':0			
			}
		}
	    """
        self.dict = {}
        for nom_regle in systemeReecriture:
            regle = systemeReecriture.getRegle(nom_regle)
            new_dict = {}
            lhs = regle.getLeftHandSide()
            for noeud in regle.getLeftHandSide().iterateurNoeuds():
                name = noeud.nom
                new_dict[name] = 0
            self.dict[nom_regle] = new_dict
		
			
    def get_new_name_from_dict(self, rule_name:str, node_name:str):
        """
		retourne le nom unique d'une nouvelle variable avec le compteur adéquat
		"""
        return f"{rule_name}_{node_name}_{self.dict[rule_name][node_name]}"
	    
    def inc_compteur(self, rule_name:str):
        """
		incrémente les compteurs des noeuds d'une règle
		"""
        for node_name in self.dict[rule_name]:
            self.dict[rule_name][node_name] += 1
    
    def rename(self, rule_name:str, formule):
        """
        Renomme récursivement toutes les variables d'une regle "rule_name" dans une formule
        """
        if formule.letype == 'VARIABLE':
            node_name = formule.getValeur()
            if node_name in self.dict[rule_name] and '~' not in node_name: # la variable est dans le lhs
                return AFvariable(self.get_new_name_from_dict(rule_name, node_name))
            return formule
        
        elif formule.letype == "PREDICAT_1":
            return AFconcept(formule.getValeur(),self.rename(rule_name, formule.getFils()))
        
        elif formule.letype == "PREDICAT_2":
            return AFrole(formule.getValeur(), self.rename(rule_name, formule.getFils()), self.rename(rule_name, formule.getFils(2)))
        
        elif formule.letype == "NEGATION":
            return AFnegation(self.rename(rule_name, formule.getFils()))
        
        elif formule.letype == "TRUE":
            return AFarbreTrue( )
        
        elif formule.letype == "FALSE":
            return AFarbreFalse( )
        
        elif formule.letype == "IMPLICATION":
            return AFimplication(self.rename(rule_name, formule.getFils()), self.rename(rule_name, formule.getFils(2)))
        
        elif formule.letype == "EGAL":
            return AFarbreEgal(self.rename(rule_name, formule.getFils()), self.rename(rule_name, formule.getFils(2)))
        
        elif formule.letype == "EXISTENTIEL":
            return AFexistentiel(formule.getValeur(), self.rename(rule_name, formule.getFils()))
        
        elif formule.letype == "UNIVERSEL":
            return AFuniversel(formule.getValeur(), self.rename(rule_name, formule.getFils()))
    
        elif formule.letype == "CONJONCTION":
            return AFconjonction(self.rename(rule_name, formule.getFils(1)), self.rename(rule_name, formule.getFils(2)))
        
        elif formule.letype == "DISJONCTION":
            return AFdisjonction(self.rename(rule_name, formule.getFils(1)), self.rename(rule_name, formule.getFils(2)))
    
    def get_exists(self, rule_name:str, formule):
        """
        Retourne la formule précédée des exists imbriqués avec les nouveaux noms de variable
        """
        f = self.rename(rule_name, formule)
        for n in self.dict[rule_name]:
            if '~' not in n:
                f = AFexistentiel(self.get_new_name_from_dict(rule_name, n), f)

        self.inc_compteur(rule_name)
        return f


    