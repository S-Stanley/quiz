import random
from physique import Physique
from mathematics import Math

__TOTAL__ = 3

def main():
	score = 0
	question = []
	question.extend([ Physique.planetes, Math.nombre_premier_lvl_1, Math.nombre_premier_lvl_2])
	random.shuffle(question)
	for key in question:
		score += key()
	global __TOTAL__
	print(f'Final Grade : {int((score/__TOTAL__)* 20)}/20')

main()