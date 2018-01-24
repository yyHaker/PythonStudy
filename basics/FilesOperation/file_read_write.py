# -*- coding: utf-8 -*-
"""
reference:
[1]python 文件读写时用open还是codecs.open: https://www.cnblogs.com/weapon-liu/p/7989049.html
[2]python文件操作：https://www.cnblogs.com/rollenholt/archive/2012/04/23/2466179.html
[3]python使用codecs模块进行文件操作-读写中英文字符:http://blog.csdn.net/chenyxh2005/article/details/72465758
"""
import codecs
"""
open打开文件, 只能写入str类型, 不管字符串是什么编码方式
"""
fr = open('test.txt', 'a')  # a  以追加模式打开 (从 EOF 开始, 必要时创建新文件)
line1 = "wsdsd"
line2 = "我爱python"
line3 = u"8989我爱python"
fr.write(line1)
fr.write(line2)
fr.write(line3)

"""
use codecs to write file
"""
fw = codecs.open('text2.txt', 'a', encoding='utf-8')
fw.write(line1)
fw.write(line2)
fw.write(line3)

"""
小结：相比于open(), codecs这种方法可以指定一个编码打开文件，使用这个
方法打开的文件读取返回的将是unicode。写入时，如果参数 是unicode，则使
用open()时指定的编码进行编码后写入；如果是str，则先根据源代码文件声明
的字符编码，解码成unicode后再进行前述 操作。相对内置的open()来说，
这个方法比较不容易在编码上出现问题。
"""

