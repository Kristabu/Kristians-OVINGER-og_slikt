//
// This is example code from Chapter 2.2 "The classic first program" of
// "Programming -- Principles and Practice Using C++" by Bjarne Stroustrup
//
// This program outputs the message "Hello, World!" to the monitor

#include "std_lib_facilities.h"

//------------------------------------------------------------------------------'
//oppgave a)
/*
def maxOfTwo(a, b):
    if a > b:
        print("A is greater than B")
    return a
    
    else:
        print("B is greater than or equal to A")
    return b
*/


int maxof2(int a, int b){
        if (a > b){
        cout << "A is greater than B" << endl;
        return a;
    } else {
        cout << "B is greater than or equal to A" << endl;
        return b;
    }
}

//------------------------------------------------------------------------------
//oppgave c
/*
def fibonacci(n):
    a = 0
    b = 1
    print("Fibonacci numbers:")
    for x in range(1, n + 1):
        print(x, b)
        temp = b
        b += a
        a = temp
    print("----")
    return b
*/

int fibonacci(int n){
    int a = 0;
    int b = 1;
    cout << "Fibonacci numbers:" << endl;
    for (int x = 1; x < n+1; ++x) {
        cout << x << " " << b << endl;
        int temp = b;
        b += a;
        a = temp;
    }
    cout << "----" << endl;
    return b;
}

//------------------------------------------------------------------------------
//oppgave d
/*
def squareNumberSum(n):
    totalSum = 0
    for i in range(1, n + 1):
        totalSum += i * i
        print(i * i)
    print(totalSum)
    return totalSum
*/

int squareNumberSum(int n){
    int totalSum = 0;
    for (int i = 1; i < n + 1; ++i){
        totalSum += (i * i);
        cout << (i * i) << endl;
    }
    cout << totalSum << endl;
    return totalSum;
}

//------------------------------------------------------------------------------
//oppgave e
/*
def triangleNumbersBelow(n):
    acc = 1
    num = 2
    print("Triangle numbers below ", n, ":", sep="")
    while acc < n:
        print(acc)
        acc += num
        num += 1
    print()
*/
void triangleNumbersBelow(int n){
    int acc = 1;
    int num = 2;
    cout << "Triangle numbers below " << n << ":" << endl;
    while(acc < n){
        cout << acc << endl; 
        acc += num;
        num += 1;
    }
    cout << endl;
}

/*
I C++ er det ikke vanlig å ha returverdi for en 'void'-funksjon, siden 'void'
spesifiserer at funksjonen ikke returnerer noen verdi. Imidlertid kan du vise resultater 
til skjerm fra en 'void'-funksjon ved å bruke 'std::cout' eller lignende metoder for å 
skrive til standardutgangen (for eksempel terminalvinduet).
*/

//------------------------------------------------------------------------------
//oppgave f




//------------------------------------------------------------------------------
//oppgave b
/*
    cout << "" << endl;
    cout <<  << endl;
*/

int main() {
    cout << "Oppgave a)" << endl;
    cout << maxof2(5, 6) << endl;

    cout << "Oppgave c)" << endl;
    cout << fibonacci(5) << endl;
    
    cout << "Oppgave d)" << endl;
    cout << squareNumberSum(5) << endl;

    cout << "Oppgave e)" << endl;
    triangleNumbersBelow(10);

    return 0;
}


