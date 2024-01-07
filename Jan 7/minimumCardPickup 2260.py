"""
My question
https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/

Notes:
    1:00:10
    Don't like the way I got to my answer... It performs really well, but going back and forth between using
    lists and the cards.index(...) solution only to settle on using a dict in the end felt cheap.
"""

class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        
        minimum = len(cards) + 1

        repeats = {}

        for i in range(len(cards)):
            if cards[i] not in repeats:
                # print(repeats)
                repeats[cards[i]] = i

            else:
                first = repeats[cards[i]]
                cards[first] = -1
                new_min = i-first + 1
                minimum = new_min if new_min < minimum else minimum
                repeats[cards[i]] = i

        if minimum == len(cards) + 1:
            return -1
        return minimum
