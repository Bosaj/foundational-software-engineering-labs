#include <iostream>
#include <vector>

using namespace std;

// Fonction pour calculer le produit scalaire de deux vecteurs
int produitScalaire(const vector<int>& vecteur1, const vector<int>& vecteur2) {
    // Vérifier si les deux vecteurs ont la même taille
    if (vecteur1.size() != vecteur2.size()) {
        cerr << "Les vecteurs doivent avoir la même taille !" << endl;
        return 0;
    }

    int produit = 0;
    for (size_t i = 0; i < vecteur1.size(); ++i) {
        produit += vecteur1[i] * vecteur2[i];
    }
    return produit;
}

int main() {
    // Demander à l'utilisateur la taille des vecteurs
    int taille;
    cout << "Entrez la taille des vecteurs : ";
    cin >> taille;

    // Créer les deux vecteurs dynamiques
    vector<int> vecteur1(taille);
    vector<int> vecteur2(taille);

    // Remplir les vecteurs avec des valeurs saisies par l'utilisateur
    cout << "Entrez les valeurs du premier vecteur :" << endl;
    for (int i = 0; i < taille; ++i) {
        cout << "Element " << i + 1 << " : ";
        cin >> vecteur1[i];
    }

    cout << "Entrez les valeurs du deuxième vecteur :" << endl;
    for (int i = 0; i < taille; ++i) {
        cout << "Element " << i + 1 << " : ";
        cin >> vecteur2[i];
    }

    // Calculer et afficher le produit scalaire des deux vecteurs
    int resultat = produitScalaire(vecteur1, vecteur2);
    cout << "Le produit scalaire des deux vecteurs est : " << resultat << endl;

    return 0;
}
