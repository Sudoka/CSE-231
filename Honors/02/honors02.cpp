// GA Project 02
// Create a population of bitstrings and evaluates fitness

/* Algorithm */
/*
100 individuals
    Array of individual()
For each individual
    Print
*/

/* Includes */
#include <iostream>
#include <stdlib.h>
#include <string>
#include <sys/time.h>

/* Using */
using namespace std;

/* Classes */
class individual{
    public:
        string bitstring;
        int fitness;

        individual();

        friend ostream &operator<<(ostream &stream, individual ob);

        string genBitstring(){
            string temp;
            for(int i = 0; i < 100; i++){
                int rChar = (rand() % 2);
                if (rChar == 0){
                    temp += "0";
                }
                else if (rChar == 1){
                    temp += "1";
                }
            }
            return temp;
        }

        int genFitness(){
            int count = 0;
            for (int i = 0; i < bitstring.length(); i++){
                if (bitstring[i] == '1'){
                    count++;
                }
            }
            return count;
        }
};

individual::individual(){
    bitstring = genBitstring();
    fitness = genFitness();
}

ostream &operator<<(ostream &stream, individual ob){
    stream << "Bitstring: " << ob.bitstring << "\nFitness: " << ob.fitness << "\n\n";
    return stream;
}


/* Main */
int main(){
    //Seed RNG
    timeval t1;// To seed rand()
    gettimeofday(&t1, NULL);// Microsecond resolution
    srand(t1.tv_usec * t1.tv_sec);
    individual population [100];
    for (int i = 0; i < 100; i++){
        population[i] = individual();
    }
    for (int i = 0; i < 100; i++){
        cout << population[i] << endl;
    }

    return 0;
}
