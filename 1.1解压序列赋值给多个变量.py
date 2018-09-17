# 现在有一个包含 N 个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给 N 个变量

s = 'Hello'
a, b, c, d, e = s
print(a)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, _, (year, *_) = data
print(shares, year)

