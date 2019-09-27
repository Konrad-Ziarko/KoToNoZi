Virtual keyword
===

Virtual function
---
Virtual functions are used in polymorphism in C++.  
They allow to overload functions in runtime.

Virtual keyword makes function bind in runtime so pointer of a base class type can be used to access derived class members.  
Without virtual keyword base class pointer will be bind in compile time and will allways point to base class members.  

```cpp
struct Base1{
  void print1(){std::cout<<"Base1";};
};
struct Base2{
  virtual void print2(){std::cout<<"Base2";};
};
struct Derived : Base1, Base2{
  void print1(){std::cout<<"Derived";};
  void print2(){std::cout<<"Derived";};
};

Base1* p1 = new Derived();
Base2* p2 = (Base2*)p1;
p1->print1(); // prints "Base1"
p2->print2(); // prints "Derived"
```

>Constructors cannot be virtual  
>Static members cannot be virtual  
>Friend function cannot be virtual

Virtual inheritance
---
Virtual inheritance allows to inherit from the same base class more than once.
It can be required when derived class multiple inherits from classes that share same base class.
