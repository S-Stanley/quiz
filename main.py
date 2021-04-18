from physique import Physique
from math import Math

__TOTAL__ = 3

def main():
	score = 0

	score += Physique.planetes()
	score += Math.nombre_premier_lvl_1()
	score += Math.nombre_premier_lvl_2()

	global __TOTAL__
	print(f'Final Grade : {int((score/__TOTAL__)* 20)}/20')

main()