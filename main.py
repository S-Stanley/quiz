import random
from physique import Physique
from mathematics import Math

__TOTAL__ = 0

def main():
	score = 0
	question = []
	question.extend([ Physique.planetes, Math.nombre_premier_lvl_1, Math.nombre_premier_lvl_2])
	random.shuffle(question)
	global __TOTAL__
	for key in question:
		score += key()
		__TOTAL__ += 1
	print(f'Final Grade : {int((score/__TOTAL__)* 20)}/20')

main()