class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m = len(s)
        if m < 2:
            return 0
        dp = [0] * m
        res = 0 
        for i in range(1, m):
            if s[i] == ')':
                # dp[i] 表示到当前位置的最大长度
                if s[i - 1] == '(':
                    # 连接上前面的
                    if i - dp[i - 2] >= 0:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                else:
                    # 可能出现 (())
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                        dp[i] = 2 + dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0 )
            
            res = max(res, dp[i])
        return res 
                    
        