import numpy as np
x = np.array([np.random.choice(np.arange(1,16),5),
               np.random.choice(np.arange(16,31),5),
               np.random.choice(np.arange(31,46),5) ,
               np.random.choice(np.arange(46,61),5) ,
               np.random.choice(np.arange(61,76),5)
              ]).transpose()
print(x)