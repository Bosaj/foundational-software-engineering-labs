#include <iostream>

using namespace std;

int main() {
    int somme = 0;

    for(int i = 0; i < 1000; ++i) {
        if(i % 3 == 0 || i % 5 == 0) {
            somme += i;
        }
    }

    cout << "La somme des multiples de 3 ou 5 inférieurs à 1000 est : " << somme << endl;

    return 0;
}