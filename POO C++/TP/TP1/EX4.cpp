#include <iostream>
using namespace std;

int main() {
    int nombre;

    cout << "Entrez un nombre entier : ";
    cin >> nombre;

    cout << "Table de multiblication pour " << nombre << ":" << endl;
    for (int i = 0; i <= 10; ++i) {
        cout << nombre << " x " << i << " = " << nombre * i << endl;
    }
    return 0;
}