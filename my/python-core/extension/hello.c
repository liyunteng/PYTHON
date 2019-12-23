/*
 * hello.c - hello
 *
 * Date   : 2019/12/21
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum Sex {
   Man,
   Woman
};

typedef struct  _test_t {
  int id;
  char name[128];
  enum Sex sex;
  struct _test_t *next;
} test_t;

int hello()
{
  printf("Hello world!\n");
  return 0;
}

int fac(int n)
{
  if (n < 2)
    return n;
  return n * fac(n-1);
}

/* argument */
int test(int a, float b, char *c)
{
  printf("a=%d\n", a);
  printf("b=%f\n", b);
  printf("c=%s\n", c);
  return 100;
}

/* struct */
static test_t *g_test = NULL;
int setTest(test_t *test)
{
    if (g_test != NULL) {
        free(g_test);
    }
    g_test = (test_t *)malloc(sizeof(test_t));
    if (g_test != NULL) {
        memcpy(g_test, test, sizeof(*g_test));
        printf("t->id=%d\n", g_test->id);
        printf("t->sex=%d\n", g_test->sex);
        printf("t->name=%s\n", g_test->name);
        return 0;
    }
    return -1;
}
test_t *getTest(int id)
{
    if (g_test == NULL)
        return NULL;
    if (g_test->id == id)
        return g_test;
    return NULL;
}

/* callback */
typedef int (*fn)(int, int);
static fn fns[10];
int register_callback(fn f)
{
    for (int i = 0; i < 10; i++) {
        if (fns[i] == NULL) {
            fns[i] = f;
            return i;
        }
    }
    return -1;
}

void run_callback()
{
    for (int i = 0; i < 10; i++) {
        if (fns[i] != NULL) {
            printf("%d\n", fns[i](i, i));
        }
    }
}

/* struct + callback */
struct callback_all {
    int (*callback1)(int);
    int (*callback2)(int);
    int (*callback3)(int);
};

int run_callback_all(struct callback_all fs)
{
    printf("callback1: %d\n", fs.callback1(1));
    printf("callback2: %d\n", fs.callback2(2));
    printf("callback3: %d\n", fs.callback3(3));
    return 0;
}

int main(void)
{
  printf("4! = %d\n", fac(4));
  printf("8! = %d\n", fac(8));

  return 0;
}


/* Local Variables: */
/* compile-command: "gcc -Wall hello.c -fPIC -shared -o libhello.so" */
/* End: */
