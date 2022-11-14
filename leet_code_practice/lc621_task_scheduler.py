import heapq
class Solution:
    def leastInterval(self, tasks, n):
        # first count the frequency for each task
        task_freq = {}
        for task in tasks:
            if task not in task_freq:
                task_freq[task] = 1
            else:
                task_freq[task] += 1

        # next use task_frequency to populate frequency heap
        # initialize item position as "0" since we are able to choose any item at the start
        # items in freq_heap will always be allowable options for next task
        # thus we can prioritize based on frequency min(-freq) is max(freq)
        freq_heap = []
        for freq in task_freq.values():
            heapq.heappush(freq_heap, (-freq , 0))

        # initialize waiting heap
        # this is where we hold tasks that are not ready yet
        wait_heap = []
        task_count = 0
        while freq_heap or wait_heap:
            task_count += 1

            # add all tasks ready to complete
            while wait_heap and wait_heap[0][0] + n < task_count:
                move = heapq.heappop(wait_heap)
                heapq.heappush(freq_heap, (move[1], move[0] ))

            # no tasks are ready, continue to next loop
            if not freq_heap:
                continue
            
            next_task = heapq.heappop(freq_heap)
            
            # if frequency greater than 1, add to wait_heap
            # flip frequency and position
            # we prioritize wait_heap by task completion position
            if next_task[0] < -1:
                heapq.heappush(wait_heap, (task_count, next_task[0] + 1 ))

        return task_count

