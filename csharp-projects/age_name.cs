Console.WriteLine("Excuse me, what is your name?");
string name = Console.ReadLine();


Console.WriteLine("Nice to meet you " + name + ", if you don't mind me asking. How old are you? :)");
int age = Convert.ToInt32(Console.ReadLine());


if (age >= 150)
{
    Console.WriteLine("That's very unlikely. Are you sure that you're " + age + "?" + Environment.NewLine + "Not sure i believe this... ");
}

else
{
    Console.WriteLine("So you are " + name + ", age " + age + ", correct?");
}