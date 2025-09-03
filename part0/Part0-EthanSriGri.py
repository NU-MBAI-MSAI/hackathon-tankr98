##MBAi Hackathon
## Author: Sri Tankasala
## Team: Ethan Carpenter, Giri Ravichandran
## Date: September 3, 2025
## Various Function Definitions to solve part 0


def getTicketCost(speedLimit, drivingSpeed):
    speed_diff = speedLimit - drivingSpeed #Takes difference of speed and limit and tests against scenarios
    if(speed_diff<= -10):
        return 50
    elif(speed_diff>=6 and speed_diff<=20):
        return 100
    elif(speed_diff>=21 and speed_diff<=40):
        return 150
    elif(speed_diff >= 40):
        return 300

def calcHeaatingCoolingDays():
    heating = 0 #defined local variables at starting position
    cooling = 0
    while(True):
        temp = input("Enter the average daily temperature: ")
        temp = int(temp) #converts temp to an integer
        if temp<-459:
            break #break scenario
        if temp<60:
            heating += 1 #incrmentally adds to heating variable
            continue
        if temp<80:
            cooling += 1 #incrementally adds to cooling variable
            continue
    print("Heating days:",heating)
    print("Cooling days:",cooling)

def countInput(input):
    count = 0
    revisedString = ""
    for character in input:
        if(character not in ['.','!',' ',',']): #checks for listed punctuation instnances
            count += 1 #counts the number of characters that are not in the listed punctuation
    return count

def maxProfit(prices):
    max = 0
    days = len(prices)
    for i in range(days):
        for j in range(i,days):
            if(prices[j] - prices[i]>max):
                max = prices[j] - prices[i]
    return max


if __name__ == '__main__':
    print(getTicketCost(35,45))
    calcHeaatingCoolingDays()
    print(countInput("Listen, Mr. Jones, calm down."))
    print(maxProfit(prices = [7,1,5,3,6,4]))
    print(maxProfit(prices=[1, 2, 3, 4, 5, 6]))
    print(maxProfit(prices=[1, 3, 1, 6, 6, 3]))
    print(maxProfit(prices=[7, 7, 5, 5, 5, 7]))
    print(maxProfit(prices=[7, 6, 5, 4, 3, 2]))
