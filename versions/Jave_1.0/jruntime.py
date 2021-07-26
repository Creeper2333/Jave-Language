import jexceptions as jex
import jbuiltins
import jvariables as jv
import os,sys

#关键字:"|"及"&"，严禁使用否则干扰运行
#我tm有什么办法？？
class jruntime():
    rtvarstack={}
    rtinputstream=[]
    rtoutputstream=[]
    rtcodestack=[]

    def getopt(self,optname):
        opts={
            'j':jbuiltins.builtins.itself,#返回值自身，用于布尔值
            'j+':jbuiltins.builtins.plus,#加减乘除及求余数
            'j-':jbuiltins.builtins.minus,
            'j*':jbuiltins.builtins.times,
            'j/':jbuiltins.builtins.divide,
            'j%':jbuiltins.builtins.mod,
            'j>':jbuiltins.builtins.isbigger,#比大小
            'j<':jbuiltins.builtins.issmaller,
            'j=':jbuiltins.builtins.isequal,
            'j!=':jbuiltins.builtins.isnotequal,
            '!j':jbuiltins.builtins.boolnot,#布尔值运算
            'bor':jbuiltins.builtins.boolor,
            'band':jbuiltins.builtins.booland,
            'vstr':self.varsetter,#变量与常量定义
            'cstr':self.constsetter,
            'aostr':self.addostream,#往输出流中添加东西
            'rfostr':self.refreshostream,#将输出流中的东西显示
            'aistr':self.addistream,#往输入流中添加东西 ps:输入信息时的提示文本也会被放进输出流，这是有意为之
            'istram':self.istreamtoram,#取输入流最新的东西放入所谓的内存
            'vrdr':self.vareader,#读取变量
            'goto':self.gotoinstantly,#无条件goto
            'sclr':self.clearstack,#清空堆栈
            'rmvr':self.removeitem,#删除变量或常量
            'fi':self.fileinput,#文件io
            'fo':self.fileoutput,
            'exit':self.endinstantly#无条件终止程序
        }#内置的一些核心操作
        return opts.get(optname)

    def fileinput(self,fname,*arg):
        try:
            with open(fname,'r') as f:
                r=f.read()
                self.rtinputstream.append(r)
        except:
            self.rtinputstream.append('[empty file]')#读取文件，将数据写入输入流末尾
    def fileoutput(self,fname,*args):
        try:
            with open(fname,'w') as f:
                r=[]
                for i in self.rtoutputstream:#写入文件，将输出流中全部数据写入文件
                    r.append(str(i))
                f.writelines(r)
        except:
            ex=jex.jrexceptions.FileIOException()
    def mandatorytypeconvert(self,value,newtype):#强制类型转换，用于输入数据。错误使用会导致 python 的异常，反正我也懒得管
        supported_types={
            "&i":int,
            "&f":float,
            "&s":str
        }
        
        try:
            converter=supported_types[newtype]
            return(converter(value))
        except:
            #print(value,newtype)
            ex=jex.jrexceptions.TypeConvertFailure()
            #return value
    def clearstack(self,stackname,*args):#清空指定堆栈
        stacks={
            'var':self.rtvarstack,
            'input':self.rtinputstream,
            'output':self.rtoutputstream
        }
        stacks[stackname].clear()
    def removeitem(self,varname,*args):#删除一个指定名称的变量或常量
        self.rtvarstack.pop(varname)
    
    def __init__(self,srcpath):
        try:
            with open(srcpath,'r') as f:
                self.rtcodestack=f.readlines()
                f.close()
        except:
            print('runtime error: cannot find target file or the file contains unsupported characters.')
    def endinstantly(self,exitcode=0,*args):
        sys.exit(exitcode)
    def gotoinstantly(self,*args):return False#无条件goto
    def postprocess(self,i,*args):
        containsvar=True
        if('??' in i):
            containsvar=False
            i=i.replace('??','?')
        try:
            if('&i' in i):
                v=int(i.replace('&i',''))#避免输入数值比大小时奇妙崩溃(指定输入的是数值需要在数字前或后加入强制类型转换符&i或&f)
                return v
            else:
                if('&f' in i):
                    v=float(i.replace('&f',''))
                    return v
                else:
                    v=i
        except:
                v=i
        if('?' in v and containsvar==True):
            v=self.vareader(i.replace('?',''))
        return v
    def varsetter(self,varname,value,*args):

        var=jv.JaveVariables.variables(varname,value)
        self.rtvarstack[varname]=var
        #print(varname)

    def constsetter(self,constname,value,*args):
        if(self.rtvarstack.get(constname)!=None):
            raise jex.jrexceptions.TryEditConstantException()
        const=jv.JaveVariables.variables(constname,value,isconstant=True)
        self.rtvarstack[constname]=const

    def addostream(self,value,*args): #编译后的变量名表示必须带"?"标识符
        v=str(value)
        if('?' in v):
            v=self.vareader(value.replace('?',''))
        self.rtoutputstream.append(v)

    def refreshostream(self,*args):
        a=os.system(r'cls')
        for t in self.rtoutputstream:
            print(t)
            
    def addistream(self,typeconvert,prompt='',*args):
        i=input(prompt).replace('\n','')
        #print(i)
        i_tgt=self.mandatorytypeconvert(i,typeconvert)#强制转换类型
        self.rtinputstream.append(i_tgt)
        self.rtoutputstream.append(prompt+i)
    def istreamtoram(self,varname,*args):
        self.varsetter(varname,
        self.rtinputstream[len(self.rtinputstream)-1]
        )
    
    def vareader(self,varname):
        try:
            return(self.rtvarstack.get(varname).getvalue())
        except:
            raise(jex.jrexceptions.VarNotFoundException(varname))

    def start(self,*startarguments):
        executioncount=0
        maxcount=len(self.rtcodestack)
        #print(self.rtcodestack[executioncount])
        while executioncount < maxcount:
            code=self.rtcodestack[executioncount].replace('\n','')
            args=code.split('|')
            optname=args[0]
            tgt=int(args[3])
            opt=self.getopt(optname)
            usinggotoflag=opt(self.postprocess(args[1]),self.postprocess(args[2]))
            
            executioncount_tmp=executioncount
            if(usinggotoflag==None):
                executioncount=tgt-1
                if(tgt==-1):
                    executioncount_tmp+=1#这里是在返回值为空的情况下，
                    executioncount=executioncount_tmp#若目标行为-1则默认跳转至下一行
            else:
                if(usinggotoflag):
                    executioncount+=1
                if(not usinggotoflag):
                    executioncount=tgt-1#这一段用于比较快捷地实现比大小结果为false后的跳转
            if(type(usinggotoflag)==int or type(usinggotoflag)==float):
                self.rtinputstream.append(usinggotoflag)#加减运算结果放入输入流末尾，懒得再弄别的花里胡哨的玩意了
                executioncount=tgt-1
            #print(code,executioncount)
            #print(args[1],args[2])
if __name__=='__main__':#自己定义的变量就不能含中文，用户输入的玩意就可以带中文，离谱
    try:
        fname=input('输入需要运行的程序文件名：')
        #fname='calc.jave'
        runtime=jruntime(fname)
        runtime.start()
    except:
        print('\nOriginal Jave Runtime Environment (Fake) by CreeperBlyat. Version 1.2. ')
        print('An error,which caused the program to be terminated, occured unexpectedly.')
        input('Press [Enter] to leave.')

#这只是个做出来好玩的东西
#所谓的“编译”只是个唬人的玩意，这玩意根本就不是什么把高级语言编译成什么机器语言的玩意
#所谓的变量都是一个我自制的 py 的类；所谓的内存和堆栈之类的更是扯淡，是一个字典和几个集合
#还有那个吊 IOStream，什么嘛，就是两个集合，还要手动刷新
#这就是个基于解释型语言 python 的解释型语言，所以运行速度是慢上加慢
#这个 Jave 的名字和 Java 没有关系，一点都没有
#这个名字来自一个梗，梗详见某位b站xxs的视频
#这个狗屁不通的所谓语言做出来就是为了折磨人的，嘻嘻
#have fun!! XD