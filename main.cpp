//
// This is example code from Chapter 2.2 "The classic first program" of
// "Programming -- Principles and Practice Using C++" by Bjarne Stroustrup
//
// This program outputs the message "Hello, World!" to the monitor

#include "std_lib_facilities.h"

//------------------------------------------------------------------------------'
/*
def maxOfTwo(a, b):
    if a > b:
        print("A is greater than B")
    return a
    
    else:
        print("B is greater than or equal to A")
    return b
*/
int a = 1;
int b = 0;


int main() {

    if (a > b){
        cout << a << endl;
    } else {
        cout << b << endl;
    }
    return 0;
}

/*
// funksjonen 'add' som har to parameter av
// typen 'int' og returverdi av typen 'int'.
int add(int a, int b) {
    // legger sammen verdiene av 'a' og 'b' og returner resultatet
    return a + b;
}

int main() {
    // Skriver 'Hello world!' i konsollen
    cout << "Hello world!" << endl;
    // Kaller på 'add' med heltallene 1 og 2 som argumenter.
    // Returverdien (3) skrives ut i konsollen
    cout << add(1, 2) << endl;
    
    return 0;
    }

*/


//------------------------------------------------------------------------------
