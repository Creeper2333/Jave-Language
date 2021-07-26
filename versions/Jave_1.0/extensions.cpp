#include <iostream>

using namespace std;

int VarSetter(int var,int len=1){
    int* varloc=(int*)malloc(sizeof(int)*len);
    *varloc=var;
    
    return PtrToInt(varloc);
}
int VarSetter(double var,int len=1){
    float* varloc=(float*)malloc(sizeof(double)*len);
    *varloc=var;

    return PtrToInt(varloc);
}
int VarSetter(char* var,int len=1){
    char* v=NULL;
    v=(char*)malloc(sizeof(char)*len);
    strcpy(v,var);
    free(var);

    return PtrToInt(v);
}

template <typename T>
T VarReader(T type,int varloc, bool ischar=False, int len=1){
    if(!ischar){
        T* ptr=IntToPtr(varloc);
        return *ptr
    }
    else{

    }
}

#include "dependencies/Python.h"

static int Ext_VSetter(PyObject* self, PyObject* args){
    PyArg_ParseTuple(arg,)
}

