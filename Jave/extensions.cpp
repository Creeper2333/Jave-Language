#include "dependencies/Python.h"
#include <iostream>

using namespace std;
class JaveCppExtensions{
    public:
    void *ram=nullptr;

    void RamLengthInit(int len){
    ram=malloc(len);
}
};
