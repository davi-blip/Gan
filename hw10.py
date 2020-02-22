class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def get_real(self):
        return self.real

    def get_imag(self):
        return self.imag

    def set_real(self,new_real):
        self.real = new_real

    def set_imag(self,new_imag):
        self.imag = new_imag
    
    def __str__(self):
        return str(self.real)+' '+ '+' +' '+ str(self.imag)+'i'

    def __add__(self,other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self,other):
        return Complex(self.real*other.real-self.imag*other.imag, self.real * other.imag + other.real*self.imag)

    def __eq__(self,other):
        if self.real == other.real and self.imag == other.imag:
            return True
        else:
            return False


class Employee:
    def __init__(self,classes):
        classes = classes.split(',')
        self.name = classes[0]
        self.position = classes[1]
        self.salary = float(classes[2])
        self.seniority = float(classes[3])
        self.value = float(classes[4])

    def __str__(self):
        return (str(self.name))+','+(str(self.position))

    def net_value(self):
        return round(self.value - self.salary,2)

    def __lt__(self,other):
        if (self.value - self.salary)<(other.value - other.salary):
            return True
        else:
            return False


class Branch:
    def __init__(self,fname):
        ls = []
        with open(fname,'r') as f:
            for lines in f:
                ls.append(lines)
        self.team = []
        for col in ls[3:]:
            self.team.append(Employee(col))
        print(self.team)
        
        for col in ls[0:1]:
            a = col.split(',')
            self.location = a[1]
            
        
        for col in ls[1:2]:
            a = col.split(',')
            self.upkeep=a[1]
            
        
    def __str__(self):
        result = str(self.location) + '\n'
        for e in range (len(self.team)):
            result += str(self.team[e]) + '\n'
        return result

    def profit(self):
        net_value = 0
        for e in self.team:
            net_value += e.net_value()
        return round(net_value - float(self.upkeep),2)

    def __lt__(self,other):
        if self.profit() < other.profit():
            return True
        else:
            return False

    def cut(self,num):
        employees = sorted(self.team)
        self.team = employees[num:]
            
        


class Company:
    def __init__(self,name,branches):
        self.name = name
        self.branches = branches

        

    def __str__(self):
        result = str(self.name) + '\n\n' + str(b1) + '\n' + str(b2) + '\n' + str(b3) + '\n'+ str(b4)
        
        return result

    def synergize(self:
        self.branches.sort()
        lowest_branches = self.branches[0]
        cut_employees = len(lowest_branches.team) // 2
        self.branches[0].cut(cut_employees)
        
        
        
        
                

