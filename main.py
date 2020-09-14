import timeit

print("Python converted to C++ t(s)",timeit.timeit(setup="import iterate", stmt="iterate.iterate()", number=10000))
print("Pure Python t(s): ",timeit.timeit(setup="import iterate1", stmt="iterate1.iterate1()", number=10000))

