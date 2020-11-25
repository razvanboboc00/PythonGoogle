# declararea unei liste care să conțină elementele 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (în această ordine)

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)

# afișarea unei alte liste ordonată ascendent (lista inițială trebuie păstrată în aceeași formă)

my_list_copy = my_list.copy()
my_list_copy.sort()
print(my_list_copy)

# afișarea unei liste ordonată descendent (lista inițială trebuie păstrată în aceeași formă)

my_list_copy_2 = my_list.copy()
my_list_copy_2.sort()
my_list_copy_2.reverse()
print(my_list_copy_2)

# afișarea numerelor pare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

print(my_list_copy[1:10:2])

# afișarea numerelor impare din listă (folosind DOAR slice, altă metodă va fi considerată invalidă)

print(my_list_copy[::2])

# afișarea elementelor multipli ai lui 3

print(my_list_copy[2:10:3])
