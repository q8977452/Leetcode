class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if '0000' in deadends:
            return -1
        queue = ['0000']
        visits = set(queue + deadends)
        step = 0
        while queue:
            queue0 = []
            for status in queue:
                if status == target:
                    return step
                for nstatus in self.nextStatus(status):
                    if nstatus in visits:
                        continue
                    visits.add(nstatus)
                    queue0.append(nstatus)
            queue = queue0
            step += 1 
        return -1
    def nextStatus(self, status):
        ans = []
        for i, n in enumerate(status):
            for y in (-1, 1):
                digit = (int(status[i]) + y +10) % 10
                yield status[:i] + str(digit) + status[i+1:]
        