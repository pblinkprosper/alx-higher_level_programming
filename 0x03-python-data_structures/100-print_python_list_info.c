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
	size_t size;
	size_t i;
	PyObject *obj;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zu\n", size);
	printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GET_ITEM(p, i);
		printf("Element %zu: %s\n", i, Py_TYPE(obj)->tp_name;
	}
}
