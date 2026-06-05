import re
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            first_plus = email.find("+")
            only_at = email.find("@")
            email_up_to_plus = email[:first_plus].replace(".", "")
            seen.add(email_up_to_plus + email[only_at:])
        
        return len(seen)