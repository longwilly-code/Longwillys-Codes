using System;
using System.IO;


class Human
{


    private static Random rand = new Random();
    private static string[] names = File.ReadAllLines(@"C:\Users\William\.vscode\python\class human\names_txt.txt");
    private static string[] nationality = File.ReadAllLines(@"C:\Users\William\.vscode\python\class human\nationalities.txt");
    

    public string Name
    {
        get; private set;
    }


    public int Age
    {
        get; private set;   
    }

    public string Nation
    {
        get; private set;
    }


    public Human()
    {
        Name = names[rand.Next(names.Length)];
        Age = rand.Next(1, 100);
        Nation = nationality[rand.Next(nationality.Length)];
       
        Console.WriteLine($"Name: {Name} | Age: {Age} | Nation: {Nation}");
    }
}