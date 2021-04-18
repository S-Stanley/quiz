class Physique():

	@staticmethod
	def planetes():
		solu = ['Mercure', 'Venus', 'Terre', 'Mars', 'Jupyter', 'Saturne', 'Uranus', 'Neptune']
		rep = input('Citez les planetes dans l\'ordre, séparé par une virgule. Ex: Planete 1, Planete 2, etc..\n')
		spl = rep.split(',')
		for i in range(len(solu)):
			if solu[i].lower().replace(' ', '') != spl[i].lower().replace(' ', ''):
				print('Erreur! Vous avez dit |{}|, il fallait écrire |{}|'.format(spl[i].lower(), solu[i].lower()))
				return 0
		print('Parfait, question suivante')
		return 1