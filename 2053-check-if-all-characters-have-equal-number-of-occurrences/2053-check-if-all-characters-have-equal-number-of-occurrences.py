class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import defaultdict
        count_dict = defaultdict(int)
        for letter in s:
            count_dict[letter] += 1
        
        return len(set(count_dict.values())) == 1
        