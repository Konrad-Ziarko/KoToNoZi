Static
===

Structs/Classes
---
Keyword static makes members of a class available across all instances of that class.  
Static member are not members of a instance but rather a class it self.  

```
#include <stdio.h>

void mod(){
    static int a=5;
    ++a;
    printf("%d\n", a);
}

int main()
{
    int a=4;
    mod();
    mod();
    printf("%d\n", a);
    return 0;
    // output:
    //  6
    //  7
    //  4
}
```  