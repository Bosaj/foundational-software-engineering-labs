#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Classe Livre
class Livre {
    private:
        string titre;
        string auteur;
        int anneeDePublication;

    public:
        // Constructeur avec paramètres
        Livre(string titre, string auteur, int anneeDePublication) : titre(titre), auteur(auteur), anneeDePublication(anneeDePublication) {}

        // Méthode pour afficher les informations du livre
        void afficherInformations() const {
            cout << "Titre: " << titre << endl;
            cout << "Auteur: " << auteur << endl;
            cout << "Annee de publication: " << anneeDePublication << endl;
        }

        // Méthode pour obtenir le titre du livre
        string getTitre() const {
            return titre;
        }
};

// Classe Bibliotheque
class Bibliotheque {
    private:
        vector<Livre> livres;

    public:
        // Méthode pour ajouter un livre à la bibliothèque
        void ajouterLivre(const Livre& livre) {
            livres.push_back(livre);
        }

        // Méthode pour afficher tous les livres de la bibliothèque
        void afficherLivres() const {
            if (livres.empty()) {
                cout << "La bibliotheque est vide." << endl;
                return;
            }

            cout << "Livres dans la bibliotheque :" << endl;
            for (const Livre& livre : livres) {
                livre.afficherInformations();
                cout << endl;
            }
        }

        // Méthode pour rechercher un livre par titre
        void rechercherLivreParTitre(const string& titre) const {
            bool livreTrouve = false;

            for (const Livre& livre : livres) {
                if (livre.getTitre() == titre) {
                    livre.afficherInformations();
                    livreTrouve = true;
                    break;
                }
            }

            if (!livreTrouve) {
                cout << "Le livre avec le titre \"" << titre << "\" n'a pas ete trouve dans la bibliotheque." << endl;
                cout << endl;
            }
        }
};

int main() {
    // Création d'une bibliothèque
    Bibliotheque bibliotheque;

    // Ajout de quelques livres à la bibliothèque
    Livre livre1("Harry Potter a l'ecole des sorciers", "J.K. Rowling", 1997);
    Livre livre2("Le Seigneur des anneaux", "J.R.R. Tolkien", 1954);
    Livre livre3("1984", "George Orwell", 1949);

    bibliotheque.ajouterLivre(livre1);
    bibliotheque.ajouterLivre(livre2);
    bibliotheque.ajouterLivre(livre3);

    // Affichage de tous les livres de la bibliothèque
    bibliotheque.afficherLivres();

    // Recherche d'un livre par titre
    bibliotheque.rechercherLivreParTitre("194");

    return 0;
}
