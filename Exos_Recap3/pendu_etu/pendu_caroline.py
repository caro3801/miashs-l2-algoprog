#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Auteur: Caroline Desprat
Contenu: Jeu du Pendu avec dessindu pendu 
Note: Script de dessin inspiré du code de l'étudiant Baptiste Charazac
'''
from outils import *
from dessiner_pendu import *


def initGame(mot='bonjour', nb_essai=6):
    afficher('[Joueur 1] Entrez un mot : ')
    mot = lire_chaine()
    cache = str.ljust('', len(mot), '*')
    while len(mot) < 1:
        afficher_ligne('[Joueur 1] Donner un mot supérieur à 1 lettre.')
        mot = lire_chaine().lower()
    afficher("[Joueur 1] Combien d'essais voulez-vous donner (défaut:",nb_essai,") ? ")
    nb = lire_chaine()
    if nb == "":
        nb = nb_essai
    else:
        nb_essai = int(nb)
    while nb_essai < 1:
        afficher_ligne('Donner un nombre supérieur à 1.')
        nb_essai = lire_nombre()
    for i in range(25):
        afficher_ligne("")
    return (mot, cache, nb_essai)


def getLetter():
    return str.lower(lire_chaine()[0])


def get_checked_letter(liste_ok, liste_ko):
    letter = getLetter()
    while letter < 'a' or letter > 'z' or letter in liste_ok or letter \
        in liste_ko:
        afficher("[Joueur 2] Donner une lettre entre a et z non comprise dans '"
                       , liste_ok, "' ou '", liste_ko, "' : ")
        letter = getLetter()
    return letter


def count_letter_in_word(letter, word):
    return word.count(letter)


def replace_letter(letter, current_word, word):
    new_word = ''
    for i in range(len(word)):
        if word[i] == letter:
            new_word += letter
        else:
            new_word += current_word[i]
    return new_word


def ask_for_letter(liste_ok, liste_ko):
    if liste_ok == '' and liste_ko == '':
        afficher_ligne("[Aide] Aucune lettre n'a encore été jouée")
    else:
        if liste_ok != '':
            afficher_ligne('[Aide] Liste des lettres jouées gagnantes :'
                           , liste_ok)
        if liste_ko != '':
            afficher_ligne('[Aide] Liste des lettres jouées perdantes :'
                           , liste_ko)
    afficher('[Joueur 2] Entrez une lettre : ')
    return get_checked_letter(liste_ok, liste_ko)

def afficher_courant(courant, nb_essai):
    afficher_ligne('\n*********\n[Ordi] Le mot courant est', courant, '. Il vous reste ',
                   nb_essai, 'essais\n*********\n')
                   
def afficher_nb_letter(letter,nb_letter):
    if nb_letter == 0:
        afficher_ligne('[Aide] Non trouvé, la lettre', letter,
                           "n'est pas présente dans le mot secret"
                           )
    else:
        afficher_ligne('[Aide] Trouvé, la lettre', letter,
                           'est présente', nb_letter, 'fois')
                   
if __name__ == '__main__':
    dessiner = False
    (secret, courant, nb_essai) = initGame()
    if nb_essai == 6:
        dessiner = True
    afficher_courant(courant,nb_essai)
    
    if dessiner:
        pendu(nb_essai)
    perdu = False
    lettres_ok = ''
    lettres_ko = ''
    while nb_essai > 0 and courant != secret:

        j2_letter = ask_for_letter(lettres_ok, lettres_ko)
        nb_letter = count_letter_in_word(j2_letter, secret)

        if nb_letter == 0:
            lettres_ko += j2_letter
            nb_essai -= 1
            if dessiner:
                pendu(nb_essai)
            afficher_nb_letter(j2_letter,nb_letter)
            
        else:
            lettres_ok += j2_letter
            afficher_nb_letter(j2_letter,nb_letter)
            courant = replace_letter(j2_letter, courant, secret)
        afficher_courant(courant,nb_essai)

    if courant == secret:
        afficher_ligne("[Ordi] GAGNE ! Le mot courant est '", courant,
                       "'. Il vous restait ", nb_essai, "essais\n")
    if nb_essai == 0:
        afficher_ligne("[Ordi] Trop d'essais, perdu. Vous êtes pendus. Le mot secret était '"
                       , secret, "'.")
    quitter()
