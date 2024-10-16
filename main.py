a=input("Введите вашу строку: ")
print("Ваша строка: ", a)
g=0
for i in a:
    if i=="а" or i=="о" or i=="э" or i=="ю" or i=="я" or i=="у" or i=="е" or i=="ё" or i=="ы" or i=="и" or i=="А" or i=="О" or i=="Э" or i=="Ю" or i=="Я" or i=="У" or i=="Е" or i=="Ё" or i=="И":
        g+=1
print("Количество гласных в вашей строке: ", g)