with open ('recipe.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        quantity_ing = int(file.readline())
        ingredients_list = []
        for ing in range(quantity_ing):
            ingredients = file.readline().strip()
            prod, num, meas = ingredients.split(' | ')
            ingredients_list.append({'ingredient_name': prod, 'quantity': num, 'measure': meas})
        file.readline()
        cook_book[dish_name] = ingredients_list

# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count, book=cook_book):
    res = {}
    for dish in dishes:
        value = book.get(dish)
        for dicts in value:
            if dicts.get('ingredient_name') not in res.keys():
                res[dicts.get('ingredient_name')] = {'measure': dicts.get('measure'),\
'quantity': int(dicts.get('quantity')) * int(person_count)}
            elif dicts.get('ingredient_name') in res.keys():
                res[dicts.get('ingredient_name')].update({'quantity': (res[dicts.get('ingredient_name')].get('quantity')\
+ int(dicts.get('quantity')) * int(person_count))})
            else:
                print('Ошибка')
    return print(res)

# get_shop_list_by_dishes(['Фахитос', 'Омлет', 'Утка по-пекински'], 1)




        

