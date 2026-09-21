#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    const int MAX_TAILLE = 100;
    int taille1, taille2;
    int tableau1[MAX_TAILLE], tableau2[MAX_TAILLE];
    int resultat[2 * MAX_TAILLE];

    cout <<"Entrez la taille de pramier tableau : ",
    cin >> taille1;

    cout << "Entrez les elements du premier tableau (tries) : " << endl;
    for (int i =0; i < taille1; ++i) {
        cout << "Element " << i + 1 << " : ";
        cin >> tableau1[i];
    }

    cout << "Entrez la taille du deuxième tableau : ";
    cin >> taille2;

    cout << "Entrez les elements du deuxième tableau (triés) :" << endl;
    for (int i = 0; i < taille2; ++i) {
        cout << "Element " << i + 1 << " : ";
        cin >> tableau2[i];
    }

    cout << "Tableau 1 : ";
    for (int i = 0; i < taille1; ++i) {
        cout << tableau1[i] << " ";
    }
    cout << endl;

    cout << "Tableau 2 : ";
    for (int i = 0; i < taille2; ++i) {
        cout << tableau2[i] << " ";
    }
    cout << endl;    

    merge(tableau1, tableau1 + taille1, tableau2, tableau2 + taille2, resultat);

    cout << "Tableau fusionne : ";
    for (int i = 0; i < taille1 +taille2; ++i) {
        cout << resultat[i] <<" ";
    }
    cout <<endl;

    return 0;
}
