Console.WriteLine("first c# clac :)");


Console.Write("Input your numbers here:");

double num1 = Convert.ToDouble(Console.ReadLine());

Console.Write("allowed ops: +, -, *");
string op = Console.ReadLine();

double num2 = Convert.ToDouble(Console.ReadLine());

double result = 0;


if (op == "+")
{
    result = num1 + num2;
}
else if (op == "-")
{
    result = num1 - num2;
}
else if (op == "*")
{
    result = num1 * num2;
}

else
{
    Console.WriteLine("invalid op");
    return;
}

Console.WriteLine("restult: " + result);