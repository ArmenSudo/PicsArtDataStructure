"""
	Վարժություն 1.8
		n = ((m / (n ** 2)) + (2 * n)) / 3
		Այս բանաձևով ստեղծեք ֆունկցիա, որը հաշվում է թվի խորանարդ արմատը։
"""


def third_sqrt(n):
	res = 1
	while not guess_enough(res, n):
		res = improve(res, n)
	return res


def guess_enough(x, y):
	if abs(x ** 3 - y) < 0.0000000001:
		return True
	else:
		return False


def improve(n, m):
	return ((m / n ** 2) + (2 * n)) / 3


print(third_sqrt(10))
