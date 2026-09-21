// En utilisant l'algorithme de tri par insertion
#include <iostream>

using namespace std;

// Fonction pour afficher le tableau
void afficherTableau(int tableau[], int taille) {
    for (int i = 0; i < taille; ++i) {
        cout << tableau[i] << " ";
    }
    cout << endl;
}

// Fonction pour trier le tableau en ordre croissant
void triCroissant(int tableau[], int taille) {
    for (int i = 1; i < taille; ++i) {
        int cle = tableau[i];
        int j = i - 1;
        while (j >= 0 && tableau[j] > cle) {
            tableau[j + 1] = tableau[j];
            j = j - 1;
        }
        tableau[j + 1] = cle;
    }
}

// Fonction pour trier le tableau en ordre décroissant
void triDecroissant(int tableau[], int taille) {
    for (int i = 1; i < taille; ++i) {
        int cle = tableau[i];
        int j = i - 1;
        while (j >= 0 && tableau[j] < cle) {
            tableau[j + 1] = tableau[j];
            j = j - 1;
        }
        tableau[j + 1] = cle;
    }
}

int main() {
    const int MAX_TAILLE = 100;
    int taille;
    int tableau[MAX_TAILLE];

    cout << "Entrez la taille du tableau : ";
    cin >> taille;

    cout << "Entrez les elements du tableau :" << endl;
    for (int i = 0; i < taille; ++i) {
        cout << "Element " << i + 1 << " : ";
        cin >> tableau[i];
    }

    cout << "Tableau avant le tri : ";
    afficherTableau(tableau, taille);

    triCroissant(tableau, taille); // Pour tri croissant

    cout << "Tableau apres le tri croissant : ";
    afficherTableau(tableau, taille);


    triDecroissant(tableau, taille); // Pour tri décroissant

    cout << "Tableau apres le tri decroissant : ";
    afficherTableau(tableau, taille);

    return 0;
}
