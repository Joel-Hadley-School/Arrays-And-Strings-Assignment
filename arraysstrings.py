#Problem 1
totals = 0 #SET TOTAL TO 0 TO RESET

def sum_even_numbers(numbers, totals): #INPUT TOTALS AND NUMBERS VARIALBES
    for number in numbers:
        if number % 2 == 0:
            totals += number #IF NUMBER IS MODULUS 2 == 0, THE NUMBER IS ADDED TO THE TOTAL
    return totals #SEND FINISHED TOTALS

numbers = [1,2,3,4,5,6] #SET NUMBERS
totals = sum_even_numbers(numbers, totals) #GET TOTAL AFTER THE FUNCTION RUNS           
print(totals) #PRINT TOTALS

#Problem 2
message = "Hello"
#SET MESSAGE
def char_frequency(message): #DEFINE FUNCTION, ADD MESSAGE INTO PARAMETERS
    letter_dict = {}  #QUICK DICTIONARY SETUP
    for letter in message: #CHECK THE LETTER
        if letter in letter_dict: #THIS CODE JUST SAYS BASICALLY: IF LETTER ISNT ALREADY IN THE DICTIONARY ADD IT
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict #RETURN DICTIONARY COMPLETED

lettercount = char_frequency(message) #FUNCTION RUNS, RESULT GIVEN
print(lettercount)

#Problem 3

def filter_negative_numbers(originallist):
    withoutit = []
    for number in originallist: #TAKES THE NUMBER AND STARTS LOOP
        if number > 0:
            withoutit.append(number) #ADD NUMBER TO LIST IF IT IS LESS THAN OR EQUAL TO 0
        if number == 0:
            withoutit.append(number)
    return withoutit

originallist = [-1, 0, 2, -3, 5] #INPUT NUMBERS
final_list = filter_negative_numbers(originallist)
print(final_list) #PRINT LIST

#Problem 4 (work in progress)

def average_score(scores):
    score1 = int('Alice')
    score2 = int('Bob')
    score3 = int('Charlie')
    totals = score1 + score2 + score3
    return totals

scores = ({'Alice' : 85, 'Bob' : 90, 'Charlie': 70})
print(totals)

#Problem 5

def reverselist(startinglist): #FUNCTION AND PARAMETERS
    newlist = startinglist[::-1] #COPIES TO NEW LIST AND REVERSES ORDER (looked this up)
    return newlist #RETURNS THE LIST
    
startinglist = [1,2,3] #STARTING LIST
reversedlist = reverselist(startinglist)
print(reversedlist) #PRINT FINAL LIST

#Problem 6

def count_vowels(message2):
    vowel_dict = {'a': 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u' : 0} #SETS LETTERS THAT CAN BE CHOSEN
    for letter in message2.lower(): #CHECKS IF VOWELS ARE IN THE MESSAGE
        if letter in vowel_dict:
            vowel_dict[letter] += 1 #ADDS TO VOWEL COUNTER
    return vowel_dict

message2 = "The quick brown fox jumps over the lazy dog" #MESSAGE
vowels = count_vowels(message2)
print(vowels)