# import matlab.engine
# eng = matlab.engine.start_matlab()

import matlab.engine
# import numpy as np
# data1 = np.random.uniform(low = 0.0, high = 30000.0, size = (1000000,))
# data1m = matlab.double(list(data1))

# print("Numpy:", data1)
# print("Matlab:", data1m)

import timeit

def setup_func(low):
    import matlab.engine
    import numpy as np
    data1 = np.random.uniform(low = low, high = 30000.0, size = (1000000,))
    # return matlab.double(list(data1))
    return matlab.double(data1)

low = 0
# setup_script = ("import matlab.engine\n"
#                 "import numpy as np\n"
#                 "data1 = np.random.uniform(low = 0.0, high = 30000.0, size = (1000000,))\n"
#                 "data1m = matlab.double(list(data1))\n")

print(timeit.timeit('setup_func', globals=globals(), number=1000000))