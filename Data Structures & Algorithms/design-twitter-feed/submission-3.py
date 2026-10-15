class Twitter:

    def __init__(self):
        self.time = 0
        self.follow_map = defaultdict(set)
        self.user_tweets_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets_map[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follow_map[userId]
        users.add(userId)

        heap = []
        for user in users:
            for tweet in self.user_tweets_map[user]:
                heapq.heappush(heap, tweet)
                if len(heap) > 10:
                    heapq.heappop(heap)

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res[::-1] 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)


"""
follow
4 -> 3

tweets
3 -> 9, 10, 11, 12, 16
4 -> 13, 14, 15

"""