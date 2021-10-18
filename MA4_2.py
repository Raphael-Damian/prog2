#!/usr/bin/env python3:
""" MA4_2.py

Student: Raphaël Ashruf
Mail: raphael-damian.ashruf.3037@student.uu.se
Reviewed by: Niklas Wik
Date reviewed: 18-10-2021 (18 Oktober 2021)
""" 
import time
from integer import Integer
import matplotlib.pyplot as mp

def pfib(n):
	if n == 0 or n == 1:
		return n
	else:
		return pfib(n-1) + pfib(n-2)

def main():
	f = Integer(5)
	print(f.get())
	f.set(7)
	print(f.get())
	n = 5
	print(pfib(n)) #so python function works!
	#now we shall time it:
	n = 47
	f = Integer(n)
	x = f.fib()
	print("fib(47) = ", x)
	
	n_list = [30,35,40]
	py_times = []
	cplusplus_times = []
	for i in n_list:
		t1 = time.perf_counter()
		f = Integer(i)
		k = f.fib()
		t2 = time.perf_counter()
		cplusplus_times.append(t2-t1)
		t3 = time.perf_counter()
		j = pfib(i)
		t4 = time.perf_counter()
		py_times.append(t4-t3)
	mp.plot(n_list, cplusplus_times)
	mp.plot(n_list, py_times)
	mp.savefig('plot_fibtimes.png')
if __name__ == '__main__':
	main()

