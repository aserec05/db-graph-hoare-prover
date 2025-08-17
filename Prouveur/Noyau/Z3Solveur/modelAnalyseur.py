import z3

class ModelAnalyser:
    """
    Cette classe permet de faciliter la compréhension des contre-exemples de Z3.
    z3.model() ne permet toujours pas la bonne compréhension de ces contre exemples
    """

    
    def __init__(self, model, vocab):
        self.model = model
        self.liste_nonvariable_predicate = {} # recense pour chaque prédicat les noeuds (ou couple de noeuds) qui sont vraix ou faux
        self.arbitral_values_map = {} # lisaison entre les valeurs arbitraires données par z3 et les constantes/variables
        self.liste_else_variables_predicate = {} # les noeuds qui n'ont pas été traité par l'analyseur et se retrouve dans le 'else' du model()
        self.est_bin = {} # dit si un prédicat est binéaire
        self.vocabulaire = vocab
        self.replacement_comma = '\u060C' # virgule des couples de noeuds



    def print_assignation_arbitral_values(self) -> str:
        """
        String qui résume le dictionnaire des valeurs arbitraires
        Elle se retrouve dans le formulaire de la correction
        """

        res = "--- Assignation des variables et des valeurs --- \n"
    
        for valeur in self.arbitral_values_map:
            if "Noeud " not in self.arbitral_values_map[valeur]:
                res += self.arbitral_values_map[valeur] + " a commme valeur " + valeur + " \n"
        res += "\n"
        res += "Remarque : \n"
        res += "- Le contre exemple est un graphe G (il peut en avoir plusieur) qui ne satisfait pas la preuve ; \n" 
        res += " - les  '...' signifient tous les autres noeuds (attributs possibles et imaginables) ; \n"
        res += "- les 'Noeud i' signifient des noeuds qu'on ne connait pas le nom, mais qui suffisent à montrer que la preuve est fausse pour le graphe G ; \n"
        res += "- des éléments comme x!i ou elem!i peuvent apparaître dans les contre-exemples. Il s'agit de noeud souvent important dans le contre-exemple, mais parfois non. Ce sont des variables comme les Noeud i, cependant. "
        return res
    
    

    def string_to_dict(self, s:str, name):

        """
        Fonction utilitaire qui transforme des strings tel que "[att1 -> True, att2 -> False, else -> False] 
        en {"att1":True, "att2": False, "else":False}

        """

        # Retirer les crochets
        s = s.strip('[]')
        s = self.modify_comma(s) # différencie les virgules des listes de ceux des couples (representant les roles)
        pairs = s.split(',')
        
        
        # Initialiser le dictionnaire
        result_dict = {}
        print("Voilà les pairs", pairs)
        self.est_bin[name] = False

        for pair in pairs:
            # Diviser par '->' pour séparer la clé et la valeur
            print("une pair pour voir ! ", pair, "MAYEEEEE")
            key, value = pair.split(' -> ')

            # On elève les \n et espace
            key = self.clean_string(key)
            value = self.clean_string(value)
            
            if key not in self.arbitral_values_map:
                # on renome les A!Val!i par Noeud i, ce qui peut clarifier la compréhension de l'utilisateur.
                self.arbitral_values_map[key] = f"Noeud {key[-3:].replace('!', '').replace('l','').replace('se', '')}"

            if '(' in key:
                
                # c'est un predicat binaire ; donc un couple ; on remplace les valeur abitraires par leurs noeuds
                self.est_bin[name] = True
                tab = key.split(self.replacement_comma)
                t0 = tab[0]
                t1 = tab[1]
                for k in self.arbitral_values_map:
                    if k in tab[0]:
                        t0 = self.arbitral_values_map[k]
                    if k in tab[1]:
                        t1 = self.arbitral_values_map[k]
                    
                key = f"({t0}, {t1})"
            
            # Convertir la valeur en booléen
            if value == 'True':
                value = True
            elif value == 'False':
                value = False
            
            # Ajouter la paire clé-valeur au dictionnaire
            result_dict[key] = value

            if key != "else":
                self.liste_else_variables_predicate[name].append(key)
            else:
                self.liste_else_variables_predicate[name].append("...")
                

                
        
        return result_dict
    
    

    
    def to_dnf(self, f):


        # Simplifier l'expression
        f = z3.simplify(f)
        
        # Utiliser le Tactic pour convertir en DNF
        dnf_tactic = z3.Tactic('tseitin-cnf')
        goals = dnf_tactic(z3.Not(f))  # Utiliser Not(f) pour obtenir la DNF de f
        dnf = z3.Or([z3.simplify(g.as_expr()) for g in goals])
        
        return dnf

    def set(self) -> None:

        "Analyse du model et modification de variables qui vont être réutilisés dans l'affichage"

        for decl in self.model.decls(): # parcours des première éléments du modèle
            name = decl # nom de la variable ou de la fonction (predicat)
            value = str(self.model[name]) 
            self.liste_else_variables_predicate[name] = [] # initialisation des noeuds qui ont la même propriétés
            print(str(name), 'k!' not in str(name))
            
            if "A!val!" in value and '[' not in value and ']' not in value and "elem!" not in value and "x!" not in value: 
                # c'est une assignation d'une valeur arbitraire ; ce n'est pas un prédicat !!!
                self.arbitral_values_map[value] = str(name) # on assigne une variable à sa valeur arbitraire
            
            elif "k!" not in str(name) and "x!" not in str(name) and "And" not in value and "Or" not in value and "Not" not in value and "Var" not in value:
                # C'est un predicat binaire ou unaire simple à annaylser sans formule
                if '!' in str(name):
                    self.liste_nonvariable_predicate[name] = self.string_to_dict(value, name)
                else:
                    self.liste_nonvariable_predicate[name] = self.string_to_dict(value, name)
                if '(' not in value:
                    for i in range(len(self.liste_else_variables_predicate[name])):
                        elem = self.liste_else_variables_predicate[name][i]
                        if elem in self.arbitral_values_map:
                            self.liste_else_variables_predicate[name][i] = self.arbitral_values_map[elem]
                    self.liste_else_variables_predicate[name] = [elem for elem in list(self.arbitral_values_map.values()) if elem not in self.liste_else_variables_predicate[name]]
            

        print("WESH ALORS", self.liste_nonvariable_predicate)


    """
    ##############################################################
    ###########              PRIVE                   #############
    ##############################################################
    """
    def clean_string(self, s:str) -> str:
        """
        Enlève les \n et les espaces d'un string
        """
        return ' '.join(s.split())
    
    def modify_comma(self, s:str) -> str:
        """
        Modifie les virgules des couples, des séparateurs de liste
        Utilité : permettre une unicité de code entre concept et role en évitant les bugs 
        """
        
        compt_paranthese = 0 # compteur de paranthèsage, impair -> entre parenthèses, pair -> paranthèses fermées
        s_list = list(s)  # Convertir la chaîne en liste de caractères
    
        for i, c in enumerate(s_list):
            if c == '(' or c == ')':
                compt_paranthese += 1
            elif c == ',' and compt_paranthese % 2 != 0:  # Changer la condition pour vérifier les parenthèses ouvertes
                s_list[i] = self.replacement_comma
    
        return ''.join(s_list)  # Reconvertir la liste en chaîne de caractères


