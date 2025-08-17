
''' gere la liste des predicats
'''
caracteres = [172, 8743, 8744, 8868, 8869, 8707, 8704,  8660, 8658, 8868, 8869] 
# 8872, 8866,
# attention, copie depuis predicats, à partager 
correspondance = { 1 : 8704, 2 : 8707, 3: 172, 4 : 8743, 5 : 8744, 6:8658, 7:8660, 8:8868, 9: 8869  }

# a reprendre
correspondanceRetour = { 8704 : 1, 8707 : 2, 172 : 3, 8743 : 4, 8744 : 5, 8658 : 6, 8660 : 7, 8868 : 8, 8869 : 9  }





def estUnSymboleLogique(car):
	return ord(car) in caracteres


def unicodeSymbole(entier):
	return correspondance[entier]

def codeEntierSymbole(car):
	return correspondanceRetour[ord(car)]


def getTupleSymboles():
	return tuple(caracteres)
