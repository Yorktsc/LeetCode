class Solution: 
    def calculate(self, s: str) -> int:
        res = []
        s = "".join(s.split(" "))
        tmp = ""
        for char in s:
            if char != "+" and char != "-":
                tmp += char
            else:
                res.append(tmp)
                res.append(char)
                tmp = ""
        res.append(tmp)
        res2 = []
        for part in res:
            if part.isdigit() or part == "+" or part == "-":
                res2.append(part)
            else:
                ss = str(self.cal(part))
                res2.append(ss)
        total = int(res2[0])       
        i = 1 
        while i < len(res2):
            operator = res2[i]
            num = res2[i+1]
            if operator == "+":
                total += int(num)
            else:
                total -= int(num)
            i += 2
        return total
    
    def cal(self, s):
        res = 1
        tmp_s = ""
        last_cal = "*"
        for idx, char in enumerate(s):
            if char == "*" or char == "/" or idx == len(s) - 1:
                num = int(tmp_s) if idx != len(s) - 1 else int(tmp_s + char)
                if last_cal == "*":
                    res *= num
                elif last_cal == "/":
                    res //= num
                tmp_s = ""
                last_cal = char
            else:
                tmp_s += char
        return res
