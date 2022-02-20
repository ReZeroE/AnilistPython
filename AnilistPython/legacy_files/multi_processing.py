import multiprocessing
import time
import random
import os

class A(object):
    def __init__(self, *args, **kwargs):
        # do other stuff
        pass

    def do_something(self, i):

        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test.txt'), 'a', encoding='utf-8') as f:
            f.write(f'{i}\n')

        print('Process Complete')

    def run(self):
        processes = []

        for i in range(20):
            p = multiprocessing.Process(target=self.do_something, args=(i,))
            processes.append(p)

        [x.start() for x in processes]
        [x.join() for x in processes]


if __name__ == '__main__':
    start = time.time()
    a = A()
    a.run()
    print(time.time() - start)
    