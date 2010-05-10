// GA Project 01
// Create a bitarray and evaluate its fitness using C++ and classes

/* Includes */
#include <iostream>
#include <list>
#include <stdlib.h>
#include <time.h>

/* Using */
using namespace std;

/* Classes */
class individual
{
    public:
        int bitarray [100];
        int fitness;
  
        individual (string);

        friend ostream &operator<<(ostream &stream, individual ob);
    
        string genBitstring()
        {
            string temp;
            srand(time(NULL));
            int i;
            for(int i = 0; i < 99; i++)
            {
                temp += (rand() % 1);
            }
            return temp;
        }
    
        float genFitness()
        {
            float count;
            for (int i = 0; i < 99; i++)
            {
                if (bitarray[i] == 1)
                {
                    count++;
                }
            }
            return count;
        }
};

individual::individual (string bitarray = "")
{
    if (bitarray == "")
    {
        bitarray = genBitstring();
    }
    fitness = genFitness();
}

ostream &operator<<(ostream &stream, individual ob)
{
    stream << "Bitstring: " << ob.bitarray << "\nFitness: " << ob.fitness << "\n\n";
    return stream;
}


/* Main */
int main()
{
individual ind1;
cout << ind1;

return 0;
}
