import threading

class H2O(object):

    def __init__(self):
        self.hydrogen_sem = threading.Semaphore(2)
        self.oxygen_sem = threading.Semaphore(0)

        self.lock = threading.Lock()
        self.hydrogen_count = 0

    def hydrogen(self, releaseHydrogen):
        self.hydrogen_sem.acquire()

        releaseHydrogen()

        with self.lock:
            self.hydrogen_count += 1

            if self.hydrogen_count == 2:
                self.oxygen_sem.release()

    def oxygen(self, releaseOxygen):
        self.oxygen_sem.acquire()

        releaseOxygen()

        with self.lock:
            self.hydrogen_count = 0

            self.hydrogen_sem.release()
            self.hydrogen_sem.release()