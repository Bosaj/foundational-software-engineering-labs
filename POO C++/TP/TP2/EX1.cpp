#include <iostream>

using namespace std;

int sommeElements(int tableau[], int taille) {
    int somme = 0;

    for (int i = 0; i < taille; ++i) {
        somme += tableau[i];
    }

    return somme;
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

    int resultat = sommeElements(tableau, taille);

    cout << "La somme des elements du tableau est : " << resultat << endl;

    return 0;
}