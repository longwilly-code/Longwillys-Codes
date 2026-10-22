#include <iostream>
using namespace std;

// User writes a number in the terminal, the number will be returned
int GetNumber() {

    int number;

    cin >> number;

    return number;
}

// Takes the number the user wrote and uses it to print.
void PrintNumber(int UserNumber) {
    cout << "You said the number " << UserNumber << "." << endl;
}

// Makes the returned details into new veriables.
int main() {
    int UserNumber = GetNumber();
    PrintNumber(UserNumber);

    return 0;
}

