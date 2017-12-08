from gevent import monkey
monkey.patch_all(thread=False)
import random
import time
import multiprocessing.pool
import gevent
# import urllib2

def delay_print(t):
    time.sleep(t)
    print(t)

def main():
    pool = multiprocessing.pool.Pool()
    rng = random.Random()
    rng.seed(random.SystemRandom().random())
    for i in range(30):
        pool.apply_async(delay_print,(rng.randrange(3,8),))
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()

