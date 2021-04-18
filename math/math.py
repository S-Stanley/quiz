class Math():

	@staticmethod
	def nombre_premier_lvl_1() -> int:
		score = 0

		#ex 0
		print('Consigne: écrire sous forme de facteur premier.')
		res = input('10 = ?\n').replace(' ', '').replace('x', '*')
		if res == '2*5':
			score += 0.5
			print('Correct')
		else:
			print('Incorrect')
		
		#ex 1
		res = input('42 = ?\n').replace(' ', '').replace('x', '*')
		if res == '2*3*7' or res == '2*7*3':
			score += 0.5
		elif res == '3*2*7' or res == '3*7*2':
			score += 0.5
		elif res == '7*2*3' or res == '7*3*2':
			score += 0.5
		else:
			print('Incorrect')
		return score