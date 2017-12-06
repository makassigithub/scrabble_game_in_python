"""
Projet:    TP3 IFT-1004
Session:   Automne 2017
Équipe 90: Miguel Castelo
           Brahima Traore
"""
from random import shuffle
from tkinter import *

class Joueur:
    """
    Cette classe permet de représenter un joueur.

    La classe joueur possède une variable de classe:
    - TAILLE_CHEVALET : le nombre de jetons maximum qu'un joueur peut avoir.

    Un joueur a 3 attributs:
    - nom (str, public): représente le nom du joueur doit être non vide.
    - __points (entier, privé): représente le nombre de points que le joueur détient.
    - __chevalet (list, privé): représente le chevalet (l'ensemble des jetons du joueur) du joueur.
            Cette liste devrait être en tout temps de taille Joueur.TAILLE_CHEVALET. À chaque position du chevalier on peut avoir un jeton ou pas.
            Une position libre devra contenir None. Autrement elle devrait avoir un objet Jeton à cette position.
    """
    TAILLE_CHEVALET = 7

    def __init__(self, nom):
        """
        Initialise un objet joueur avec le nom passé en argument.
        Le nombre de points d'un joueur devra être 0 à l'initialisation, et le chevalet devra être vide.
        Rappel: Un chevalet vide veut dire une liste contenant que des None.
        :param nom: Le nom du joueur.
        :return: Ne retourne rien.
        :exception: Levez une exception si le nom est une chaine vide.
        """
        # À compléter
        # Mettre votre code ici

        # Valider que le nom n'est pas une chaine vide
        assert (not nom.isspace()) and (len(nom) > 0), "Le nom ne doit pas être vide"

        # Initialisation des variables d'instance de la classe
        self.nom = nom
        self.__points = 0
        self.__chevalet = [None] * Joueur.TAILLE_CHEVALET
        root = Tk()
        self.__chevalet = Canvas(root, width=300, height=80, bg="grey").grid(column=0, row=0)
        root.mainloop()

        # canvas = Canvas(Tk(), width=chevalet_width, height=chevalet_height)
        # canvas.pack()
        # jetons_initiaux = [None] * Joueur.TAILLE_CHEVALET
        # taille_chevalet = len(jetons_initiaux)
        #
        # etape_x = int(chevalet_width/taille_chevalet)
        # for i in range(0, taille_chevalet):
        #     canvas.create_bitmap((i + 1) * etape_x - etape_x / 2, 50, bitmap=jetons_initiaux[i])
        # self.__chevalet = canvas

    @property
    def nb_a_tirer(self):
        """
        Méthode permet de trouver le nombre de places vides dans le chevalet.
        Rappel: Un chevalet vide veut dire une liste contenant que des None.
        :return: (int) Le nombre de places vides dans le chevalet.
        """
        # À compléter
        # Mettre votre code ici

        # Retourner le nombre de places vides dans le chevalet
        return self.__chevalet.count(None)

    @property
    def points(self):
        """
        Méthode permettant d'obtenir le nombre de points du joueur.
        :return: (int) Le nombre de points du joueur.
        """
        # À compléter
        # Mettre votre code ici

        # Retourner le nombre de points du joueur
        return self.__points

    @staticmethod
    def position_est_valide(pos):
        """
        Méthode permettant de vérifier si une position sur un chevalet est valide ou pas.
        Valide veut dire que la position est entre 0 et Joueur.TAILLE_CHEVALET (Joueur.TAILLE_CHEVALET étant exclus)
        :param pos: (int) la position à valider
        :return: True si position valide, False sinon
        """
        # À compléter
        # Mettre votre code ici

        # Retourner True si position entre 0 et Joueur.TAILLE_CHEVALET, sinon False
        return 0 <= pos < Joueur.TAILLE_CHEVALET

    def position_est_vide(self, pos):
        """
        Étant donnée une position sur le chevalet, cette méthode permet de voir
        si la position est vide ou pas.
        Rappel: Une position vide ne contient pas de jeton, juste None.
        :param pos: (int) position à vérifier.
        :return: True si la position est vide et False sinon.
        :exception: Levez une exception avec assert si la position n'est pas valide. Pensez à réutiliser Joueur.position_est_valide.
        """
        # À compléter
        # Mettre votre code ici

        # Vérifier que la position est valide
        assert Joueur.position_est_valide(pos), "La position n'est pas valide"

        # Retourner True si la position est vide, sinon False
        return self.__chevalet[pos] is None

    def ajouter_jeton(self, jeton, pos=None):
        """
        Étant donnés un jeton et une position sur le chevalet, cette méthode permet d'ajouter le jeton
        au chevalet si la position mentionnée est vide.
        Si la position est vide (i.e. pos est égal à None), le jeton est mis à la première position libre du chevalet en partant de la gauche.
        Rappel: Une position vide ne contient pas de jeton, juste None.
        :param jeton: (Jeton) Jeton à placer sur le chevalet.
        :param pos: (int, optionnel) Position où ajouter le jeton.
        :return: Ne retourne rien.
        :exception: Levez une exception avec assert si la position est spécifiée mais n'est pas valide ou si elle n'est pas vide pour y déposer un jeton. Pensez à réutiliser Joueur.position_est_valide et position_est_vide.
        """
        # À compléter
        # Mettre votre code ici

        # Rajouter le jeton à la première position libre lorsque la position n'est pas spécifiée.
        if pos is None:
            self.__chevalet[self.__chevalet.index(None)] = jeton
            return

        # Vérifier que la position est valide et est vide.
        assert Joueur.position_est_valide(pos) and self.position_est_vide(pos), "La position n'est pas valide ou n'est pas vide"

        # Rajouter le jeton à la position spécifiée.
        self.__chevalet[pos] = jeton

    def retirer_jeton(self, pos):
        """
        Cette méthode permet de retirer un jeton du chevalet: c'est comme simuler un joueur qui prend un jeton de son chevalet. Donc retirer veut dire mettre la position à None et retourner le jeton qui était présent à cet emplacement.
        :param pos: Position du jeton à retirer.
        :return: Le jeton retiré.
        :exception: Levez une exception avec assert si la position spécifiée n'est pas valide ou si elle est vide. Pensez à réutiliser Joueur.position_est_valide et position_est_vide.
        """
        # À compléter
        # Mettre votre code ici

        # Vérifier que la position est valide et n'est pas vide.
        assert Joueur.position_est_valide(pos) and not self.position_est_vide(pos), "La position n'est pas valide ou elle est vide"

        # Assigner le jeton à retirer à une variable temporaire.
        jeton_retire = self.__chevalet[pos]

        # Retirer le jeton du chevalet.
        self.__chevalet[pos] = None

        # Retourner le jeton retiré.
        return jeton_retire

    def obtenir_jeton(self, pos):
        """
        Cette méthode permet d'obtenir un jeton du chevalet: c'est comme si le joueur voulait voir un jeton de son chevalet. Donc obtenir un jeton à une position revient juste à retourner le jeton à la position indiquée.
        :param pos: Position du jeton.
        :return: Le jeton à la position d'intérêt.
        :exception: Levez une exception avec assert si la position spécifiée n'est pas valide ou si elle est vide. Pensez à réutiliser Joueur.position_est_valide et position_est_vide.
        """
        # À compléter
        # Mettre votre code ici

        # Vérifier que la position est valide et n'est pas vide.
        assert Joueur.position_est_valide(pos) and not self.position_est_vide(pos), "La position n'est pas valide ou elle est vide"

        # Retourner le jeton à la position spécifiée
        return self.__chevalet[pos]

    def ajouter_points(self, points):
        """
        Cette méthode permet d'ajouter des points à un joueur
        :param points: (int) points à ajouter.
        :return: Ne retourne rien.
        """
        # À compléter
        # Mettre votre code ici

        # Ajouter les points au joueur
        self.__points += points

    def melanger_jetons(self):
        """
        Cette méthode permet de mélanger au hasard le chevalet du joueur, c'est-à-dire mélanger les positions des éléments dans la liste représentant le chevalet.
        Pensez à utiliser la fonction shuffle du module random.
        :return: Ne retourne rien.
        """
        # À compléter
        # Mettre votre code ici

        # Mélanger au hasard le chevalet du joueur en utilisant la fonction shuffle du module random
        shuffle(self.__chevalet)

    def __str__(self):
        """ *** Vous n'avez pas à coder cette méthode ***
        Formatage du joueur. Cette méthode est appelée lorsque vous faites str(v) où v est un joueur.
        :return: str représentant le joueur.
        """
        s = "{}\n".format(self.nom)
        s += "Score: {}\n".format(self.points)
        s += "            " + "".join(["{:<3s}".format(str(x)) if x else '  ' for x in self.__chevalet])
        s += "\nChevalet: \_" + "__".join([chr(0x2080 + i + 1) for i in range(self.TAILLE_CHEVALET)]) + '_/\n'
        return s

if __name__ == "__main__":
        j1 = Joueur("Brahima")