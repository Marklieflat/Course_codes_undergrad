class Derivative:
    def __init__(self, polynomial = 0):
        self.polynomial = polynomial

    def setPolynomial(self):
        self.polynomial = input('Enter the polynomial:')
    
    def setVariable(self):
        for i in self.polynomial:
            if i.isalpha():
                self.variable = i
                break
    
    def setPolydict(self):
        self.record = {}
        init = ''
        coefficient = 0
        count = 0
        for i in self.polynomial:
            if i == '-' and self.polynomial.index(i) == 0 and count == 0:
                init += '-'
                count += 1
                continue
            count += 1
            if i.isdigit():
                init += i
            elif i.isalpha():
                try:
                    init = eval(init)
                except:
                    init = eval(init+'1')
                coefficient = init
                init = ''
            elif i in ['+', '-']:
                if coefficient == 0:
                    self.record.update({0:eval(init)})
                else:
                    try:
                        init = eval(init)
                    except:
                        init = 1
                    self.record.update({init:coefficient})
                init = i
                coefficient = 0
            else:
                continue

        if coefficient == 0:
            self.record.update({0:eval(init)})
        else:
            try:
                init = eval(init)
            except:
                init = 1
            self.record.update({init:coefficient})
    
    def setFirstDerivative(self):
        self.firstd = ''
        for key in self.record:
            if key * self.record[key] == 0:
                continue
            if key * self.record[key] < 0:
                s1 = str(key*self.record[key])
            else:
                s1 = '+' + str(key*self.record[key])
            if key == 1:
                s2 = ''
            elif key == 2:
                s2 = '*' + self.variable
            else:
                s2 = '*' + self.variable + '^' + str(key - 1)
            self.firstd += s1 + s2
        if self.firstd[0] == '+':
            self.firstd = self.firstd[1:]
    
    def __str__(self):
        return self.firstd

x = Derivative()
x.setPolynomial()
x.setVariable()
x.setPolydict()
x.setFirstDerivative()
print(x)
