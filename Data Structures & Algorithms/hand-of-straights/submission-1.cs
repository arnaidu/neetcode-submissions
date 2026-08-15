public class Solution
{
    public bool IsNStraightHand(int[] hand, int groupSize)
    {
        if (hand.Length % groupSize != 0)
        {
            return false;
        }

        Array.Sort(hand);

        Dictionary<int, int> frequencies = hand
            .GroupBy(x => x)
            .ToDictionary(x => x.Key, x => x.Count());

        foreach (int num in hand)
        {
            // Already completely consumed as part of an earlier group
            if (!frequencies.ContainsKey(num))
            {
                continue;
            }

            // Start a new group at num
            for (int i = 0; i < groupSize; i++)
            {
                int current = num + i;

                if (!frequencies.ContainsKey(current))
                {
                    return false;
                }

                frequencies[current]--;

                if (frequencies[current] == 0)
                {
                    frequencies.Remove(current);
                }
            }
        }

        return true;
    }
}