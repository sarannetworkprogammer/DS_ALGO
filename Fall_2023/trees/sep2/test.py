

dict1 = {"a":[1]}

if "a" not in dict1:
    dict1["a"] = [1]
else:

    dict1["a"].append(2)


print(dict1)