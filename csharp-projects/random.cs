Random rand =  new Random();

Console.WriteLine("Chose any number 1 - 99" + Environment.NewLine + "for more info type 'info' or to proceed type 'y'");


string input = Console.ReadLine();

if (input == "info")
{
    Console.WriteLine("The computer will chose a random number from 1 to 99. If your number matches the computers, you win.");
    return;
}

else if (input == "y")
{
    Console.WriteLine("Ok, You proceed. Now write your number.");
}

else
{
    Console.WriteLine(input + " is not an valid command");
    return;
}




int person_number;

while (!int.TryParse(Console.ReadLine(), out person_number) || person_number < 1 || person_number > 99)
{
    Console.WriteLine("enter any number from 1 to 99");
}


int comp_int = rand.Next(1, 100);


if (person_number == comp_int)
{
    Console.WriteLine($"You Won! The computer picked {comp_int}, you chose {person_number}!");
}
else
{
    Console.WriteLine($"You lost! The computer picked  {comp_int}, you chose {person_number}.");
}

