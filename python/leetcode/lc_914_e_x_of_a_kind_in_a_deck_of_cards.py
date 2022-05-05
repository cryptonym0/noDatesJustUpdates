class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = Counter(deck).values()

        if len(deck) < 2:
            return False
        if len(count) == 1:
            return True

        for i in range(2, len(deck)):
            if all(c % i == 0 for c in count):
                return True
        return False
