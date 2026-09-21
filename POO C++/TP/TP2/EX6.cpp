#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> vecteur;
    int taille, valeur;

    // Demander à l'utilisateur la taille du vecteur
    cout << "Entrez la taille du vecteur : ";
    cin >> taille;

    cout << "Entrez les elements du vecteur : "<< endl;
    for (int i = 0; i < taille; ++i) {
        cout << "Element "<< i + 1 << " : ";
        cin >> valeur;
        vecteur.push_back(valeur);
    }

    // Supprimer les éléments impairs du vecteur
    for (auto it = vecteur.begin(); it != vecteur.end(); ) {
        if (*it % 2 != 0) {
            it = vecteur.erase(it);
        }else {
            ++it;
        }
    }

    // Afficher le vecteur résultant
    cout << "Vecteur resultant (élements pairs uniquement) :"<< endl;
    for (int num : vecteur) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}