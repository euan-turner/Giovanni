from datetime import datetime, timedelta

class TimeSlot():
    """Parent class for all time slots
    """    

    def __init__(self, startTime, recipient):
        self.recipient = recipient
        self.startTime = startTime


    def format_time(self):
        return self.startTime.strftime('%H:%M:%S')


class MakeSandwich(TimeSlot):
    """Time slot to make a sandwich, duration = 2.5
    """
    duration = timedelta(minutes = 2.5)
    task = "Make for: "

    def __init__(self, startTime, recipient):
        super().__init__(startTime, recipient)
        self.endTime = self.startTime + self.duration


    def __str__(self):
        return f'\t{self.format_time()}\t\tMake for:\t\t{self.recipient}'
        ##return f'Make sandwich for {self.recipient} at {self.format_time()}'


class ServeSandwich(TimeSlot):
    """Time slot to serve a sandwich, duration = 1
    """
    duration = timedelta(minutes = 1)
    task = "Serve to: "

    def __init__(self, startTime, recipient):
        super().__init__(startTime, recipient)
        self.endTime = self.startTime + self.duration
    
    def __str__(self):
        ##return f'Serve sandwich to {self.recipient} at {self.format_time()}'
        return f'\t{self.format_time()}\t\tServe to:\t\t{self.recipient}'


##Calculate start time
def calculate_start_time(times):
    if len(times) != 0:
        return times[-1].endTime
    else:
        return datetime.now()

def add_order(name,times):
    makeSlot = MakeSandwich(calculate_start_time(times), name)
    times.append(makeSlot)
    serveSlot = ServeSandwich(calculate_start_time(times), name)
    times.append(serveSlot)

##Test output
def output_schedule(times):
    print(generate_strings(times))

##Generate string output in one variable
def generate_strings(times):
    strings = []
    strings.append(['No.', 'Time', 'Task', 'Customer'])
    for i in range(len(times)):
        strings.append([str(i+1), times[i].format_time(), times[i].task, times[i].recipient])
    takeBreak = TimeSlot(calculate_start_time(times), '')
    strings.append([str(len(times)+1), takeBreak.format_time(), "Take break", '-'])
    return strings

    

