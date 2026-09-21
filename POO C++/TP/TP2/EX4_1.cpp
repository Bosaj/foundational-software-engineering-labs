// fusionne deux tableaux triés en un troisième tableau trié sans utiliser la fonction "merge" :

#include <iostream>

using namespace std;

void fusionnerTableaux(int tableau1[], int taille1, int tableau2[], int taille2, int resultat[]) {
    int i = 0, j = 0 , k = 0;

    while(i < taille1 && j < taille2) {
        if(tableau1[i] < tableau2[j]) {
            resultat[k++] = tableau1[i++];
        }else {
            resultat[k++] = tableau2[j++];
        }
    }

    while (i < taille1) {
        resultat[k++] = tableau1[i++];
    }

    while (j < taille2) {
        resultat[k++] = tableau2[j++];
    }
}

void afficherTableau(int tableau[], int taille) {
    for (int i = 0; i < taille; ++i) {
        cout << tableau[i] << " ";
    }
    cout << endl;
}

int main() {
    const int MAX_TAILLE = 100;
    int taille1, taille2;
    int tableau1[MAX_TAILLE], tableau2[MAX_TAILLE];
    int resultat[2 * MAX_TAILLE];

    cout << "Entrez la taille du premier tableau : ";
    cin >> taille1;

    cout << "Entrez les elements du premier tableau (tries) :" << endl;
    for (int i = 0; i < taille1; ++i) {
        cout << "Element " << i + 1 << " : ";
        cin >> tableau1[i];
    }

    cout << "Entrez la taille du deuxième tableau : ";
    cin >> taille2;
    
    cout << "Entrez les elements du deuxieme tableau (tries) :" << endl;
    for (int i = 0; i < taille2; ++i) {
        cout << "Element " << i + 1 << " : ";
        cin >> tableau2[i];
    }

    cout << "Tablaeu 1 : ";
    afficherTableau(tableau1, taille1);
    
    cout << "Tablaeu 2 : ";
    afficherTableau(tableau2, taille2);

    fusionnerTableaux(tableau1, taille1, tableau2, taille2, resultat);

    cout << "Tablaeu fusionne : ";
    afficherTableau(resultat, taille1 + taille2);
    
    
}