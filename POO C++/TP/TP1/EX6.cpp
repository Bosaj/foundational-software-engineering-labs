#include <iostream>

using namespace std;

double celsiusVersFahrenheit(double celsius) {
    return (celsius * 9 / 5) + 32;
}

double fahrenheitVersCelsius(double fahrenheit) {
    return (fahrenheit - 32) * 5 / 9;
}

int main() {
    char choix;
    double temperture;

    cout << "Choisissez la conversion : " << endl;
    cout << "Celsius vers Fahrenheit (C) / Fahrenheit vers Celsius (F) : ";
    cin >> choix;

    if (choix == 'C' || choix == 'c') {
        cout << "Entrez la temperature en degres Celsius : ";
        cin >> temperture;
        cout << temperture <<" degres Celsius equivalant a " << celsiusVersFahrenheit(temperture) << " degres Fahrenheit." << endl;
    }else if(choix == 'F' || choix == 'f') {
        cout << "Entrez la temperature en degres Fahrenheit : ";
        cin >> temperture;
        cout << temperture << " degres Fahrenheit équivalant a " << fahrenheitVersCelsius(temperture) << " degres Celsius." << endl;
    }else {
        cout << "Choix invalide." << endl;
    }
    
    return 0;
}