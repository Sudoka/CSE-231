// GA Project 01
// Create a bitstring and evaluate its fitness using C++ and classes

/* Includes */
#include <cstring>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <time.h>

/* Using */
using namespace std;

/* Classes */
class individual
{
    public:
        string bitstring;
        int fitness;
  
        individual();

        friend ostream &operator<<(ostream &stream, individual ob);
    
        string genBitstring()
        {
            string temp;
            srand(time(NULL));
            for(int i = 0; i < 100; i++)
            {
                int rChar = (rand() % 2);
                if (rChar == 0)
                {
                    temp += "0";
                }
                else if (rChar == 1)
                {
                    temp += "1";
                }
            }
            return temp;
        }
    
        int genFitness()
        {
            int count = 0;
            for (int i = 0; i < bitstring.length(); i++)
            {
                if (bitstring[i] == '1')
                {
                    count++;
                }
            }
            return count;
        }
};

individual::individual()
{
    bitstring = genBitstring();
    fitness = genFitness();
}

ostream &operator<<(ostream &stream, individual ob)
{
    stream << "Bitstring: " << ob.bitstring << "\nFitness: " << ob.fitness << "\n\n";
    return stream;
}


/* Main */
int main()
{
individual ind1;
cout << ind1;

return 0;
}
