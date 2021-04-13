class Solution:
    def calculate(self, s: str) -> int:
        # Strip all whitespace
        s = s.replace(' ', '')
        s += "+0"
        
        stack = []
        num = 0
        op = "+"
        
        # print("i\tcurr\top\tstack\tsum")
        # print("----------------------------------")
        
        for i in s:
            # Some operator. Look at previous numbers and operator, 
            # and apply to top of stack
            if i in ["+", "-", "*", "/"]:
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                elif op == "/":
                    stack.append(int(stack.pop() / num))
                op = i
                num = 0
            # Another digit of a number, so increase place value and add current digit
            else:
                num = num * 10 + int(i)
                
            # print(i, num, op, stack, sum(stack), sep="\t")
        return sum(stack)