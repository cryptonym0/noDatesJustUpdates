class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # 2 rules
        # "." is ignored in local not not domain
        # "+" means to strip everything after the + in local namme
        # alb.gg.+.dd@gmail.com, would be "albgg@gmail.com"
        # return number of unique

        unique_emails = {}
        count = 0

        for i, v in enumerate(emails):
            head = emails[i].rsplit("@", 1)
            email = head[0].split("+", 1)[0].replace(".", "") + "@" + head[1]

            if unique_emails.get(email, None) is not None:
                unique_emails[email] += 1
            else:
                unique_emails[email] = 1
                count += 1

        return count

        # .replace('.', '')

        # string.rsplit('@', 1)
