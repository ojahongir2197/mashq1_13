1
print("1")
my_tuple = (5, 10, 15, 20)

print("Tuple uzunligi:", len(my_tuple))
print("Uchinchi element:", my_tuple[2])
print("15 tuple ichida bormi?", 15 in my_tuple)


# 2
print("\n2")
colors = ('red', 'blue', 'green')

colors_list = list(colors)
colors_list.append('yellow')
colors_list.remove('blue')
colors_list.sort()

print("Yakuniy ro‘yxat:", colors_list)


#3
print("\3")
numbers = (3, 7, 2, 9, 4)

total = sum(numbers)
print("Yig‘indi:", total)

if total % 2 == 0:
    print("Yig‘indi juft")
else:
    print("Yig‘indi toq")


#4
print("\4")
items = (1, 2, 2, 3, 3, 4, 1)

unique_items = list(set(items))
unique_items.sort()

print("Takrorlarsiz tartiblangan ro‘yxat:", unique_items)

#5
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

new_tuple = tuple1 + tuple2
print("Yangi tuple:", new_tuple)
print("Elementlar soni:", len(new_tuple))
print("Oxirgi element:", new_tuple[-1])

print("-----")

#6
values = (12, 5, 8, 19, 3, 15)

max_val = max(values)
min_val = min(values)
print("Eng katta:", max_val)
print("Eng kichik:", min_val)
print("Farqi:", max_val - min_val)

print("-----")

#7
words = ('apple', 'banana', 'cherry', 'date')

reversed_words = words[::-1]
print("Teskari tuple:", reversed_words)
print("Birinchi element:", reversed_words[0])
print("Oxirgi element:", reversed_words[-1])

print("-----")

#8
data = (10, 20, 30, 40, 50)

if 30 in data:
    print("30 mavjud")
    print("Indeksi:", data.index(30))
else:
    print("Element topilmadi")
