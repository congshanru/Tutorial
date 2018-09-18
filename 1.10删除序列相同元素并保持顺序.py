# 怎样在一个序列上面保持元素顺序的同时消除重复的值？
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))  # [1, 5, 2, 9, 10]


# 这个方法仅仅在序列中元素为 hashable 的时候才管用。
# 如果你想消除元素不可哈希（比如 dict 类型）的序列中重复元素的话，你需要将上述代码稍微改变一下，就像这样：
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))  # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: d['x'])))  # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]

# 如果你仅仅就是想消除重复元素，通常可以简单的构造一个集合
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))  # {1, 2, 10, 5, 9}

# 使用了生成器函数让我们的函数更加通用，不仅仅是局限于列表处理。 比如，如果如果你想读取一个文件，消除重复行，你可以很容易像这样做：
# with open(r'somefile.txt','r') as f:
#     for line in dedupe(f):
#         ...


