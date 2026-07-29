public class Solution {
    public int LeastInterval(char[] tasks, int n) {
        var taskFreqs = tasks.GroupBy(o => o).ToDictionary(o => o.Key, o => o.Count());
        var pq = new PriorityQueue<(char task, int count), int>();
        foreach (var task in taskFreqs) {
            pq.Enqueue((task.Key, taskFreqs[task.Key]), -taskFreqs[task.Key]);
        }
        
        // (task, count, readyTime)
        var cooldownQueue = new Queue<(char task, int count, int readytime)>();
        
        var time = 0;
        while (pq.Count > 0 || cooldownQueue.Count > 0) {
            // Check cooldown queue. If any are now ready, then add them back to PriorityQueue
            while (cooldownQueue.Count > 0 && cooldownQueue.Peek().readytime <= time) {
                (char readyTask, int count, int readytime) = cooldownQueue.Dequeue();
                pq.Enqueue((readyTask, count), -count);
            }
            
            if (pq.Count > 0) {
                (char task, int taskCount) = pq.Dequeue();
                // task runs
                taskCount--;
                
                // if any more same task left
                if (taskCount > 0) {
                    // Next similar task ready after n cycle cooldown
                    int readyTime = time + n + 1;
                    
                    // Load into cooldown Queue
                    cooldownQueue.Enqueue((task, taskCount, readyTime));
                }
            }
            
            time++;
        }
        
        return time;
    }
}