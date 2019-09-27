Reference
===

Variable
---
C++ as superset of C does allow to make variables and pointers.  
Reference, introduced in C++, does allow to make alias to original variable. 
```cpp
int originalVal = 42;
int& reference = originalVal;
++reference;
std::cout << originalVa; // 43
```
Reference works as hard link to same memory address, that is way modifying reference changes original - reference IS the original variable but has different name.

Function
---
In case of passing by value we always pass copy of original variable - even if it is a pointer.  
Existence of reference does allow to make new operation - passing parameters by reference.  
Passing by reference does allow to modify original without pointers.
```cpp
void modCopy(int val){
    ++val;
}
void modRef(int& val){
    ++val;
}
int original = 42;
modCopy(original);
std::cout << original; // 42
modRef(original);
std::cout << original; // 43
```
