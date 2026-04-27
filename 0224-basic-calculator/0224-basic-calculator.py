class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        result = 0
        sign = 1      # 默认正号
        num = 0

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)   # 处理多位数，如"12"
            
            elif c == '+' or c == '-':
                result += sign * num      # 把上一个数结算进result
                num = 0
                sign = 1 if c == '+' else -1
            
            elif c == '(':
                # 开新账本前，把当前状态压栈保存
                stack.append(result)
                stack.append(sign)
                result = 0   # 新账本清零
                sign = 1
            
            elif c == ')':
                result += sign * num      # 结算括号内最后一个数
                num = 0
                result *= stack.pop()     # 乘以括号前的符号
                result += stack.pop()     # 加上括号前的累计值
        
        result += sign * num  # 别忘了最后一个数
        return result        