#!/usr/bin/env python3

# Ce programme sert à générer une liste de nucléotide aléatoire
import random

def main():
	ma_liste = []
	for i in range(10):
		ma_liste.append(random.randint(0, 3))
	print(ma_liste)

if __name__ == "__main__":
	main()
