// Utilisant la fonction sort de la bibliothèque <algorithm>
#include <iostream>
#include <algorithm>

using namespace std;

void afficherTableau(int tableau[], int taille) {
    for(int i = 0; i < taille; ++i) {
        cout <<tableau[i] << " ";
    }
    cout << endl;
}

int main() {
    const int MAX_TAILLE = 100;
    int taille;
    int tableau [MAX_TAILLE];

    cout << "Entrez la taille du tableau : ";
    cin >> taille;

    cout << "Entrz les element du tableau :" << endl;
    for(int i = 0; i < taille; ++i) {
        cout << "Element "<< i + 1 << " : ";
        cin >> tableau[i]; 
    }

    cout << "Tableau avant le tri : ";
    afficherTableau(tableau, taille);

    sort(tableau, tableau + taille); // Pour tri croissant

    cout<< "Taleau apres le tri croissant : ";
    afficherTableau(tableau, taille);

    sort(tableau, tableau + taille, greater<int>()); // Pour tri décroissant

    cout<< "Taleau apres le tri decroissant : ";
    afficherTableau(tableau, taille);
    return 0;
}