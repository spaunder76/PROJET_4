class Controleur:
    def __init__(self, nb_tours):
        self.nb_tours = nb_tours
        self.tours = []
        self.joueurs = []
        self.vue = Vue()
    
    def ajouter_joueur(self, nom):
        joueur = Joueur(nom)
        self.joueurs.append(joueur)
    
    def creer_tour(self, numero_tour):
        tour = Tour(numero_tour, self.joueurs)
        self.tours.append(tour)
    
    def jouer_tournoi(self):
        for tour in self.tours:
            tour.jouer_tour()
    
    def afficher_resultats_tournoi(self):
        self.vue.afficher_resultats_tournoi(self.joueurs)
    
    def afficher_tournoi(self):
        self.vue.afficher_tournoi(self.tours)

class Tour:
    def __init__(self, numero_tour, joueurs):
        self.numero_tour = numero_tour
        self.matchs = []
        self.joueurs = joueurs
    
    def ajouter_match(self, match):
        self.matchs.append(match)
    
    def jouer_tour(self):
        for match in self.matchs:
            resultat = int(input(f"Score de {match.joueur1} ({match.joueur2}) : "))
            match.jouer_match(resultat)
    
    def __str__(self):
        res = f"Tour {self.numero_tour} : \n"
        for match in self.matchs:
            res += f"{match}\n"
        return res
    
class TournoiControleur:
    def __init__(self, tournoi, vue):
        self.tournoi = tournoi
        self.vue = vue

    def ajouter_joueur(self):
        joueur = self.vue.ajouter_joueur()
        self.tournoi.ajouter_joueur(joueur)

    def ajouter_tour(self):
        numero = self.vue.ajouter_tour()
        tour = Tour(numero)
        self.tournoi.ajouter_tour(tour)