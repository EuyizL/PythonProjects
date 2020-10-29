'''import random
def getRandomNumber(min, max):
    return random.randrange(min, max+1)


def getRandomAverage(min, max, count):
    numList = []
    
    for i in range(count):
        numList.append(getRandomNumber(min, max))
        
    sum = 0
                          
    for num in numList:
        sum = sum + num

    return sum / count



def main():
    minMaxValue = int(input('Enter the minimum value, separated by a space: '))
    min, max = minMaxValue.split(' ')
    numDigitPrecision = int(input('Enter number of digits precision after decimal point: '))
    count = int(input('Enter number of random numbers to test: '))
    avg = getRandomAverage(min, max, count)
    print(f'Average of {count} random numbers, {avg:numDigitPrecisiond} of {} and {}, {}')'''
    
    
def claim():
    listOfClaims = []
    while True:
        print('Menu\n1. Make A Claim\n2. Get Summary\n0. Exit')
        choice = int(input('Enter option: '))
        if choice == 0:
            print('End of program')
            break
        if choice == 1:
            policyType = input('Enter policy type: ').lower()
            if policyType != 'a' and policyType != 'b' and policyType != 'c' :
                print('Invalid policy type')
            else:
                claimAmt = float(input('Enter claim amount: $'))
                if claimAmt < 0:
                    print('Invalid claim amount')
                else:
                    fw = open('bmi.dat', 'w')
                    listOfClaims.append(claimAmt)
                    print(f'{listOfClaims}', file=fw)
                    
                    fr.close()
                    
                
claim()
        
        
        
        
        
        
        
        
        
        
        