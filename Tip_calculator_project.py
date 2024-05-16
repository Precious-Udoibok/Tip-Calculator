#program to calculate a tip
print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $')) #users enters a bill
percent = int(input('What percentage tip would you like to give? 10, 12 or 15? ')) #enters a percentage tip
people = int(input('How many people to split the bill? ')) #enter the number of people 
final_bill = (percent/100 * bill + bill)#people #calculate the final bill
bills = '{:.2f}'.format(final_bill) # convert it to 2 d.p
print(f'Each person should pay: ${bills}')