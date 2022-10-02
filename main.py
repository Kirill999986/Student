class Student():

    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def SetName(self, name):
        return "The name of the student is %s" % name

    def SetAge(self, age):
        return "The age of the student is %s" % age

    def setGroupNumber(self, groupNumber):
        return "The groupNumber of the student is %s" % groupNumber


Vlad = Student("Vlad", 16, "12d")
Misha = Student("Misha", 12, "7a")
Samira = Student("Samira", 10, "10f")
Ivan = Student()
Zoro = Student("Zoro", 20, "12s")
student = input('выберите студента: ')
if student == 'Zoro':
 comand = input('выберите команду: ')
 if comand == 'setNameAge':
   print(Zoro.SetName(input('видите имя: ')))
   print(Zoro.SetAge(input('видите возраст: ')))
 if comand == 'setGroupNumber':
  print(Zoro.setGroupNumber(input('видите номер групы: ')))
 if comand == 'getName':
  print(Zoro.name, Zoro.age, Zoro.groupNumber)
 if comand == 'getAge':
  print(Zoro.age)
 if comand == 'getGroupNumber':
  print(Zoro.groupNumber)
if student == 'Vlad':
 comand = input('выберите команду: ')
 if comand == 'setNameAge':
  print(Vlad.SetName(input('видите имя: ')))
  print(Vlad.SetAge(input('видите возраст: ')))
 if comand == 'setGroupNumber':
  print(Vlad.setGroupNumber(input('видите номер групы: ')))
 if comand == 'getName':
  print(Vlad.name, Vlad.age, Vlad.groupNumber)
 if comand == 'getAge':
  print(Vlad.age)
 if comand == 'getGroupNumber':
  print(Vlad.groupNumber)
if student == 'Samira':
 comand = input('выберите команду: ')
 if comand == 'setNameAge':
  print(Samira.SetName(input('видите имя: ')))
  print(Samira.SetAge(input('видите возраст: ')))
 if comand == 'setGroupNumber':
  print(Samira.setGroupNumber(input('видите номер групы: ')))
 if comand == 'getName':
  print(Samira.name, Samira.age, Samira.groupNumber)
 if comand == 'getAge':
  print(Samira.age)
 if comand == 'getGroupNumber':
  print(Samira.groupNumber)
if student == 'Misha':
 comand = input('выберите команду: ')
 if comand == 'setNameAge':
  print(Misha.SetName(input('видите имя: ')))
  print(Misha.SetAge(input('видите возраст: ')))
 if comand == 'setGroupNumber':
  print(Misha.setGroupNumber(input('видите номер групы: ')))
 if comand == 'getName':
  print(Misha.name, Misha.age, Misha.groupNumber)
 if comand == 'getAge':
  print(Misha.age)
 if comand == 'getGroupNumber':
  print(Misha.groupNumber)
if student == 'Ivan':
 comand = input('выберите команду: ')
 if comand == 'setNameAge':
  print(Ivan.SetName(input('видите имя: ')))
  print(Ivan.SetAge(input('видите возраст: ')))
 if comand == 'setGroupNumber':
  print(Ivan.setGroupNumber(input('видите номер групы: ')))
 if comand == 'getName':
  print(Ivan.name, Ivan.age, Ivan.groupNumber)
 if comand == 'getAge':
  print(Ivan.age)
 if comand == 'getGroupNumber':
  print(Ivan.groupNumber)