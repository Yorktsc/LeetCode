class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        s = set()
        for e in emails:
            domain = False
            valid, index = "", 0
            while index < len(e):
                c = e[index]
                if c == '.' and not domain:
                    index += 1
                    continue 
                    
                elif c == '+':
                    index += 1
                    while index < len(e): 
                        if e[index] == '@':
                            domain = True
                            valid += '@'
                            break
                        else:
                            index += 1
                            continue
                else:
                    if c == '@':
                        domain = True
                    valid += c
                index += 1
            s.add(valid)
        print(s)
        return len(s)
        """
        s = set()
        for email in emails:
            local, domain = email.split("@")
            if '+' in local:
                local = local[:local.index('+')]
            s.add(local.replace(".", "") + '@' + domain)
        return len(s
