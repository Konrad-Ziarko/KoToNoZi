Discrepancies
===

Size of inline char
---
```c
// C
#include <stdio.h>

int main()
{
    printf("%d\n", sizeof('c')); // 4
    char c = 'c';
    printf("%d\n", sizeof(c)); // 1
    return 0;
}
```
```cpp
// CPP
#include <stdio.h>

int main()
{
    printf("%d\n", sizeof('c')); // 1
    char c = 'c';
    printf("%d\n", sizeof(c)); // 1
    return 0;
}
```

