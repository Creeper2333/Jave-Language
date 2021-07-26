from os import name
import jexceptions as jex

class JaveVariables():
    class variables():
        #mystackid=-1
        myname=''
        myvalue=None
        isconstant=False
        isempty=False
        def __init__(self,name,value,isconstant=False):
            if (value==None):raise(jex.jrexceptions.ValueNotGivenException())
            try:
                if('&i' in value):
                    v=int(value.replace('&i',''))#避免输入数值比大小时奇妙崩溃(指定输入的是数值需要在数字前或后加入强制类型转换符&i或&f)
                else:
                    if('&f' in value):
                        v=float(value.replace('&f',''))
                    else:
                        if('&s' in value):
                            v=str(value.replace('&s',''))
                        else:
                            v=value
            except:
                v=value
            #self.mystackid=stackid
            self.myname=name
            self.myvalue=v
            self.isconstant=isconstant
            
        def getvalue(self):
            return(self.myvalue)

        def setvalue(self,value):
            if(self.isconstant):raise(jex.jrexceptions.TryEditConstantException())
            if(type(value)!=type(self.myvalue)):raise(jex.jrexceptions.TypeErrorException())
            self.myvalue=value
    
