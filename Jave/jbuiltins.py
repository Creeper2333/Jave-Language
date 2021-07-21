import jexceptions as jex
import jvariables as jv
import os

class builtins:
    def __init__(self) -> None:
        pass
    def itself(operand1,*arg):
        return operand1
    def isbigger(operand1,operand2):
        return(operand1>operand2)
    def issmaller(operand1,operand2):
        return (operand1<operand2)
    def isequal(operand1,operand2):
        return(operand1==operand2)
    def isnotequal(operand1,operand2):
        return(operand1!=operand2)
    def isbiggerbandequal(self,operand1,operand2):
        return(self.isbigger(operand1,operand2) or self.isequal(operand1,operand2))
    def issmallerandequal(self,operand1,operand2):
        return(self.issmaller(operand1,operand2) or self.isequal(operand1,operand2))
    def booland(operand1,operand2):
        if(type(operand1)!=bool or type(operand2)!=bool):
            raise(jex.jrexceptions.TypeErrorException(type(operand1),bool))
        return (operand1 and operand2)
    def boolor(operand1,operand2):
        if(type(operand1)!=bool or type(operand2)!=bool):
            raise(jex.jrexceptions.TypeErrorException(type(operand1),bool))
        return (operand1 or operand2)
    def boolnot(operand1,*arg):
        if(type(operand1)!=bool):
            raise(jex.jrexceptions.TypeErrorException(type(operand1),bool))
        return (not operand1)

    def plus(operand1,operand2):
        return operand1+operand2
    def minus(operand1,operand2):
        return operand1-operand2
    def times(operand1,operand2):
        return operand1*operand2
    def divide(operand1,operand2):
        return operand1/operand2
    def mod(operand1,operand2):
        return operand1%operand2

    