#Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую
# True, если год високосный, и False иначе.




def is_year_leap(x):
    if x % 4 != 0 or x % 100 == 0 and x % 400 != 0:
        print("False")
    else:
        print("True")






is_year_leap(1860)