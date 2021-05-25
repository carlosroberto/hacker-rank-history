"""
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.

This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

Task

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

Input Format

Read

, the year to test.

Constraints

Output Format

The function must return a Boolean value (True/False). Output is handled by the provided code stub.

Sample Input 0

1990

Sample Output 0

False

Explanation 0

1990 is not a multiple of 4 hence it's not a leap year. 

---

Feitas as correções de calendário definiu-se a nova regra para o cálculo dos anos bissextos:

    De 4 em 4 anos é ano bissexto.
    De 100 em 100 anos não é ano bissexto.
    De 400 em 400 anos é ano bissexto.
    Prevalecem as últimas regras sobre as primeiras.[2]

Para melhor entender

    São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
    São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, p.ex: 1996, 2000, 2004, 2008, 2012, 2016, 2020...
    Não são bissextos todos os demais anos.

Essa regra aproxima o ano trópico pelo valor de 365,2425 dias.

Em função da nossa longevidade média, é comum e compreensível que nos lembremos apenas da primeira regra, a de quatro em quatro anos, embora a correção dos anos bissextos seja mais complexa.

Como curiosidade, o ano de 2000 foi o segundo ano em que a terceira regra foi aplicada. Contudo, como foi ano bissexto, o ano de 1900 foi a última vez que a regra da divisão por 100 foi aplicada até os dias atuais; a próxima ocorrerá apenas em 2100. 


"""




def is_leap(year):
    leap = False
    
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    else:
        leap = False    
    
    return leap

year = int(input())
print(is_leap(year))



"""
According to these rules, the years 1992, 2000 and 2400 are leap years,
while 1800, 1900, 2100, 2200, 2300, and 2500 are not leap years.

if __name__ == "__main__":
    for i in list([1992, 2000, 2400, 1800, 1900, 2100, 2200, 2300, 2500]):
        print(str(i) + " is " + str(is_leap(i)))
"""        

