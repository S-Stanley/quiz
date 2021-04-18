from physique import Physique
from math import Math

def main():
	score = 0
	total = 0
	
	score += Physique.planetes()
	total += 1

	score += Math.nombre_premier_lvl_1()
	total += 1

	score += Math.nombre_premier_lvl_2()
	total += 1

	print(f'Final Grade : {int(score/total) * 20}/20')

main()