#include <iostream>
#include <cstring>

using namespace std;

int compterVoyelles(const char* chaine) {
    int nbVoyelles = 0;

    for (int i =0; i < strlen(chaine); ++i) {
        char caractere = tolower(chaine[i]);

        if (caractere == 'a' || caractere == 'e' || caractere == 'i' || caractere == 'o' || caractere =='u') {
            nbVoyelles++;
        }
    }

    return nbVoyelles;
}

int main() {
    const int MAX_TAILLE = 1000;
    char chaine[MAX_TAILLE];

    cout << "Entrez une chaine de caracteres : ";
    cin.getline(chaine, MAX_TAILLE);

    int nbVoyelles = compterVoyelles(chaine);

    cout <<"Le nombre de voyelles dans la chaine est : "<< nbVoyelles << endl;

    return 0;
}