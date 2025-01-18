# 933. Number of Recent Calls
# https://leetcode.com/problems/number-of-recent-calls/description/


class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)

        pointer = len(self.queue) - 2

        while pointer >= 0:
            if self.queue[-1] - self.queue[pointer] > 3000:
                break

            pointer -= 1

        return len(self.queue) - pointer - 1
