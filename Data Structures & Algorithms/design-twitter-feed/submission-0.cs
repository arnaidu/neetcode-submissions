public class Twitter {

    private Dictionary<int, List<(int TweetId, int Timestamp)>> _userTweets = new();
    private Dictionary<int, HashSet<int>> _follows = new();
    private int _timestamp = 1;

    public Twitter() {
        
    }
    
    public void PostTweet(int userId, int tweetId) {
        if (!_userTweets.TryGetValue(userId, out var feed)) {
            feed = new();
            _userTweets[userId] = feed;
        }

        feed.Add((tweetId, _timestamp));
        _timestamp += 1;
    }

    private void AddTempFeed(PriorityQueue<(int UserId, int Index, int TweetId), int> tempFeed, int userId) {
        if (_userTweets.TryGetValue(userId, out var userTweets)) {
            if (userTweets.Count > 0) {
                var index = userTweets.Count - 1;
                tempFeed.Enqueue((userId, index, userTweets[index].TweetId), -1 * userTweets[index].Timestamp);
            }
        }
    }
    
    public List<int> GetNewsFeed(int userId) {
        List<int> newsFeed = new();
        PriorityQueue<(int UserId, int Index, int TweetId), int> tempFeed = new();


        if (_follows.TryGetValue(userId, out var follows)) {
            foreach (var user in follows) {
                AddTempFeed(tempFeed, user);
            }
        }

        AddTempFeed(tempFeed, userId);

        while (newsFeed.Count < 10 && tempFeed.Count > 0) {
            var (user, index, tweetId) = tempFeed.Dequeue();
            newsFeed.Add(tweetId);

            // add next for that userTweet
            if (index > 0) {
                var userTweets = _userTweets[user];
                tempFeed.Enqueue((user, index - 1, userTweets[index - 1].TweetId), -1 * userTweets[index - 1].Timestamp);
            }
        }

        return newsFeed;
    }
    
    public void Follow(int followerId, int followeeId) {
        if (!_follows.TryGetValue(followerId, out var follows)) {
            follows = new();
            _follows[followerId] = follows;
        }

        follows.Add(followeeId);
    }
    
    public void Unfollow(int followerId, int followeeId) {
        if (!_follows.TryGetValue(followerId, out var follows)) {
            return;
        }

        follows.Remove(followeeId);
    }
}
