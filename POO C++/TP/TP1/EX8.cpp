#include <iostream>
using namespace std;

int sommeDiviseurs(int nombre) {
    int somme = 0;

    for (int i = 1; i <= nombre; ++i) {
        if( nombre % i == 0){
            somme += 1;
        }
    }

    return somme;
}

int main() {
    int nombre;
    char continuer;
    do {
        cout << "Entrez un nombre entier : ";
        cin >> nombre;

        int resultat = sommeDiviseurs(nombre);

        cout << "La somme des diviseurs de " << nombre << " est : " << resultat << endl;
        
        cout <<"Veuillez vous continuer ? (O/N) : ";
        cin >> continuer;

    }while(continuer == 'O' || continuer == 'o');

    return 0;
}