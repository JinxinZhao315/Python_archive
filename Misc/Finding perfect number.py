# A compilation of if, for , while.


a_int_str=input('Type an integer here:')
a_int=int(a_int_str)

divisor=1
divisor_sum=0 #This seams useless, but you have to define it or an error of 'name
              #not defined' will occur. Whenever you need a THING that is initially nothing/empty,
              #define it 0 first! 

while divisor<a_int:
    if a_int % divisor == 0:
        divisor_sum = divisor_sum + divisor
    divisor += 1
if divisor_sum == a_int:
    print('The number is perfect')
if divisor_sum > a_int:            
    print('The number is abundant')
if divisor_sum < a_int:
    print('The number is deficient')

# Here do not use if...else... since there are three cases!(>,<,=)
# The "else" in If...else.. means ALL other occasions except that described in "if"!


# Difference between if...else and if:
# after an if, what follows the if will certainly be executed.
# after an if...else..., the else part may not be executed / excuted only when if is False. 
