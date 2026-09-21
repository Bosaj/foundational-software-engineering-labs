#include <iostream>
#include <string>

using namespace std;

class Article {
    protected:
        string titre;
        string auteur;
        int annee;
        bool disponible;

    public:
        Article(string titre, string auteur, int annee) : titre(titre), auteur(auteur), annee(annee), disponible(true) {}

        void emprunter() {
            disponible = false;
        }

        void retourner() {
            disponible = true;
        }

        virtual void afficherDetails() const {
            cout << "     Titre: " << titre << endl;
            cout << "     Auteur: " << auteur << endl;
            cout << "     Annee: " << annee << endl;
            cout << "     Disponible: " << (disponible ? "Oui" : "Nom") << endl;
        }
};

class Livre : public Article {
    private:
        string genre;

    public:
        Livre(string titre, string auteur, int annee, string genre) : Article(titre, auteur, annee), genre(genre) {}

        void afficherDetails() const override {
            Article::afficherDetails();
            cout << "     Genre: "<< genre << endl;
        }
};

class Magazine : public Article {
    private:
        int mois;

    public:
        Magazine(string titre, string auteur, int annee, int mois) : Article(titre, auteur, annee), mois(mois) {}

            void afficherDetails() const override {
                Article::afficherDetails();
                cout << "     Mois de publication: " << mois << endl;
            }
        
};

int main() {
    Livre livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954, "Fantasy");
    Magazine magazine("National Geographic", "National Geographic Society", 1888, 3);

    cout << "Details du livre :" << endl;
    livre.afficherDetails();
    cout << endl;

    cout << "Details du magazine :" << endl;
    magazine.afficherDetails();
    cout << endl;
    return 0;
}