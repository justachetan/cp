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

- ```push\_back()``` appends to end. 
- ```insert()``` inserts at an index specified.
- When passed to a function, a copy of the vector is passed.

```

void foo(vector<int> v) {
	// This creates many copies

}

void smart\_foo(const vector<int>& v){
	// Reference will be passed
}

void edit\_foo(vector<int>& v){
	v[i]++;
}
```


