#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	power = voltage**2 / resistance
	return power

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	
	v1[0] # Pour accéder au X
	v1[1] # Pour accéder au Y
	#produit scalaire = somme de Vx * Ux + Vy * Uy + Vz * Uz ect.

	prod_scalaire = v1[0] * v2[0] + v1[1] * v2[1]
	return prod_scalaire == 0

def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	count = 0
	for v in values:
		count += 1 # La variable v contient une valeur de la liste.
	return sum(values) / count

def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = tens = fives = ones = 0
	while value != 0:
		if value >= 20:
			twenties = value // 20
			value -= twenties * 20
		elif value >= 10:
			tens = value // 10
			value -= tens * 10
		elif value >= 5:
			fives = value // 5
			value -= fives * 5
		elif value >= 1:
			ones = int(value)
			value = 0
	
	return (twenties, tens, fives, ones)

def format_base(value, base, digit_char):
	# ex: value = 1337; base = 10
	# value % base = 1337 % 10 = 7
	# value // base = 1337 // 10 = 133
	# ...ect. jusqu'a 0

	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres <
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.

	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		result += digit_char[abs_value % base]
		abs_value //= base
	if value < 0: result += "-"
	return result[::-1]


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(48879, 16, "0123456789ABCDEF"))
