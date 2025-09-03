##MBAi Hackathon
## Author: Sri Tankasala
## Team: Ethan Carpenter, Giri Ravichandran
## Date: September 3, 2025
## Count non punctuation or space characters
#

def countInput(input):
    count = 0
    revisedString = ""
    for character in input:
        if(character not in ['.','!',' ',',']): #checks for listed punctuation instnances
            count += 1 #counts the number of characters that are not in the listed punctuation
    return count

if __name__ == '__main__':

    print(countInput("Listen, Mr. Jones, calm down."))
