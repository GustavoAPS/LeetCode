from queue import Queue


class RecentCounter(object):

    def __init__(self):
        self.recent_calls = Queue()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        t is a time in milisseconds, return the number of calls that have been done in the last 3000 milisseconds
        """
        self.recent_calls.put(t)

        lower_range, upper_range = t - 3000, t

        # print(f" range is from {lower_range} to {upper_range}")

        out_of_range_removed = False

        while (out_of_range_removed is False):
            if not self.recent_calls.empty():
                first_item = self.recent_calls.queue[0]
                if first_item < lower_range:
                    self.recent_calls.get()
                else:
                    out_of_range_removed = True
            else:
                out_of_range_removed = True

        return self.recent_calls.qsize()


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))

# Input
# ["RecentCounter", "ping", "ping", "ping", "ping"]
# [[], [1], [100], [3001], [3002]]
# Output
# [null, 1, 2, 3, 3]

# Explanation
# RecentCounter recentCounter = new RecentCounter();
# recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
# recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
# recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
# recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3
