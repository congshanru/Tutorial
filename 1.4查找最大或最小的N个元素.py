import heapq


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(max(nums))
print(heapq.nlargest(3, nums))  # Prints [42, 37, 23]
print(min(nums))
print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]


portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)  # [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]
print(heapq.heappop(heap))


# ��Ҫ���ҵ�Ԫ�ظ�����ԱȽ�С��ʱ�򣬺��� nlargest() �� nsmallest() �Ǻܺ��ʵġ�
# �������������Ψһ����С�����N=1����Ԫ�صĻ�����ôʹ�� min() �� max() ���������Щ��
# ���Ƶģ���� N �Ĵ�С�ͼ��ϴ�С�ӽ���ʱ��
# ͨ���������������Ȼ����ʹ����Ƭ���������� �� sorted(items)[:N] ������ sorted(items)[-N:] ����

