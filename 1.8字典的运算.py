# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys())) # min_price is (10.75, 'FB')
max_price = max(zip(prices.values(), prices.keys())) # max_price is (612.78, 'AAPL')
print(min_price, max_price)

# 类似的，可以使用 zip() 和 sorted() 函数来排列字典数据：
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# 执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。 比如，下面的代码就会产生错误：
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence


print(min(prices, key=lambda k: prices[k])) # Returns 'FB'
print(max(prices, key=lambda k: prices[k])) # Returns 'AAPL'
# 如果还想要得到最小值，你又得执行一次查找操作。比如：
min_value = prices[min(prices, key=lambda k: prices[k])]
print(min_price)
