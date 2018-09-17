# 如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？


# 排除掉第一个和最后一个分数求平均值
def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)


grades = [100, 90, 80, 70]
print(drop_first_last(grades))


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)


# *trailing_qtrs, current_qtr = sales_record
# trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)


# 星号表达式在迭代元素为可变长元组的序列时是很有用的
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir, sh)


# 有时候，你想解压一些元素后丢弃它们，你不能简单就使用 * ， 但是你可以使用一个普通的废弃名称，比如 _ 或者 ign （ignore）。
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record


# 一个列表， 很容易的将它分割成前后两部分
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(tail)


# 分割语法去巧妙的实现递归算法，由于语言层面的限制，递归并不是 Python 擅长的。 因此，最后那个递归演示仅仅是个好奇的探索罢了，对这个不要太认真了。
def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(sum(items))











