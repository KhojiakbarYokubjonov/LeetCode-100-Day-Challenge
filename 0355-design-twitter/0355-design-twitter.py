
class User:
    def __init__(self, id):
        self.id = id
        self.followers = {}
        self.following = {}
        self.feed = []
        self.feedLimit = 10
        heapq.heapify(self.feed)
    def notify(self, tweetId, time):        
        for id in self.followers:
            user = self.followers[id]
            user.receive(tweetId, time)
    def receive(self, tweetId, time):
        heapq.heappush(self.feed, (-time, tweetId))
        if len(self.feed) > self.feedLimit:
            self.feed.pop()
            
class Twitter:

    def __init__(self):
        self.tweetLimit = 10
        self.users = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.validateUser(userId)
        user = self.users[userId]
        user.feed.append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.time += 1

        self.validateUser(userId)
        allFeed = []
        user = self.users[userId]
        for time, tweet in user.feed:
            allFeed.append((-time, tweet))
          
        for id in user.following:
            u = self.users[id]
            for time,tweet in u.feed:
                heapq.heappush(allFeed, (-time, tweet))
                
        allFeed.sort(key = lambda k:k[0])
        result = []
        for time, tweet in allFeed:
            result.append(tweet)
            if len(result) == 10:
                break
        return result
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.time += 1

        self.validateUser(followerId)
        self.validateUser(followeeId)

        follower = self.users[followerId]
        followee = self.users[followeeId]
        
        followee.followers[followerId] = follower
        follower.following[followeeId] = followee
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.time += 1
        follower = self.users[followerId]
        followee = self.users[followeeId]
        
        if followerId in followee.followers:
            followee.followers.pop(followerId)
        if followeeId in follower.following:
            follower.following.pop(followeeId)
    
    def validateUser(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)