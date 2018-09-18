# 如果你的程序包含了大量无法直视的硬编码切片，并且你想清理一下代码。

######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(record[20:23], record[31:37], cost)


SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)


items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10,11]
print(items)
del items[a]
print(items)


a = slice(5, 50, 2)
print(a.start, a.stop, a.step)

# 通过调用切片的 indices(size) 方法将它映射到一个已知大小的序列上
# 这个方法返回一个三元组 (start, stop, step) ，所有的值都会被缩小，直到适合这个已知序列的边界为止。
# 这样，使用的时就不会出现 IndexError 异常。
print('-' * 20)
s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(i, s[i])
