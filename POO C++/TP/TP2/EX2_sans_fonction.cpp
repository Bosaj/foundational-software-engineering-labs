// Programme sans l'utilisation d'une fonction
#include <iostream>

using namespace std;

int main() {
    int taille;
    cout << "Entrez la taille du tableau : ";
    cin >> taille;

    int tableau[taille];

    cout << "Entrz les elements du tableau :" <<endl;
    for (int i = 0; i < taille; ++i) {
        cout << "Element "<< i + 1 << " : ";
        cin >> tableau[i];
    }

    int elementCible;
    cout << "Entrez l'element a rechercher : ";
    cin >> elementCible;

    bool trouve = false;
    for (int i = 0; i < taille; ++i) {
        if (tableau[i] == elementCible) {
            cout << "L'element" << elementCible << " a ete trouve a l'index " << i << endl;
            trouve = true;
            break;
        }
    }
    if (!trouve) {
        cout << "L'element " << elementCible << " n'a pas ete trouve dans le tableau." << endl;
    }

    return 0;
}