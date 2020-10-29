class Module:
    
    _validStartCharacterOfCode = ['B', 'E', 'I', 'S']
    
    def __init__(self, code, level):
        self._code = code
        self._list = Module._validStartCharacterOfCode
        if self._code[0] not in Module._validStartCharacterOfCode:
            self._code[0] = Module._validStartCharacterOfCode[0]
        self._level = level

        
    @property
    def code(self):
        return self._code
    
    @property
    def level(self):
        return self._level
    
    
    @level.setter
    def level(self, newLevel):
        self._level = newLevel
        

    def changeLevelBy(self, changeByLevel):
        self._level = changeByLevel
        if changeByLevel > 0:
            if changeByLevel > 5:
                changeByLevel = 5
            else:
                return changeByLevel
            
        else:
            changeByLevel = 1
        
    def getDiffereceInLevels(self, module):
        difference = self._level - self._module
        return difference
    
    @classmethod
    def addValidStartCharacter(cls, startCharacter):
        cls._validStartCharacterCode.append(startCharacter)
        
    @classmethod
    def removeValidStartCharacter(cls, startCharacter):
        cls._validStartCharacterCode.remove(startCharacter)
    
       
    def __str__(self):
        f'Code: {self._code} Level: {self._level}'
        
        
def m():
    m1 = Module('S123', '3')
    print(m1)
    m2 = Module('B231', '2')
    print(m2)
    m1.changeLevelBy(2)
    m2.changeLevelBy(1)
    print(m1.getDiffereceInLevels(m2.level)
    Module.addValidStartCharacter('T')
    
    
#2b
class Staff:
    _nextStaffId = 1
    
    def __init__(self, name):
        self.staffId = Staff._nextStaffId
        Staff._nextStaffId +=1
        self._name = name 
        self._modules = []
          
    
    def numberOfModule(self):
        return len(self._modules)
    
    def searchModule(self, code):
        pass
    
    def removeModule(self, code):
        pass
    
    
    
class PartTimeStaff(Staff):
    
    _datejoin = datetime.today()
    
    def init(self, name, dateJoined, module):
        super().__init__(name, modules)
        self._dateJoined = PartTimeStaff._datejoin.year - dateJoined.year
        
    def removeModule(self, code):
        search = self.searchModule(code)
        if search is None:
            return False
        
        else:
            if len(self._modules) < self._dateJoined:
                return False 
            
            else:
                self._modules.remove(search)
                return True
            
            
def main():       
p1 = PartTimeStaff('John','01/06/2020',m1)
print(p.removeModule('B231'))
main()
    
    
from abc import ABC, abstractmethod
class StaffManagmentException(Exception):
    pass
        
        
class Staff(ABC):
    def _init_(self, staffId, name, salary):
        self._staffId = staffId
        self._name = name
        self._salary = salary
        
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, newSalary):
        if newSalary <= 0:
            raise StaffManagmentException('Salary cannot be zero or negative')
        self._salary = newSalary
        
    @abstractmethod
    def allowance(self):
        pass
    
    def grossSalary(self):
        pass
    
    
class SupportStaff(Staff):
    _baseAllowance = 200
    
    @property
    def allowance(self):
        return self._baseAllowance * 1.02
    
    def _str_(self):
        return f'{self._baseAllowance}'
    
    
    
class Department:
    
    _staffList = []
    
    def _init_(self, budget, manager):
        self._budget = budget
        self._manager = manager
        
    def addStaff(self, staff):
        if self.grossSalary >= self._budget:
            raise StaffManagmentException('Cannot add staff as budget will be exceeded')
        if self.grossSalary > self._manager.salary:
            raise StaffManagmentException('Staff has more salary than manager')
        return self._staff
        
    def manager(self):
        self._manager = self._staffList    

def main():
    m = SupportStaff(1, 'Peter', 6000)
    d = Department(15000)
    s = SupportStaff(2, 'John', 2000)
    try:
        s.salary = 0
        print(s)
        d.addStaff() = 100
    except StaffManagmentException as e:
        print(e)
main()
    
    
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
class StatsGui:

def __init__(self):
    self._numbers = []
    self.win = tk.Tk()
    self.win.resizable(False, False)
    #setting a window title
    self.win.title("Statistics")
    self.create_widgets()
    self.win.mainloop()

def create_widgets(self):
    #Making a frame of a window for the GUI
    dataFrame = ttk.Frame(self.win)
    dataFrame.grid(column=0, row=0)
    
    inputDataFrame = ttk.Frame(dataFrame)
    #To make a label that says 'Number'
    p1_lbl = ttk.Label(inputDataFrame, text="Number:")
    #Shift to the left
    p1_lbl.pack(side=tk.LEFT)
    
    #Making a input variable for the widget
    self.numValue = tk.StringVar()
    self.numValue_Ety = ttk.Entry(inputDataFrame, width=18,\
    textvariable=self.numValue)
    #Shift entry box to align to the left
    self.numValue_Ety.pack(side=tk.LEFT)
    inputDataFrame.grid(column = 0, row = 0)
    
    actionFrame = ttk.Frame(dataFrame)
    actionFrame.grid(column=0, row=1)
    self.add_btn = ttk.Button(actionFrame, text="Add A Number") #Add a button that says 'Add a number'
    #Shift to the left
    self.add_btn.pack(side = tk.LEFT)
    
    self.statistics_btn = ttk.Button(actionFrame, text="Get Statistics")
    #Shift to the left
    self.statistics_btn.pack(side = tk.LEFT)
    
    outputFrame = ttk.Frame(self.win)
    outputFrame.grid(column=0, row=2, columnspan=2)
    self.output = ScrolledText(outputFrame, width=40, height=10, \
    wrap=tk.WORD)
    self.output.grid(column=0, row=0, sticky='WE', columnspan=2)    
 
       
'''
Created on 21 May 2020

@author: Lester
'''
   