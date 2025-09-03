##MBAi Hackathon
## Author: Sri Tankasala
## Team: Ethan Carpenter, Giri Ravichandran
## Date: September 3, 2025
## Calculate Number of days that require heat and AC

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

    if __name__ == '__main__':
        calcHeaatingCoolingDays()
