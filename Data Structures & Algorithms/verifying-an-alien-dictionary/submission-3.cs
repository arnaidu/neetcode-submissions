public class Solution {
    public bool IsAlienSorted(string[] words, string order) {
        var previousWord = words[0];

        for (int i = 1; i < words.Length; i++) {
            var currWord = words[i];
            var minLength = Math.Min(currWord.Length, previousWord.Length);

            for (int j = 0; j < minLength; j++) {
                var letterBefore = previousWord[j];
                var orderLetterBefore = order.IndexOf(letterBefore);

                var letterCurrent = currWord[j];
                var orderLetterCurrent = order.IndexOf(letterCurrent);

                if (orderLetterBefore > orderLetterCurrent) {
                    return false;
                } 

                if (orderLetterBefore < orderLetterCurrent) {
                    break;
                }
            }

            if (currWord.Length < previousWord.Length && previousWord.StartsWith(currWord)) {
                return false;
            }   

            previousWord = currWord;
        } 

        return true;
    }
}