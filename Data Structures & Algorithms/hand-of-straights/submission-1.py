from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        count_dict = Counter(hand)
        for i in count_dict.keys():
            if count_dict[i] == 0:
                continue
            while count_dict[i] != 0:
                group = [j for j in range(i,i+groupSize)]
                print(group)
                for card in group:
                    if count_dict[card] == 0:
                        return False
                    count_dict[card] -= 1
        
        return True


