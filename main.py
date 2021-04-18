from physique import Physique

def main():
	score = 0
	total = 0
	score += Physique.planetes()
	total += 1
	print(f'Final Grade : {int(total/score) * 20}/20')

main()