
import sys
sys.path.append('..')

from analyseStrategie import *
import os

import pydot


# **********************************************************************
# ****         classe    DrawArbre
# **********************************************************************

class DrawArbre:
	
	def __init__(self,  tree):
		
		self.compteur = 0
		self.graph = pydot.Dot(graph_type='digraph')
		self.construction(tree, None)
 


	# ******************************************************************
	def construction(self, tree, node_father):
		 
		chaine = tree.label
		if tree.indice>=0:
			chaine += " [{}]".format(str(tree.indice))
		new_node = self.dessine(chaine, node_father)
			
		if tree.gauche : 
			self.construction(tree.gauche, new_node)
			
		if tree.droite : 
			self.construction(tree.droite, new_node)
		
		 
	
	# ******************************************************************
	def dessine(self, chaine, node_father):
		 
		self.compteur += 1
		nouveau = pydot.Node(self.compteur,   label = chaine, style="filled", fillcolor="#aabbcc") 
		#nouveau = pydot.Node(compteur, nom = chaine, label = chaine, style="filled", fillcolor="red") 
		
		self.graph.add_node(nouveau)
		if (node_father):
			self.graph.add_edge(pydot.Edge(node_father, nouveau))
		
		return nouveau



	# ******************************************************************
	def enregistre_png(self, filename ):
		os.chdir("imagesArbres")
		#~ print(os.getcwd())
		self.graph.write_png(filename)
		os.chdir("..")









# **********************************************************************
# **********************************************************************

if __name__ == "__main__":
	
	 
	ch = '((r1!;r2?!?)*+r3?*)*;r4'
	print(ch)
	
	
	lexer = LexerStrategie(ch)
	listeLexemes = lexer.listeLex() 
	print("\n\n", listeLexemes)

	parser = ParserStrategie(listeLexemes)
	arbre = parser.getArbreStrategie()
	print(type(arbre))

	
	b = DrawArbre(arbre)
	b.enregistre_png("arbre10.png")


	 
 
