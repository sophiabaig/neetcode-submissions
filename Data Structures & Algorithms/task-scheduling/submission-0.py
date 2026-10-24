import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        taskMap = {}

        for t in tasks:
            if t not in taskMap:
                taskMap[t]=0
            taskMap[t]+=1
        
        t_heap = []
        for task, freq in taskMap.items():
            heapq.heappush(t_heap, freq * -1)
                
        cycles = 0
        q = collections.deque()

        while t_heap or q:
            cycles+=1

            if t_heap:
                task_freq = heapq.heappop(t_heap)
                task_freq+=1
                if task_freq < 0:
                    q.append((task_freq, cycles + n))

            if q:
                task_freq, task_cycle = q[0]

                if task_cycle == cycles:
                    q.popleft()
                    heapq.heappush(t_heap, task_freq)

        return cycles





        



        