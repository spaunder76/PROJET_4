class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.points = 0

class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = None

    def jouer(self, resultat):
        self.resultat = resultat
        if resultat == "victoire":
            self.joueur1.points += 1
        elif resultat == "defaite":
            self.joueur2.points += 1
        elif resultat == "nul":
            self.joueur1.points += 0.5
            self.joueur2.points += 0.5

class Tour:
    def __init__(self, matches):
        self.matches = matches

class Tournoi:
    def __init__(self, joueurs, nb_tours):
        self.joueurs = joueurs
        self.nb_tours = nb_tours
        self.tours = []

    def commencer(self):
        for i in range(self.nb_tours):
            matches = self.creer_matches()
            tour = Tour(matches)
            self.tours.append(tour)
            self.jouer_matches(matches)

    def creer_matches(self):
        matches = []
        joueurs = self.joueurs.copy()
        while len(joueurs) > 1:
            joueur1 = joueurs.pop(0)
            joueur2 = joueurs.pop(0)
            match = Match(joueur1, joueur2)
            matches.append(match)
        return matches

    def jouer_matches(self, matches):
        for match in matches:
            resultat = input(f"{match.joueur1.nom} contre {match.joueur2.nom} (victoire, defaite ou nul) : ")
            match.jouer(resultat)

    def afficher_classement(self):
        joueurs = sorted(self.joueurs, key=lambda joueur: joueur.points, reverse=True)
        for i, joueur in enumerate(joueurs):
            print(f"{i+1}. {joueur.nom} ({joueur.points} points)")

if __name__ == "__main__":
    joueurs = [Joueur("Joueur 1"), Joueur("Joueur 2"), Joueur("Joueur 3"), Joueur("Joueur 4")]
    tournoi = Tournoi(joueurs, 2)
    tournoi.commencer()
    tournoi.afficher_classement()
