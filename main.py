from character import Student
from character import Student2
from character import Student3
from character import Student4
from character import Student5
player1 = Student()
player2 = Student2()
player3 = Student3()
player4 = Student4()
player5 = Student5()
student = int(input('виберите студента: '))
if student == 1:
 comand = input('в видите команду: ')
 if comand == 'getName':
    print(player1.stats())
 if comand == 'getAge':
    print(player1.stat1())
 if comand == 'setGroupNumber':
    print(player1.stat2())
 if comand == 'SetNameAge':
    age = int(input('видите возраст: '))
    player1.take_age(age)
    name = input('видите имя: ')
    print(player1.stats())
    player1.take_name(name)
 if comand == 'setGroupNumber':
    groupNumber = input('видите группу: ')
    player1.take_groupNumber(groupNumber)
    print(player1.stats())
if student == 2:
 comand = input('в видите команду: ')
 if comand == 'getName':
    print(player2.stats2())
 if comand == 'getAge':
    print(player2.stat12())
 if comand == 'setGroupNumber':
    print(player2.stat22())
 if comand == 'SetNameAge':
    age2 = int(input('видите возраст: '))
    player2.take_age2(age2)
    name2 = input('видите имя: ')
    print(player2.stats2())
    player2.take_name2(name2)
 if comand == 'setGroupNumber':
    groupNumber2 = input('видите группу: ')
    player2.take_groupNumber2(groupNumber2)
    print(player2.stats2())
if student == 3:
 comand = input('в видите команду: ')
 if comand == 'getName':
    print(player3.stats3())
 if comand == 'getAge':
    print(player3.stat13())
 if comand == 'setGroupNumber':
    print(player3.stat23())
 if comand == 'SetNameAge':
    age3 = int(input('видите возраст: '))
    player3.take_age3(age3)
    name3 = input('видите имя: ')
    print(player3.stats3())
    player3.take_name3(name3)
 if comand == 'setGroupNumber':
    groupNumber3 = input('видите группу: ')
    player3.take_groupNumber3(groupNumber3)
    print(player3.stats3())
if student == 4:
 comand = input('в видите команду: ')
 if comand == 'getName':
    print(player4.stats())
 if comand == 'getAge':
    print(player4.stat14())
 if comand == 'setGroupNumber':
    print(player4.stat24())
 if comand == 'SetNameAge':
    age4 = int(input('видите возраст: '))
    player4.take_age4(age4)
    name4= input('видите имя: ')
    print(player4.stats4())
    player4.take_name4(name4)
 if comand == 'setGroupNumber':
    groupNumber4 = input('видите группу: ')
    player4.take_groupNumber4(groupNumber4)
    print(player4.stats4())
if student == 5:
 comand = input('в видите команду: ')
 if comand == 'getName':
    print(player5.stats5())
 if comand == 'getAge':
    print(player5.stat15())
 if comand == 'setGroupNumber':
    print(player5.stat25())
 if comand == 'SetNameAge':
    age5 = int(input('видите возраст: '))
    player5.take_age5(age5)
    name5 = input('видите имя: ')
    print(player5.stats5())
    player5.take_name5(name5)
 if comand == 'setGroupNumber':
    groupNumber5 = input('видите группу: ')
    player5.take_groupNumber5(groupNumber5)
    print(player5.stats5())