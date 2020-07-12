a="asdfggjytehtrwgrevreqf"
print(len(a))

b='123456'
#连接字符串,用‘+’号；
print(a+b)

#python不允许在+表达式中出现其他类型；

#字符串转换
age=33
print(int(age))
print(len(str(age)))
print(float(age))

#字符串和列表的转换
#list()方法用于将元祖或字符串转换为列表(重点)
string='Hello,world!!'
l=list(string)
print(l)
#元祖转化为列表
uname=('laozhang','zhangbinghui','binghui')
listu=list(uname)
print("列表元素：",listu)

#join()方法用于将序列中的元素以指定的字符串连接生产一个新的字符串；
s='-'
ss=s.join(listu)
print(ss)

#replace()方法把字符串中的old字符串，替换成new字符串，如果指定第三个参max，则替换不超过max次

#str.replace(old,new[,max])

str="this is string example... owe,this is really string!!"
print(str.replace('is','was'));
print(str.replace('is','was',3));


name="zhangbinghui"
print(name[0])
print(name[-1])
#不含上边界（重点）
print(name[1:5])
print(len(name))
print(name[1:10:2])
#s[a:b:-2] 步长为负数，两个边界意义反转了，表示从b+1到a,步长-2
print(name[10:1:-2])


#字符串内建函数
print(name.capitalize())#第一个字符大写
print(name.title())
print(name.upper())
print(name.lower())
#center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
#原字符居中，空格填充至width长度
#返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。
print(name.center(30,'*'))
#Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
#str.count(sub, start= 0,end=len(string))
print(name.count('i',0,12))
print(name.count('i'))
#decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
bianma="张冰辉"
name1=bianma.encode('utf-8')
print(name1)
print(bianma.encode('GBK','strict'))
"""str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
 
print(str)
 
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
 
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))"""

"""endswith() 方法用于判断字符串是否以指定后缀结尾，
如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置"""
#str.endswith(suffix[, start[, end]])
print(name.endswith('hui'))
print(name.endswith('zhagn'))
print(name.endswith('hui',3,5))
print(name.endswith('hui',0,12))

print("aaaaaaaaaaaaaa")
print(name.startswith('zhang'))
print('\n')

#expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
name1="zhang\tbing\thui"
print(name)
print(name1.expandtabs())
print(name1.expandtabs(12))
"""find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 
和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，
返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。"""

print(name.find('bing'))
print(name.find('bing',0,len(name)))
print(name.find('zhagn'))
"""index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。"""

"""isalnum() 方法检测字符串是否由字母和数字组成"""
"""如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False"""
print(name.isalnum())
print(bianma.isalnum())
bm="www.baidu.com"
print(bm.isalnum())
print('\n')

"""
Python isalpha() 方法检测字符串是否只由字母组成。
如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
"""
daima="abc123"
print(daima.isalnum())
print(daima.isalpha())
print('\n')

"""
ljust() 方法返回一个原字符串左对齐,
并使用空格填充至指定长度的新字符串。
如果指定的长度小于原字符串的长度则返回原字符串。
返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。
如果指定的长度小于原字符串的长度则返回原字符串。
"""
print(name.ljust(30,'.'))
print(name.ljust(30,'*'))
print(name.center(30,'*'))
print('\n')
"""
lstrip([chars]) 方法用于截掉字符串左边的空格或指定字符。
chars --指定截取的字符。
"""
str1="   zhangbinghui"
print(len(str1))
print(str1.lstrip())
print(len(str1.lstrip()))
str2='22222222zhangbinghui'
print(str2.lstrip('2'))

"""
partition() 方法用来根据指定的分隔符将字符串进行分割。

如果字符串包含指定的分隔符，则返回一个3元的元组，
第一个为分隔符左边的子串，
第二个为分隔符本身，第三个为分隔符右边的子串
"""
a2='www.baidu.com'
print(a2.partition('.'))
"""
Python split() 通过指定分隔符对字符串进行切片，
如果参数 num 有指定值，则分隔 num+1 个子字符串
str.split(str="", num=string.count(str)).
num -- 分割次数。默认为 -1, 即分隔所有。
"""
print(a2.split('.'))
a3='q.w.e.r.t.y.u.i.4.5.6'
a4=a3.split('.')
print(a4)
print(list(a4))
a5='qwtaqtadtlllt'
print(a5.split('t'))
print('\n')

"""
Python splitlines() 按照行('\r', '\r\n', \n')分隔，
返回一个包含各行作为元素的列表，如果参数 keepends 为 False，
不包含换行符，如果为 True，则保留换行符。
str.splitlines([keepends])
keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，
默认为 False，不包含换行符，如果为 True，则保留换行符。
"""
atr='ab c\n\nde fg\rkl\r\n'
print(atr.splitlines())
print(atr.splitlines(True))

"""
Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。
注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
str.strip([chars]);
"""
str3='*****zhangbing*hui******'
print(str3.strip('*'))
#swapcase() 方法用于对字符串的大小写字母进行转换。
str5='ZHANGbingHUI'
print(str5.swapcase())

"""
Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
width -- 指定字符串的长度。原字符串右对齐，前面填充0。
"""
print(name.zfill(30))
print(name.zfill(20))

print(name,'%o')
print(name,'%s')


























