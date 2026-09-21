#include <iostream>

using namespace std;

int main() {
    int nombre;
    int total = 0;
    int count = 0;

    cout << "Entrez une serie de nombre (terminee par un nombre negatif) : " << endl;

    while (true){
        cin >> nombre;

        if (nombre < 0) {
            break;
        }

        total += nombre;

        count++;
    }

    if (count > 0) {
        double moyenne = static_cast<double>(total) / count;
        cout << "La moyenne des nombre saisis est : "<< moyenne <<endl;
    }else{
        cout << "Aucun nombre n'a ete saisi." << endl;
    }

    return 0;
    
}