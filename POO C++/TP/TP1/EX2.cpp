#include <iostream>

using namespace std;
 
int main() {
    cout << "Nombres   Carré     Cube" << endl;

    for (int i; i <= 10; ++i) {
        int carre = i * i;
        int cube = i * i * i;
        cout << i << "         " << carre << "         " << cube << endl;
    }
    return 0;
}
