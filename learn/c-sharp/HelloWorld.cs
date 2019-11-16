using System;

namespace HelloWorldNS
{
    class HelloWorld
    {
        static int Main(String[] args)
        {
            Console.WriteLine("Hello World!");
            int meaningOfLife = 42;
            // int meaningOfLife = 42;
            // int MeaningOfLife = 42;
            var theMeaningOfLife = 42;
            var _theMeaningOfLife = 42;

            //var name = "chandan";
            string name = "chandan";

            Console.WriteLine("The meaning of Life is .....");
            Console.WriteLine(name, theMeaningOfLife, _theMeaningOfLife);

            return 0;
        }
    }
}