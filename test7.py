import json

customer = {
    "id" : 123344,
    "history" : [
            {"date" : "2015-01-11", "item" : "itm01"},
            {"date" : "2015-02-11" , "item" : "itm02"}
        ]        
            }

jsonString = json.dumps(customer,indent=4)
dic = json.loads(jsonString)

ex_list = ["a","b","c","d","e","a","a","c","d","e"]

print ex_list

list = list(set(ex_list))

print list
