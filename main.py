a=input("Введите вашу строку: ") #Ввод строки с клавиатуры
print("Ваша строка: ", a) #Вывод строки на консоль
g=0 #Переменная для подсчета гласных
for i in a: #Цикл for для перебора элементов строки
    #Цикл if для определения является ли символ гласным
    if i=="а" or i=="о" or i=="э" or i=="ю" or i=="я" or i=="у" or i=="е" or i=="ё" or i=="ы" or i=="и" or i=="А" or i=="О" or i=="Э" or i=="Ю" or i=="Я" or i=="У" or i=="Е" or i=="Ё" or i=="И":
        g+=1 #Увеличение переменной на 1 при верности условия
print("Количество гласных в вашей строке: ", g) #Вывод на консоль количества гласных
