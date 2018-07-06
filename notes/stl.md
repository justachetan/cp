# Powerup C++ with STL

[Link](https://www.scribd.com/document/301689406/Power-up-C-with-the-Standard-Template-Library-Part-1-topcoder)

## Vector 
- General info

    - Header: ```#include <vector>```
    - Have to use: ```using namespace std;```

- Declaration

```
vector<int> N;

vector< vector<int> > N
```

- Initialisation

```
vector<int> v1;
//...
vector<int> v2 = v1;
vector<int> v3(v1);

// v2 and v3 produce exactly the same results

vector<int> v4(1000); // For specific size

vector<string> v5(20, "unknown"); // initialise with "unknown"

vector< vector<int> > A; // 2-D array (mind the spaces)

```

- ```push_back()``` appends to end. 
- ```insert()``` inserts at an index specified.
- When passed to a function, a copy of the vector is passed.

```

void foo(vector<int> v) {
	// This creates many copies

}

void smart_foo(const vector<int>& v){
	// Reference will be passed
} 
void edit_foo(vector<int>& v){
	v[i]++;
}
```

## Pair

- A template class in C++
- Has just two numbers
- Compares first to second
- Pair comparison is like Python tuples


## Iterators

- ```swap(a, b)``` is a standard STL function
- ```c.begin()``` pointer to the first element
- ```c.end()``` pointer to the first **invalid** element
- Code sample for traversal using iterator:

```
for(vector<int>::iterator it = v.begin(); it != v.end(); it++) {

	*it++; // Increments the value that the iterator points to

}

vector<int>::iterator it; // To declare the iterator for vector
```

- ```const_iterator```
- ```reverse_iterator```

# Algorithms in STL

- ```#include <algorithm>```
- ```reverse()```
- ```find()``` : have to substract ```c.begin()``` from the result
- ```max_element()``` : return an iterator (pointer) to the respective element. Use: ```*max_element()```

- ```min_element()```

- Useful macro:

	```#define all(c) c.begin(), c.end()```
- ```sort()```:

```
sort(v.begin(), v.end());
sort(all(v));
sort(X.rbegin(), X.rend()); // sort array in descending order using with reverse item

```

- ```typeof(<expression>)``` : is replaced by type of the expression in the brackets at compile time

```

// USEFUL MACRO

#define tr(container, it) \
	for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)

void f(const vector<int> &v){
	int r = 0;
	tr(v, it) {
		r+=(*it)*(*it);
	}
	return r;
}

```

# Data Manipulation in vectors

- ```insert(i, 42)```: insert 42 after the index i
















