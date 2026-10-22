#include <iostream>
#include <limits>
using namespace std;



//terminal communication
string GetName() { 
    string name; //makes name a veriable

    cout << "  Hello, What Is Your Name?  " << endl; //will write in the terminal
    cin >> name; //allows the user to write in the terminal

    
    
    // if the name the user writes one of the names listed in "if", the computer will respond with "yessir"
    if (name == "Jarvis") 
    {
        cout << "\nYessir\n"
    ;} 
    else {
        cout << "Nice to meet you " <<name << "!\n" << endl; //will write a msg in the treminal, it also uses the name variable. which prints the users input in the computers response
    }

    return name; //returns the code status
}

int GetAge(string username) {
    int age;

    if (username == "William"){
        age = 16;
        cout << "you are" << age << "." << endl;
    }
    
    if (username == "Jarvis"){
        age = 3000; 
        cout << "\nI love you" << age << "." << endl;
    }
   
    


    // making age not accept letters.

    while(true) {

        cout << "what is your age? \n" << endl;
        cin >> age;

    
        if (cin.fail()){
        cout << "Those are nut numbers, please use numbers.\n" << endl;

        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }
    else {
        cout << "\n you gave the the age " << age << "." << username << " is " << age << " years old. \n" << endl;
        
        break;
        

    }
}
 


    

    
    
    return age;
}

int main() {
    string username = GetName();
    int userage = GetAge(username);
    
    

    return 0;
}
