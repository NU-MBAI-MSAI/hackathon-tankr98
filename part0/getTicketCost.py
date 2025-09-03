##MBAi Hackathon
## Author: Sri Tankasala
## Team: Ethan Carpenter, Giri Ravichandran
## Date: September 3, 2025
## Calculate Speeding Ticket Cost based on speed and limit


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

if __name__ == '__main__':
    print(getTicketCost(35,45))

