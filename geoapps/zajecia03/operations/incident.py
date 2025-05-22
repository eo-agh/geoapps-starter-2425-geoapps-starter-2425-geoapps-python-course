from datetime import datetime


class Incident:
    __max_id = 0

    def __init__(self, description, priority, location, reporter):
        Incident.__max_id += 1
        self.id = Incident.__max_id
        self.description = description
        self.priority = priority  # low, medium, high
        self.location = location
        self.reporter = reporter
        self.timestamp = datetime.now()
        self.time_since_report = None
        self.status = "pending"

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r}, priority={self.priority!r}, location={self.location}, reporter={self.reporter!r}, timestamp={self.timestamp!r}, timestamp={self.status!r})\n"

    def __str__(self):
        return f"Incident {self.id}: {self.description}\nPriority: {self.priority}\nReporter: {self.reporter}\nReported at: {self.timestamp}\nLocation: {self.location}\nStatus: {self.status}"
