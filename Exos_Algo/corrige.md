#Exercice 1 : age

    Début
    Afficher ("Quel âge as-tu ? ") Lire (age)
    Si (age < 18 ) Alors
        Afficher("tu es mineur") 
    Sinon
        Afficher("tu es majeur") 
    FSi
    Fin

Demande son age à l'utilisateur et indique s'il est majeur ou mineur en fonction du nombre entré.

* Initialisation : lire(age)

* Calcul : age<18

* Affichage : "majeur", "mineur"


Jeu de données pour age : 

    12 => mineur 
    23 => majeur
    -5 => mineur

#Exercice 2 : minimum

    Début
    Ecrire ("Donner un premier nombre") 
    Lire(n1)
    Ecrire("Donner un deuxième nombre") 
    Lire(n2)
    Si (n1 < n2) Alors
        Afficher(n1) 
    Sinon
        Afficher(n2) 
    FSi
    Fin

Affiche le nombre minimum entre deux nombres saisis par l'utilisateur

* Initialisation : lire(n1), lire(n2)

* Calcul : n1<n2

* Affichage : n1, n2

Jeu de données pour {n1,n2} :
 
    {10,20} => 10
    {20,10} => 10

#Exercice 3 : somme

    Début
    somme = 0
    Pour i variant de 1 à 11 non compris faire
        Lire(n)
        somme=somme+n 
    Fpour
    Afficher(somme) 
    Fin


Affiche la somme des 10 nombres saisis par l'utilisateurs 

* Initialisation : somme = 0

* Calcul : lire(n) somme+=n

* Affichage : somme


Jeu de données : 

    * {10,5,3,5,6,5,7,8,3,10} => 62
    * {-10,-5,-3,-5,-6,-5,-7,-8,-3,-10} => -62

#Exercice 4

    Début
    Lire(a)
    Lire(n)
    resultat = 1
    Pour i variant de 1 à n non compris faire
        resultat = resultat * a 
    FPour
    Afficher(resultat) 
    Fin

Affiche le résultat de *a^n* (où *a* et *n* sont saisis par l'utilisateurs 

* Initialisation : resultat = 1 lire(a) lire(n)

* Calcul : pendant n tours : resultat *=a 

* Affichage : resultat


Jeu de données {a,n}: 
    
    {2,3} => 8
    {-5,3} => -125
    
#Exercice 5

    Début
    Afficher ("entrer un entier :") Lire (n)
    m=1
    nb = 0
    Tant que m < n faire
        Si n modulo m == 0 Alors 
            nb = nb +1
        FSi
        m = m +1; 
    FTQ
    Afficher(nb) 
    Fin
    
Affiche le nombre de facteurs d'un nombre donné par l'utilisateur


* Initialisation : resultat = 1 lire(a) lire(n)

* Calcul : pendant n tours : resultat *=a 

* Affichage : resultat

Jeu de données {a,n}: 

    12 => 2,3,4 => 3
    11 => (nombre premier) => 0

#Exercice 6

    Début
    cpt = 0
    Pour i variant de 1 à 11 non compris Faire
        lire(n)
        Si n > 100 alors
            cpt = cpt + 1 
        FSi
    Fpour 
    Afficher(cpt) 
    Fin

Affiche le nombre de nombre supérieurs à 100 donnés par l'utilisateur sur 10 saisies

    {180,105,1010,5,6,5,7,8,3,3000} => 4
    {100,5,3,5,6,5,-7,8,3,10} => 0
 
#Exercice 7

    Début
    Lire(x)
    max = x
    i = 1
    Tant que i <= 4 faire
        Lire(x)
        Si max < x alors
            max = x 
        FSi
        i = i+1 
    FTQ
    Afficher(max) 
    Fin

Affiche le nombre maximum saisi par l'utilisateur sur 5 saisies

    {5,2,7,9,-3} => 9
    {0,0,0,0,0} => 0