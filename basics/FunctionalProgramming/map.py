# 利用map()函数，把用户输入的不规范的英文名字，
# 变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# METHOD 1
def normalize(name):
    def fn(a):
        return a[:1].upper()+a[1:].lower()
    return map(fn, name)
print(list(normalize(['adam', 'LISA', 'barT'])))

# method 2   normalize2()函数把一个名字的首字母变为大写，其他的变为小写
def normalize2(name):
    return name[:1].upper()+name[1:].lower()
L1=['adam', 'LISA' ,'barT']
L2=list(map(normalize2,L1))
print(L2)
