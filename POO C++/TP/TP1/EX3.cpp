#include <iostream>

using namespace std;

unsigned long long factorielle(int n) {
    unsigned long long resultat = 1;
    for(int i =1; i <= n; ++i) {
        resultat *=i;
    }
    return resultat;
}

int main() {
    int nombre;

    cout << "Entrez un nombre : ";
    cin >> nombre;

    if( nombre < 0) {
        cout << "La factorielle n'est pas définie pour les nombre négatifs." << endl;

    }else {
        unsigned long long resultat = factorielle(nombre);
        cout << "La factorielle de " << nombre << " est : " << resultat << endl;
    }
    return 0;
}