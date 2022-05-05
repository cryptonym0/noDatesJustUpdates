# https://leetcode.com/submissions/detail/683074055/
class Logger:
    def __init__(self):
        # initialize object
        self.seen = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.seen.get(message, None) is not None:
            # check next allowed timestamp <= timestamp
            if self.seen.get(message) <= timestamp:
                self.seen[message] = timestamp + 10
                return True
            return False

        # brand new message
        else:
            self.seen[message] = timestamp + 10
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
