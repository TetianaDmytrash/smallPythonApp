# Write a Python program to print all the elements of an Array using the position of the elements.

import array as arr

# variable_name = array(typecode,[elements]) - если есть элементы
# variable_name = array(typecode) - если пустой массив нужен
# array_name[index_value_of_item]

# typecode
# 'b' - signed char | 'B' - unsigned char | 'u' - wchar_t
# 'h' - signed short | 'H' - unsigned short | 'i' - signed int
# 'I' - unsigned int | 'l' - signed long | 'L' - unsigned long
# 'q' - signed long long | 'Q' - unsigned long long | 'f' - float
# 'd' - double
arr_example = arr.array('i', [10,20,30])

print(f'array length: {len(arr_example)}')
print(f'view array: ')
for el in arr_example:
	print(el, end=' || ')

print(f'\n\nadd elements 40, 50, 60')
arr_example.append(40)
arr_example.append(50)
arr_example.append(60)

print(f'new array length: {len(arr_example)}')
print(f'view array: ')
for i in range(len(arr_example)):
	print(arr_example[i])

# search for the index of the value 10
#will return the index number of the first instance of the value 10
print(f'\nfind element`s (30) index: {arr_example.index(30)}')

print(f'\nadd list of elements: [70,80,90]')
arr_example.extend([70,80,90])

print(f'new array length: {len(arr_example)}')
print(f'view array: ')
for i in range(len(arr_example)):
	print(arr_example[i], end=' ')

print(f'\n\nadd new element on 0 position')
arr_example.insert(0, 1500)

print(f'new array length: {len(arr_example)}')
print(f'view array: ')
for el in arr_example:
	print(el, end=' || ')

print(f'\n\ndelete element')
#remove the first instance of 10
arr_example.remove(10)
print(f'array length: {len(arr_example)}')
print(f'view array: ')
for el in arr_example:
	print(el, end=' ')

print(f'\n\nremove element with index 3')
arr_example.pop(3)
print(f'array length: {len(arr_example)}')
print(f'view array: ')
for el in arr_example:
	print(el, end=' ')