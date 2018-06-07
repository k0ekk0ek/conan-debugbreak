#include <stdio.h>

#include "debugbreak.h"

#ifdef _WIN32
# define EXPORT __declspec(dllexport)
#else
# define EXPORT
#endif

EXPORT int main(void)
{
    printf("Hello World! from test_package.c\n");
    return 0;
}
