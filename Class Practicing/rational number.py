def gcd(bigger,smaller):
    '''return the greatest common divisor of two numbers using Euclid's GCD algorithm '''
    if not bigger > smaller:
        bigger,smaller = smaller,bigger    # Switch bigger and smaller when smaller becomes bigger
    while smaller != 0:
        remainder = bigger % smaller
        bigger,smaller = smaller,remainder
    return bigger


def lcm(a,b):
    '''return integer, least common multiplier of two numbers '''
    return int ( (a*b) / gcd(a,b) )

class Rational(object):
    def __init__(self,numer,denom = 1):
        print('in constructor')
        self.numer = numer
        self.denom = denom

    def __str__(self):
        print('in str')
        return str(self.numer)+'/'+str(self.denom)

    def __repr__(self):
        print('in repr')
        return self.__str__()

    def __add__(self,num2):
        print('in add')
        if type(num2) == int:
            num2 = Rational(num2)
        if type(num2) == Rational:
            denom_lcm = lcm(self.denom,num2.denom)
            numer_sum = self.numer*(denom_lcm/self.denom) + num2.numer*(denom_lcm/num2.denom)
            sum_fraction = Rational(int(numer_sum),denom_lcm)
            return sum_fraction
        else:
            print('Wrong type.')
            raise(TypeError)

    def __sub__(self,num2):
        print('in sub')
        denom_lcm = lcm(self.denom,num2.denom)
        numer_sum = self.numer*(denom_lcm/self.denom) - num2.numer*(denom_lcm/num2.denom)
        sum_fraction = Rational(int(numer_sum),denom_lcm)

    def reduce_rational(self):
        print('in reduce')
        the_gcd = gcd(self.numer,self.denom)
        return Rational(self.numer//the_gcd,self.denom//the_gcd)

    def __eq__(self,num2):
        print('in eq')
        reduced_self = self.reduce_rational()
        reduced_num2 = num2.reduce_rational()
        # When you call a function defined within class, call it as if it is a method i.e. use the object.method() way
        return reduced_self.numer == reduced_num2.numer and reduced_self.denom == reduced_num2.denom

    def __radd__(self,num2):
        print('in radd')
        return self.__add__(num2)


        
'''The difference between having and not having __repr__:
instance_one = Rational(1,2)
when have, if you type instance_one directly into intepreter, you get 1/2
when don't have, if you type instance_one directly, you get <__main__.Rational object at ......>
Therefore __repr__ is just what it is named, a representation. 
'''
