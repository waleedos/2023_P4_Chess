class Round:
    def __init__(self, name, matches=[], start_time="", end_time=""):
        self.name = name
        self.matches = matches
        self.start_time = start_time
        self.end_time = end_time

    def to_dict(self):
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_time": self.start_time,
            "end_time": self.end_time,
        }
