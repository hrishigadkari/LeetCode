import numpy as np
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum([ i <= queryTime <= j for i, j in zip(startTime,endTime)])