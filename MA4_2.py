#!/usr/bin/env python3

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
	n = 35
	time_py = time.perf_counter()
	x = pfib(n)
	time_py2 = time.perf_counter()
	print("time python: ",time_py2-time_py)
	
	time_c1 = time.perf_counter()
	f = Integer(n)
	x = f.fib()
	time_c2 = time.perf_counter()
	print("time c++: ", time_c2-time_c1)
	
	n_list = [15,20,25]
	py_times = []
	cplusplus_times = []
	for i in n_list:
		t1 = time.perf_counter()
		f = Integer(i)
		f.fib()
		t2 = time.perf_counter()
		cplusplus_times.append(t2-t1)
		t3 = time.perf_counter()
		pfib(n)
		t4 = time.perf_counter()
		py_times.append(t4-t3)
	mp.plot(n_list, cplusplus_times)
	mp.plot(n_list, py_times)
	mp.savefig('plot_fibtimes.png')
if __name__ == '__main__':
	main()

