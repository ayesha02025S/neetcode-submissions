class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1) # creates dp = [0, 0, 0, 0, 0] if amount = 4
        # each index represents an amount of money 
        dp[0] = 1 # 1 way to make $0
        
        for i in range(len(coins) - 1, -1, -1): # processing coins[1,2,3] -> 3, 2, 1
            for a in range(1, amount + 1): # since amount = 4, a =1, 2, 3, 4 # how many ways can i make $1, 2, 3, 4
                dp[a] += dp[a - coins[i]] if coins[i] <= a else 0 # if i use this coin, how much money is left to make
        return dp[amount]
        


        