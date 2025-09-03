##MBAi Hackathon
## Author: Sri Tankasala
## Team: Ethan Carpenter, Giri Ravichandran
## Date: September 3, 2025
## Calculate Max Profit for stock prices

def maxProfit(prices):
    if len(prices) == 0:
        return 0
    max = 0
    days = len(prices)
    for i in range(days):
        for j in range(i,days):
            if(prices[j] - prices[i]>max):
                max = prices[j] - prices[i]
    return max

if __name__ == '__main__':
    print(maxProfit(prices = [7,1,5,3,6,4]))
    print(maxProfit(prices=[1, 2, 3, 4, 5, 6]))
    print(maxProfit(prices=[1, 3, 1, 6, 6, 3]))
    print(maxProfit(prices=[7, 7, 5, 5, 5, 7]))
    print(maxProfit(prices=[7, 6, 5, 4, 3, 2]))