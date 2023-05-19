import datetime

class Round:
    def __init__(self, name):
        self.name = name
        self.matches = []
        self.start_time = datetime.datetime.now()
        self.end_time = None
