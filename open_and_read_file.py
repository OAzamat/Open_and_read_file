import json
import pprint
import os

# Homework 1
with open('/Users/azamatodilbekov/Desktop/pythonProjects/Python/OOP_and_API/dishes.text', 'r', encoding='utf-8') as f:   
    cook_book = {}
    for dishies_name in f:
        cook_ingredient = int(f.readline())
        cook_n_list = []
        for i in range(cook_ingredient):
            name, quantity, measure = f.readline().strip().split('|')
            cook_n_list.append({
                'ingredient_name': name,
                'quantity_ingr': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[dishies_name.strip()] = cook_n_list
    res = json.dumps(cook_book, indent=2)
    # print(cooks)

for key, value in cook_book.items():
  print(f' \n{key}')
  for key in value:
    print(f'{key}')
print('--------------Задача 1----------------')


# HOMEWORK 2
def get_shop_list_by_dishes(dishies, person_count): 
    shop_list = {}
    for dish in dishies:
        for dish in cook_book.keys():
            res = cook_book.get(dish)
            for el in dish:
                if el['ingredient_name'] not in shop_list.keys():
                    shop_list.update([el]['ingredient_name']['quantity'] == int(shop_list[el]['ingredient_name']['quantity']) + int(el['quantity']) * person_count)

    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))




# HOMEWORK 3
with open('1.text', encoding='utf-8') as f1,open('2.text', encoding='utf-8') as f2,open ('3.text', encoding='utf-8') as f3: 
    text1 = f1.readlines()
    text1.insert(0, os.path.basename(r'1.text'))
    text2 = f2.readlines()
    text2. insert(0, os.path.basename(r'2.text'))
    text3 = f3.readlines()
    text3.insert(0, os.path.basename(r'3.text'))

with open('4.text', 'w', encoding='utf-8') as f4:
    text4 = [text1, text2, text3]
    text4.sort(key=len)
    for text in text4:
        f4.write(text[0])
        f4.write("\n")
        f4.write(str(len(text[1:])))
        f4.write("\n")
        f4.writelines(text[1:])
        f4.write("\n")