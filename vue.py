class Vue:
    def afficher_resultats_tournoi(self, joueurs):
        joueurs.sort(key=lambda x: x.points, reverse=True)
        print("Résultats du tournoi :")
        for i, joueur in enumerate(joueurs):
            print(f"{i+1}. {joueur.nom} : {joueur.points} points")
    
    def afficher_tournoi(self, tours):
        res = f"Tournoi à {len(tours)} tours : \n"
        for tour in tours:
            res += f"{tour}\n"
        print(res)

class TournoiVue:
    def afficher_tournoi(self, tournoi):
        print(f"{tournoi.nom} ({tournoi.date_debut} - {tournoi.date_fin}) à {tournoi.lieu}")
        print(f"{len(tournoi.joueurs)} joueurs enregistrés")
        print(f"Tour actuel : {tournoi.tour_actuel}/{tournoi.nb_tours}")
        print(f"Remarques : {tournoi.remarques}\n")
        for tour in tournoi.tours:
            print(tour)
            for match in tour.matchs:
                print(match)
            print()

    def ajouter_joueur(self):
        nom = input("Nom du joueur : ")
        prenom = input("Prénom du joueur : ")
        date_naissance = input("Date de naissance du joueur : ")
        classement = input("Classement du joueur : ")
        return (nom, prenom, date_naissance, classement)

    def ajouter_tour(self):
        return int(input("Numéro du tour : "))