import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(profits, capital))
        projects.sort(key=lambda x: x[1])

        heap = []
        project_count = 0
        available_capitol = w
        project = 0
        max_projects = min(len(projects), k)

        while project_count < max_projects:
            # fill up heap up to available_capitol
            while project < len(projects) and projects[project][1] <= available_capitol:
                profit = projects[project][0]
                heapq.heappush(heap, -profit)
                project += 1
            
            # if no project in heap, then we can't do anything more
            if not heap:
                break
            
            # grab max profit with available_capitol and add on to available_capitol
            max_profit_for_available_capitol = -heapq.heappop(heap)
            available_capitol += max_profit_for_available_capitol

            # increase project count
            project_count += 1
        
        return available_capitol
