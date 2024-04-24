#!/usr/bin/python3

my_list = [
    {"name": "ilias", "age": 27, "sexe": "male"},
    {"name": "yasmine", "age": 19, "sexe": "female"},
    {"name": "arbouba", "age": 19, "sexe": "female"}
]

sorted_list = sorted(lambda my_list: my_list["name"])

print(my_list)
    
