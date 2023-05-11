class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.points = 0
    
    def ajouter_points(self, points):
        self.points += points
    
    def __str__(self):
        return self.nom

class Match:
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = None
    
    def jouer_match(self, resultat):
        self.resultat = resultat
        
        if resultat == 0.5:
            self.joueur1.ajouter_points(0.5)
            self.joueur2.ajouter_points(0.5)
        elif resultat == 1:
            self.joueur1.ajouter_points(1)
        elif resultat == 2:
            self.joueur2.ajouter_points(1)
    
    def __str__(self):
        return f"{self.joueur1} vs {self.joueur2} : {self.resultat}"
    
class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin, tours=None, joueurs=None, nb_tours=4, tour_actuel=1, remarques=None):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nb_tours = nb_tours
        self.tour_actuel = tour_actuel
        self.tours = tours if tours else []
        self.joueurs = joueurs if joueurs else []
        self.remarques = remarques if remarques else ""

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)

    def ajouter_tour(self, tour):
        self.tours.append(tour)

    def tour_suivant(self):
        self.tour_actuel += 1

    def __str__(self):
        return f"{self.nom} ({self.date_debut} - {self.date_fin}) à {self.lieu} avec {len(self.joueurs)} joueurs"

class Tour:
    def __init__(self, numero, matchs=None):
        self.numero = numero
        self.matchs = matchs if matchs else []

    def ajouter_match(self, match):
        self.matchs.append(match)

    def __str__(self):
        return f"Tour {self.numero} ({len(self.matchs)} matchs)"

