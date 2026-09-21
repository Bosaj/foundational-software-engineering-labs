#include <iostream>
#include <string>

using namespace std;

class Personne {
    private:
        string nom;
        int age;
    
    public:
        Personne() {
            nom = "Inconnu";
            age = 0;
        }

        Personne(string nom, int age) {
            this->nom = nom;
            this->age = age;
        }

        void initialiser(string nom, int age) {
            this->nom = nom;
            this->age = age;
        }

        void afficherInformation() {
            cout << "Nom : " << nom <<endl;
            cout << "Age : " << age << endl;
        }
};

int main() {
    Personne personne1;

    personne1.initialiser("Alice", 30);

    personne1.afficherInformation();

    return 0;
}