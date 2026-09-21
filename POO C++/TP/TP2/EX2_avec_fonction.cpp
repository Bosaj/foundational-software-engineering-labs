// En utilisant une fonction pour la recherche
#include <iostream>

using namespace std;

int rechercherElement(int tableau[], int taille, int elementCible) {
    for (int i = 0; i < taille; ++i) {
        if (tableau[i] == elementCible) {
            return i;
        }
    }
    return -1; // Retourne -1 si l'élément n'est pas trouvé
}

int main() {
    int taille;
    cout << "Entrez la taille du tableau : ";
    cin >> taille;

    int tableau[taille];

    cout << "Entrez les elements du tableau :" << endl;
    for (int i = 0; i < taille; ++i) {
        cout << "Element " << i + 1 << " : ";
        cin >> tableau[i];
    }

    int elementCible;
    cout << "Entrez l'element a rechercher : ";
    cin >> elementCible;

    int index = rechercherElement(tableau, taille, elementCible);

    if (index != -1) {
        cout << "L'element " << elementCible << " a ete trouve a l'index " << index << endl;
    } else {
        cout << "L'element " << elementCible << " n'a pas ete trouve dans le tableau." << endl;
    }

    return 0;
}
