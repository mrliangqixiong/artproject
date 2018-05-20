#!/usr/bin/env python  
# encoding: utf-8  

'''
有1、2、3、4个数字，
能组成多少个互不相同且无重复数字的三位数？都是多少？
'''
def cal_not_same():
	number_list=[]
	sum = 0
	result = []
	for i in range(1, 5, 1):
		for j in range(1, 5, 1):
			for k in range(1, 5, 1):
				if(i != j and j != k and i != k):
					result.append((i, j, k))

	return result

'''
费波那契数列是以递归的方法来定义
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F[n-1]+ F[n-2](n=>2)
'''
def digui_fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return digui_fib(n-1) + digui_fib(n-2)



def fibs(n):
	f0, f1 = 0, 1
	for _ in range(n):
		#f0, f1 = f1, f0+f1   #a=b, b=a+b  ||   b=a+b a=b
		f2 = f0 + f1
		f0 = f1
		f1 = f2

	return f0

'''
打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
'''
def test():
	for i in range(1,10):
		for j in range(0,10):
			for k in range(0,10):
				n = i*100+j*10+k
				if n == i**3+j**3+k**3:
					print(n)


if __name__ == "__main__":
	#result = cal_not_same()
	#print(result)
	# mlist = []
	# for i in range(0, 7):
	# 	mlist.append(fibs(i))
	# print(mlist)
	test()


