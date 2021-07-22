# Jave 语言伪教程
## 变量与常量（Variables and constants）
### 变量的定义方法
一般写法：
```
vstr|<varname>|<value>[type converter]|<goto>
```
以下代码定义了一个名为`var_a`的变量，这个变量的内容是一串文本:
```
vstr|var_a|damedane|2
```
如果要指定一个数字变量，可以用以下方法：
```
vstr|var_b|11451&i|2
vstr|var_c|1919.81&f|2
```
其中，`var_b`是一个 int 类型变量，`var_c`是一个 float 类型变量

当然，定义一个长得像数字的字符串变量可以用如下方法确保不会出现歧义：
```
vstr|var_d|1145141919&s|2
```

### 常量的定义方法

一般写法
```
cstr|<constname>|<value>[type converter]|<goto>
```
与变量定义格式基本类似，但是指令由`vstr`变为`cstr`。如下：
```
cstr|PI|3.14159&f|2
```
 _PS: 其实名字大不大写都一样，你变量名带空格或用一些在其它语言中不让用的字符其实都没事，当然为了标准化和减少我的工作量我不建议你这样做 ——来自沙雕作者_ 

需要注意的是，一个程序里只能出现一次常量定义，且不能修改常量，否则会发生`TryEditConstantException`异常

以下的程序虽然可以启动，但是中途会暴毙：
```
vstr|var_a|damedane|2
cstr|con_a|mistake|1
```
这里是一个循环，但是这个循环在进行到第二次的时候会崩溃，因为这里试图修改一个已经存在的常量`con_a`

### 删除变量
删除变量有助于节省内存，当然这个软件已经很占内存了所以这么做就是杯水车薪

使用`rmvr`删除变量或常量。

一般写法：
```
rmvr|<varname>|[optional]|<goto>
```
如：
```
vstr|var123|blyat|2
rmvr|var123||3
exit|0||0
```
## 输入/输出流（I/O Stream）

### 输出流
`aostr` 指令被用来往输出流中添加东西，变量、文本、数字都可

`rfostr` 指令将输出流中的东西添加到屏幕上

一般写法如下：
```
aostr|<info>|[optional]|<goto>
rfostr|[optional]|[optional]|<goto>
```

以下代码在屏幕上显示如下内容：hello world!
```
aostr|hello world!&s|0|2
rfostr|0|0|3
```
运行示例：
```
hello world!
````
### 输入流
`aistr`指令用于获取用户输入暂存

`istram`指令取输入流中 **最后的** 一次输入赋给名为`<varname>`的变量

一般写法如下：
```
aistr|<type converter>|[optional:input prompt]|<goto>
istram|<varname>|[optional]|<goto>
```
以下代码取用户输入的内容，并将其输出一遍：
```
aistr|&s|input:prompt>>|2
istram|var_tmp|0|3
aostr|?var_tmp|0|4
rfostr|0|0|5
exit|0||0
```
运行示例：
```
input:prompt>> rnm，退钱！
rnm，退钱！
```
 _PS：算术运算的结果在运算完成后会追加在输入流的末尾，不要让它被覆盖，切记切记。_ 
### 清空输入/输出流
清空输入/输出流通过消耗可观的运算资源，节省几乎可以忽略的空间，十分划算。

另外，清空输出流可以实现清空屏幕输出的效果。
清空指令一般形式如下：
```
sclr|<stack name>|[optional]|<goto>
```
其中，`<stack name>` 可以为以下三种：
- input，输入流
- output，输出流
- var，变量和常量

以下代码显示一段文本，随即清屏，输出另一段文本：
```
aostr|hello world!&s|0|2
rfostr|0|0|3
sclr|output|0|4
rfostr|0|0|5
aostr|damedane~&s|0|6
rfostr|0|0|7
exit|0||0
```
运行实例：
```
hello world!
```
随即显示：
```
damedane~
```
 _PS：其实我这玩意是假的输入输出流。参见 jruntime.py。_ 
## 其它
### 强制终止程序
使用`exit`指令强制终止程序。
一般写法如下：
```
exit|[optional:exitcode]|[optional]|<(invalid) goto>
```
如：
```
exit|0||0
```
### 无条件goto
一般写法：
```
goto|[optional]|[optional]|<(invalid) goto>
```
 _PS：我不建议你用这个玩意，除非非用不可。_


## 致谢
### 哔哩哔哩的 [Soviet--1917](http://https://space.bilibili.com/445691468)（寥若星辰吖）博士
感谢您杜撰出 Jave 这一「强大无比」的计算机语言，使我们可以使用繁琐度堪比汇编语言，资源占用还如此离谱的东西制作出一个又一个（虽然目前只有两个）又臭又长的程序。另外，感谢您可以编造出 MS Word IDE 这一伟大的工具。借助此工具，我们完全可以摆脱那些令人眼花缭乱的 IDE，只用一个 word 文档就完成所有项目的开发。所有！如果哪天我可以和您在b站进行深入♂交流，我将不胜感激。

——Jave 语言开发者本人，2021年七月

![寥若星辰](https://images.gitee.com/uploads/images/2021/0720/181652_32595246_7791515.png "“玉音放送”")

_寥若星辰吖博士对某位 IT 相关从业者进行单独授课_
