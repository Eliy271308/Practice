#Написать функцию date, принимающую 3 аргумента — день, месяц и год.
# Вернуть True, если такая дата есть в нашем календаре, и False иначе.



def date(day, month, year):
        if year < 0:
            return False
        elif year % 4 == 0:
            if 1 <= month <= 12:
                if month == 2:
                    if 1 <= day <= 29:
                        return True
                    else:
                        return False
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    if 1 <= day <= 30:
                        return True
                    else:
                        return False
                else:
                    if 1 <= day <= 31:
                        return True
                    else:
                        return False
            else:
                return False
        else:
            if 1 <= month <= 12:
                if month == 2:
                    if 1 <= day <= 28:
                        return True
                    else:
                        return False
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    if 1 <= day <= 30:
                        return True
                    else:
                        return False
                else:
                    if 1 <= day <= 31:
                        return True
                    else:
                        return False
            else:
                return False









