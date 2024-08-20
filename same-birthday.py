#Number of people
n = 22

#Probability of people having different birthdays
prob_diff_bday = 1
for i in range(n):
    prob_diff_bday *= (364-i)/365

#Probability of people having the same birthday
prob_same_bday = 1 - prob_diff_bday

print (f"The probability of people having the same birthday out of {n} people = {prob_same_bday}")