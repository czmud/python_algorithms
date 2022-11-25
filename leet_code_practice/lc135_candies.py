class Solution:
    def candy(self, ratings):
        candies = 1
        pos_run = 0
        neg_run = 0

        i = 1
        while i < len(ratings):
            while i < len(ratings) and ratings[i] > ratings[i-1]:
                pos_run += 1
                candies += pos_run
                i += 1
            
            while i < len(ratings) and ratings[i] == ratings[i-1]:
                candies += pos_run + 1
                pos_run = 0
                i += 1

            while i < len(ratings) and ratings[i] < ratings[i-1]:
                neg_run += 1
                candies += neg_run
                i += 1

            candies += max(pos_run, neg_run)
            pos_run = 0
            neg_run = 0
        return candies