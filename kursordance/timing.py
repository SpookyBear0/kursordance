from threading import Thread

class Timer:
    def __init__(self):
        self.time = 0
        def time():
            while True:
                self.time += 1
        Thread(target=time).start()
        
    @property
    def get_time(self):
        return self.time