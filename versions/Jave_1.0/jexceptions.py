class jrexceptions():
    class ValueNotGivenException(Exception):
        description='[Debug]No value is given to define a variable or the value given is illegal.'
        def __init__(self,**args):
            print(self.description)
    class TypeErrorException(Exception):
        description=''
        def __init__(self,typefalse,typetrue):
            self.description='[Debug]Required var type is '+str(typetrue)+\
            ' but given type is type '+str(typefalse)
            print(self.description)
    class TryEditConstantException(Exception):
        description='[Debug]Cannot change the value of a constant'
        def __init__(self,*args):
            print(self.description)
    class TypeConvertFailure(Exception):
        description="[Debug]An error occured during the conversion process. \nCheck the convertibility of the given value."
        def __init__(self, *args):
            print(self.description)
    class VarNotFoundException(Exception):
        description='[Debug]No existing variable named *text*.'
        def __init__(self,varname, *args):
            print(self.description.replace('*text*',varname))
    class FileIOException(Exception):
        description='[Debug]File does not exist.'
        def __init__(self, *args):
            print(self.description)