class Solution(object):
    def findWinners(self, matches):
        winners = []
        losers = []
        new_winner = set()
        new_loser = set()
        for match in matches:
            winners.append(match[0])
            losers.append(match[1])
      
        for winner in winners:
            if winner not in losers:
                new_winner.add(winner)
                
        for loser in losers:
            if losers.count(loser) == 1:
                new_loser.add(loser)
                
        new_winner= sorted(new_winner)
        new_loser = sorted(new_loser)
        answer = []
        answer.append(new_winner)
        answer.append(new_loser)
        return answer
akua = Solution()
print(akua.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))