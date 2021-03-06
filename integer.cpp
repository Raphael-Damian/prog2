
//integer.cpp
//Student: Raphaël Ashruf
//Mail: raphael-damian.ashruf.3037@student.uu.se
//Reviewed by: Niklas Wik
//Date reviewed: 18-10-2021 (18 Oktober 2021)
#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		void set(int);
		int fib();
	private:
		int val;
		int _fib(int);
	};
 
Integer::Integer(int n){
	val = n;
	}
 
int Integer::get(){
	return val;
	}
 
void Integer::set(int n){
	val = n;
	}

int Integer::fib(){
	return _fib(val);
	}

int Integer::_fib(int n){
	if ( (n == 1) || (n == 0) ){
		return n; //base  case
	} else{
		return (_fib(n-1) + _fib(n-2));
	}
	}  

extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	int Integer_fib(Integer* integer) {return integer->fib();}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
