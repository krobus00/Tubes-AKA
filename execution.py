import timeit
def calulate(fname, start):
    stop = timeit.default_timer()
    execution_time = stop - start
    print("{} executed in {:f}".format(fname, execution_time))