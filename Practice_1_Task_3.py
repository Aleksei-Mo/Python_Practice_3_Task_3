#Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число 
# его повторений (без учёта регистра) в формате "слово количество".
import json

def ChangeStrLetters(str,code):
    match code:
        case 1:
            str=str.title()
        case 2:
            str=str.lower()
        case 3:
            str=str.upper()
        case 4:
            str=str.swapcase()
        case 5:
            str=str.capitalize()
    return str

def FindCopies(my_list,listItem):
    counter=my_list.count(listItem)
    return counter

def ListStatistics(my_list):
    statistics={}
    for i in my_list:
        copiesNumber=FindCopies(my_list,i)
        statistics[i]=copiesNumber
    return statistics

def PrintResult(dictionary):
    for key,value in dictionary.items():
        print(f"Element '{key}' occurs in the entered string {value} times;")

def LogToFile(data):
    with open('statistics.txt', 'a') as dataFile:
         json.dump(data, dataFile)
    print("File 'statistics.txt' was updated successfully.")

my_str=input("Enter your string. Use the whitespace to separate elements.: ")
my_list=my_str.split()
print(f"You entered the following string: {my_str}")
print(f"See statistics below:")
result=ListStatistics(my_list)
PrintResult(result)
print()
LogToFile(result)