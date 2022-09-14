#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	power = voltage**2 / resistance
	return power

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	prod_scalaire = v1[0]*v2[0] + v1[1]*v2[1]
	'''
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	'''
	return prod_scalaire == 0

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	count = 0
	for v in values:
		count += 1 # La variable v contient une valeur de la liste.
	return sum(values) / count

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	while value != 0:
		if value >= 20:
			pass
		elif value >= 10:
			pass
		elif value >= 5:
			pass
		elif value >= 1:
			pass

	return (twenties, tens, fives, twos, ones);

def format_base(value, base, digit_letters):
	'''
	ex: value = 1337; base = 10
	value % base = 1337 % 10 = 7
	value // base = 1337 // 10 = 133
	...ect. jusqu'a 0

	'''
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		pass
	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		pass
	return result


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))
