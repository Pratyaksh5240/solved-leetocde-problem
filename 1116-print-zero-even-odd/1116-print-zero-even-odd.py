import threading

class ZeroEvenOdd(object):

    def __init__(self, n):
        self.n = n
        self.current = 1

        self.zero_sem = threading.Semaphore(1)
        self.odd_sem = threading.Semaphore(0)
        self.even_sem = threading.Semaphore(0)

    def zero(self, printNumber):
        for _ in range(self.n):

            self.zero_sem.acquire()

            printNumber(0)

            if self.current % 2 == 1:
                self.odd_sem.release()
            else:
                self.even_sem.release()

    def even(self, printNumber):
        for _ in range(self.n // 2):

            self.even_sem.acquire()

            printNumber(self.current)

            self.current += 1

            self.zero_sem.release()

    def odd(self, printNumber):
        for _ in range((self.n + 1) // 2):

            self.odd_sem.acquire()

            printNumber(self.current)

            self.current += 1

            self.zero_sem.release()