public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
        int n = position.Length;
        (int position, double time)[] carInfo = new (int position, double time)[n];
        for (int i = 0; i < n; i++) {
            carInfo[i] = (position[i], Time(target, position[i], speed[i]));
        }
        
        // closest to target -> furthest
        Array.Sort(carInfo, (x, y) => y.position.CompareTo(x.position));
                
        int numFleets = 0;
        double currMaxTime = 0;
        for (int i = 0; i < n; i++) {
            if (currMaxTime < carInfo[i].time) {
                currMaxTime = carInfo[i].time;
                numFleets += 1; // each new max time means a new fleet since this car can't catch up. We don't care which car goes to which fleet.
            }
        }
        
        return numFleets;
    }

    // The i-th car can catch up to the j-th car if and only if the Time to reach
    // target from position is less than j-th cars time.
    public double Time(int target, int position, int speed) {
        int displacement = target - position;
        return (double)displacement / speed;
    }
}