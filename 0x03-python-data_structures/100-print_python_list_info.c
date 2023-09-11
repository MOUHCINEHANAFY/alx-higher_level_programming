#include <Python.h>

/**
 * print_python_list_info - This function print basic py info
 * @p: ThePyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int lenght;
	int container, idx;
	PyObject *obj;

	lenght = Py_SIZE(p);
	container = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", lenght);
	printf("[*] Allocated = %d\n", container);

	for (idx = 0; idx < lenght; idx++)
	{
		printf("Element %d: ", idx);
		obj = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
