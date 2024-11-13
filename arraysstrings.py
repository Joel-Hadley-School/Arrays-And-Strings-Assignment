#1
totals = 0 #SET TOTAL TO 0 TO RESET

def sum_even_numbers(numbers, totals): #INPUT TOTALS AND NUMBERS VARIALBES
    for number in numbers:
        if number % 2 == 0:
            totals += number #IF NUMBER IS MODULUS 2 == 0, THE NUMBER IS ADDED TO THE TOTAL
    return totals #SEND FINISHED TOTALS

numbers = [1,2,3,4,5,6] #SET NUMBERS
totals = sum_even_numbers(numbers, totals) #GET TOTAL AFTER THE FUNCTION RUNS           
print(totals) #PRINT TOTALS

#2
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


#3

