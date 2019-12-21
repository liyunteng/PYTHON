/*
 * hello.c - hello
 *
 * Date   : 2019/12/21
 */
#include <stdio.h>
#include <string.h>
#include <python3.8/Python.h>


int hello(void)
{
    printf("hello world!\n");
    return 0;
}

int fac(int n)
{
    if (n < 2) {
        return 1;
    }
    return (n)*fac(n-1);
}

char *reverse(char *s)
{
    register char t, *p = s, *q = (s+(strlen(s)-1));
    while (p < q) {
        t = *p;
        *p++ = *q;
        *q-- = t;
    }
    return s;
}

int main(void)
{
    hello();
    char s[BUFSIZ];
    printf("4! == %d\n", fac(4));
    printf("8! == %d\n", fac(8));
    strcpy(s, "abcdef");
    printf("revers 'abcdef', we get '%s'\n", reverse(s));
    return 0;
}

static PyObject *
Extest_fac(PyObject *self, PyObject *args)
{
    int num;
    if (!PyArg_ParseTuple(args, "i", &num))
        return NULL;
    return (PyObject *)Py_BuildValue("i", fac(num));
}

static PyObject *
Extest_reverse(PyObject *self, PyObject *args)
{
    char *ori_str;
    char *dup_str;
    PyObject *retval;
    if (!PyArg_ParseTuple(args, "s", &ori_str))
        return NULL;

    retval = (PyObject *)Py_BuildValue("ss", ori_str,
                                       dup_str=reverse(strdup(ori_str)));
    free(dup_str);
    return retval;
}
static struct PyMethodDef methods[] =
{
    {"fac", (PyCFunction)Extest_fac, METH_VARARGS, "fac"},
    {"reverse", (PyCFunction)Extest_reverse, METH_VARARGS, "reverse"},
    {NULL, NULL, 0, NULL}
};
static struct PyModuleDef Extest =
{
    PyModuleDef_HEAD_INIT,
    "Extest",
    "",
    -1,
    methods
};
PyMODINIT_FUNC PyInit_Extest(void)
{
    return PyModule_Create(&Extest);
}

/* Local Variables: */
/* compile-command: "clang -Wall -o hello hello.c -c -I/usr/include/python3.8" */
/* End: */
