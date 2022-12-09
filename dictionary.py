#Dictionay-used to store values in key:value pairs
#ordered
#changable
#does not allow duplicate values
# mydictionary={
#     "name":"Rajesh",
#     "age":"18",
#     "percentage":"19"
# }
#  age1=mydictionary.get("age")
# keys=mydictionary.keys()
#items=mydictionary.items()
#values=mydictionary.values()
# print(keys)
# mydictionary["roll number"]=21
# print(mydictionary)

# myDictionary={
#     "name":"Rajesh",
#     "age":"18",
#     "percentage":94.5
# }
# print(myDictionary)
# # myDictionary.update({"age":19})
# myDictionary.popitem()
# myDictionary.pop("age")
# print(myDictionary)


# dict1={"one":1,"two":2,"three":3}
# dict2={"four":4,"five":5,"six":6}
# #merge two dictionaries in one
# dict3=dict1|dict2
# print(dict3)


dict1 = {
    "class":{
        "student":{
            "name":"xyz",
            "marks":{
                "python":100,
                "web":90
            }
        }
    }
}
print(dict1.get("class").get("student").get("marks").get("web"))