from collections import defaultdict


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        char_dict = defaultdict(int)
        shortest = None
        valid = True

        for i, v in enumerate(licensePlate):
            if v.isalpha():
                char_dict[v.lower()] += 1

        for word in words:
            valid = True
            for chars in char_dict:
                if word.count(chars) < char_dict[chars]:
                    valid = False
                    break
            if valid:
                if not shortest or len(word) < len(shortest):
                    shortest = word
        return shortest
