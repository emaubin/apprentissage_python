#!/usr/bin/env python3

# Ce programme sert à générer une liste de nucléotide aléatoire
import random

def main():
	ma_liste = []
	for i in range(10):
		ma_liste.append(random.randint(0, 3))
	print(affichage(ma_liste))

def affichage(une_liste):
	resultat = []
	for i in range(len(une_liste)):
		if (une_liste[i] == 0):
			resultat.append("A")
		elif (une_liste[i] == 1):
			resultat.append("C")
		elif (une_liste[i] == 2):
			resultat.append("G")
		elif (une_liste[i] == 3):
			resultat.append("T")
	return resultat

if __name__ == "__main__":
	main()
