#include <iostream>
using namespace std;

// will print some info for the user
void print() { 

    cout << "Calculator\n" << endl;

    cout << "Operations: +, -, *, / " << endl;
}

// Gets the number the user writes
int GetNumber() {
    
    int number;

    cin >> number;

    return number;
}


int main() {
    print();

    // uses the number the user wrote and makes it n1
    cout << "Write a number, operation and a new number\n" << endl;
    int n1 = GetNumber(); //n1 = first number

    // makes op a character, only works with '' and not ""
    char op;
    cin >> op;

    // uses the second number the user writes as n2. this happens because GetNumber repeats each time it is mentioned.
    int n2 = GetNumber();

    int result; // makes result accessible


    // the char or "op" will allow the useage of one of the following: +, -, *, / 
    //depending on what the user chooses the result will show by the math function "n1, op, n2" 
    if (op == '+') {
        result = n1 + n2;
    }
    else if (op == '-')
    {
        result = n1 - n2;
    }
    else if (op == '/')
    {
        if (n2 == 0){
            cout << "can't divide by 0" << endl;
        }
        result = n1 / n2;
    }
    else if (op == '*')
    {
        result = n1 * n2;
    }
    
    // this will print the result as well as a message.
    cout << "\n Result --  " << result << endl;

    return 0;
}