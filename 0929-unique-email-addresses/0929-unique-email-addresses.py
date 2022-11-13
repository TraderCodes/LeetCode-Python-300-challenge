class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
#         first split the @ and find if domain name contain symbols 
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.','')
            unique.add((local,domain))
        return len(unique)