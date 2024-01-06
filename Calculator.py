class Calc:
    'Calculator'
    def __init__(self, a, b):
        'initialize values'
        self.value1=a
        self.value2=b

    def add(self):
         'addiation a+b =result'

         return self.value1 + self.value2


    def multiply(self):
        'multiplication a*b = result'

        return self.value1*self.value2
    def division(self):
        'division a/b = result'
        if v2 == 0:
            return print("Cannot divide by zero!")

        else:
             return self.value1/self.value2

print('Chose add(1) , multiply(2), division(3)')
Selection =input('1 , 2, 3')

v1= int(input('firt value'))
v2=int(input('second value'))
C1 =Calc(v1,v2)
if Selection=='1':
    add_result= C1.add()
    print('Add: {}'.format(add_result))

elif Selection =='2':

    multiply_result= C1.multiply()
    print('Multiply: {}'.format(multiply_result))

elif Selection == '3':
    division_result = C1.division()
    print('Division: {}'.format(division_result))
else:
    print('You have to choose 1, 2 or 3')