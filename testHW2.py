#ClaireTo
#testHW2.py
#12/10/2019

#Part1: Simulating a die
import random

'''The class Die stimulates a single die. It has two attributes: sides and value.
sides: represents the number of sides the die has. value: representing the current value
showing on the dice (always between 1 and sides)'''
class Die(object):
    def __init__(self,sides):
        self.sides = sides
        self.value = random.randint(1,sides) #The current value showing on the dice. Use random.

#This function returns the sides of the die
    def getSides(self):
        return self.sides

#This function takes in an arguement as a new sides number (additionally from self),
#changes the current sides
    def setSides(self,newsides):
        self.sides=newsides

#This function works as initiates a new roll of the die. Use random.
    def roll(self):
        self.value = random.randint(1,self.sides)

#This function stores the newly value of the die after the roll.
    def getValue(self):
        return self.value

#Part2: Simulating dice
'''This class simulates multiple dice, but have the same sides.'''
class Dice(object):
    def __init__(self,count,sides):
        self.diels = [] #A list of Die objects. Use an empty list to later concatenate.
        self.sides = sides

        for i in range(count):
            self.diels.append(Die(sides)) #This for loop used to create the diels
#according to the number of count.

    def getCount(self):
#This function returns the count.
        return len(self.diels)

    def roll(self):
#This function works as roll a new roll. Number of rolls equal number of counts.
        for el in range(len(self.diels)):
            self.diels[el].roll() #Use method from class Die

    def getValues(self):
#This function stores all the values received after rolls above
        ls = [] #Create an empty list to later concatenate
        for el in range(len(self.diels)):
            ls.append(self.diels[el].getValue()) #Use method from class Die
        return ls

#This function returns the sides of the Die. Die all have the same sides, so
#just return a number
    def getSides(self):
        return self.diels[0].getSides() #self.diels[0] is the same as any other
#value in the list self.diels. So I just take one.


#Part3: Simulating Gombaud
'''This function takes 2 arguments. dice: a dice object. rolls: the number of times
the player can roll. This function returns False if loss and True if win.'''
def gombaud(dice,rolls):
    for i in range(rolls):
        dice.roll() #Repeatedly roll until reach the 'rolls' number
        count = 0 #Set count = 0 to later add
        ls = dice.getValues()
        for el in range(len(ls)):
            if ls[el] == dice.getSides():
                count += 1 #If every value in the ls is the same, meaning that
#it is a win. count +1 for each time like that. So at the end the add is equal to
#the length of the ls.
        if count == len(ls):
            return True #Win
        else:
            return False #Loss

#Part4: Answering Gombaud
'''This function takes 3 arguments and return the number of wins divided
by simCount.'''
def testGombaud(dice,rolls,simCount):
    num_won = 0 #Set number of wins at 0 to later add.
    for i in range(simCount):
        if gombaud(dice,rolls) == True: #Similar to function gombaud
            num_won+=1

    return num_won/simCount

'''This function runs and prints the results of running testGombaud.'''
def main():
    print(testGombaud(Dice(2,6),24,10))
    print(testGombaud(Dice(2,6),24,100))
    print(testGombaud(Dice(2,6),24,1000))
    print(testGombaud(Dice(2,6),24,10000))
    print(testGombaud(Dice(2,6),24,100000))

if __name__ == '__main__':
  main()

#Part5: Analysis
#How do my results change between different runs of your programs?
# - If simCount is 10, after different runs the values returned are still 0.0
# - If simCount is 100,1000, after different runs, results fluctuate a lot.
# - If simCount is 10000,100000, after different runs, the results do not fluctuate a lot.
#about 0.026 to 0.028

#I think the bigger the simCount, the more accurate the result will be.
#Because I think the more time you test, the more reliable and accurate the results
#will be.

#I would determine a proper simulation count by having two simulation counts, one is
#smaller than the other.
#If the smaller simCount's results and the bigger simCount's results do not
#fluctuate a lot and after a number of runs (large). Then I think it will be enough.
