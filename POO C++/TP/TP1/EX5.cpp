#include <iostream>

using namespace std;

bool estNombrePremier(int nombre) {
    if(nombre <= 1) {
        return false;
    }

    for(int i = 2; i*i <= nombre; ++i) {
        if (nombre % i == 0) {
            return false;
        }
    }

    return true;
}

int main() {
    int nombre;
    char continuer;

    do{
        cout << "Entrer un nombre entier : ";
        cin >> nombre;

        if (estNombrePremier(nombre)) {
            cout << nombre << " est un nombre premier." <<endl;
        }else {
            cout << nombre << " n'est pas un nombre premier" << endl;
        }

        cout <<"Voulez-vous continuer ? (O/N) : ";
        cin >> continuer;
    } while (continuer == 'O' || continuer == 'o');
    
    return 0;
    
}