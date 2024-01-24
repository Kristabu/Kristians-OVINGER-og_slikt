//
// This is example code from Chapter 2.2 "The classic first program" of
// "Programming -- Principles and Practice Using C++" by Bjarne Stroustrup
//
// This program outputs the message "Hello, World!" to the monitor

#include "std_lib_facilities.h"

//------------------------------------------------------------------------------'
//oppgave a)
/*
lag en meny
*/

int main() {

        //menu
    cout << "Velg funksjon: \n"
            "0) Avslutt \n"
            "1) Summer to tall \n"
            "2) Summer flere tall \n"
            "3) Konverter NOK til EURO." << endl; 

    int x;
    cin >> x;

    switch(x) {
        case 0:
            cout << "0) Avslutt" << endl;
            break;
        case 1:
            cout << "1) besj" << endl;
            break;
        case 2:
            cout << "2) Avslutt" << endl;
            break;
        case 3:
            cout << "3) Avslutt" << endl;
            break;
        
        default:
            cout << "invalid" << endl;
            break;
    }

    return 0;
}