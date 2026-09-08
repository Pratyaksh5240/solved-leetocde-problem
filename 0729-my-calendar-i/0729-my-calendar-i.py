class MyCalendar(object):

    def __init__(self):
        self.events = []

    def book(self, startTime, endTime):
        for start, end in self.events:

            # No overlap
            if endTime <= start or startTime >= end:
                continue

            # Overlap found
            return False

        self.events.append((startTime, endTime))
        return True