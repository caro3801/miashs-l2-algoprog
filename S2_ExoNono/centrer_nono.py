from robot import *

def avancer_mur():
	toucher()
	while obstacle == False:
		avancer()
		toucher()


def avancer_mur_est():
	est()
	avancer_mur()

def avancer_mur_nord():
	nord()
	avancer_mur()

def avancer_extremite_est():
	# aller au 1/2 nord
	avancer_mur_nord()
	# aller au 1/4 nord-est
	avancer_mur_est()
	# longer frontiËre nord-est vers le sud
	sud()
	toucher()
	while obstacle == faux
		avancer()
		avancer_mur_est()
		sud()
		toucher()


# programme principal
avancer_extremite_est()
ouest()
avancer()
avancer()
avancer()