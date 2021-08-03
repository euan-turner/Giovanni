name = input("Input name:")

TimeSlots = []

class TimeSlot():
    def __init___(self):
        self.SeqNo = self.CalculateSeqNo(TimeSlots)
    def CalculateSeqNo(self,arr):
        if len(arr) > 0:   
            NewSeqNo = arr[-1].SeqNo
            arr[-1].SeqNo += 1
        elif len(arr) == 0:
            NewSeqNo = 1
        return NewSeqNo

        