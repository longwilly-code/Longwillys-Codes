#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <list>
#include <algorithm>
#include <cctype>
using namespace std;



// cool way to fully clear out a terminal via aasci
void clear_terminal()
    {
        cout << "\033[2J\033[1;1H";
    };


void menu_print(){
    cout << "-----MENU-----" << endl;
};

// function that lets the user order
string order(){
    cout << "Buy: ";
    string item;
    getline(cin, item);

    // transforms the letters to lower case
    transform(item.begin(), item.end(), item.begin(), [](unsigned char c){
        return tolower(c);
    });

    return item;
};


// uses the data for the list and dict.
void print_receipt(const list<string>& cart, const unordered_map<string, int>& prices){

    // to make the receipt look nice i use the clear terminal func, and then print the first part of the receipt
    clear_terminal();
    cout << "-----RECEIPT-----" << endl;
    int total_price = 0;


    // loop for every string in the list/cart takes the price and prints it like this "item: xkr"
    for (const string& item : cart)
    {

        int item_price = prices.at(item);

        cout << item << ": " << item_price << "kr" << endl;
        total_price += item_price;
    }

    // use the total price we now have from combining the item_price from the items in the cart, and print the rest of the reciept.
    cout << "-----------------" << endl;
    cout << "TOTAL: " << total_price << "kr" << endl;
    cout << "Thank you for your purchase" << endl;
};

int main() {

    clear_terminal();
    menu_print();
    

    // i wanted to make a dict like in python, but when i tried printing the dict, it came in a random order. 
    //Unlike python, in c++ you have to manually make it print in the order you want to.
    unordered_map<string, int> dict;
    vector<string> menu;


    auto add_item = [&](const string& name, int price)
    {
        dict[name] = price;
        menu.push_back(name);
    };

    // add the items to the menu
    add_item("popcorn", 50);
    add_item("soda", 30);
    add_item("candy", 35);
    add_item("chocolate",  40);

    for (const string& item : menu)
    {
        cout << item << ": " << dict[item] << "kr" << endl;
    }




    // ordering
    // start with an empty list and push_back any items from get_order that is in the dict.
   

    list<string> mylist;

    while (true){

        string get_order = order();
    
        if (dict.count(get_order))
        {
            mylist.push_back(get_order);
            cout << get_order << " added to cart" << endl;
        }

        // if the input is 'q' it will print what you bought, and will stop the program
        else if (get_order == "q"){
            if (mylist.empty())
            {
                cout << "Have a nice day!" << endl;
            }
            else
            {
                print_receipt(mylist, dict);
            }
            break;
        }

        else{
            cout << "We do not serve that item." << endl;
        }


    }

    return 0;
}