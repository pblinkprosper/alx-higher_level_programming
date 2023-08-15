#include <stdio.h>
#include <stdlib.h>
#include <Python.h>

/**
 * print_python_list_info - function that prints a python list info
 * @p: parameter for PyObject
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	size_t size, i;
	PyObject *obj;
	PyListObject *list;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
