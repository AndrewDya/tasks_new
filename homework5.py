my_list = ["apple", "banana", "orange", "kiwis", "potato"]
print(my_list)
print(my_list[0], my_list[-1])
print(my_list[2:5])
my_list[2] = "avocado"
print(my_list)

my_dict = {
    "яблоко": "apple",
    "книга": "book",
    "машина": "car",
    "солнце": "sun",
    "дом": "house"
}

print(my_dict)
print(my_dict.get("яблоко"))
my_dict["яблоко"] = "apple fruit"
my_dict["ягода"] = "berry"
print(my_dict)
