# dictionary with multiple inputs in a key

# function to add multiple values
def add_values_in_dict(dic, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in dic:
        dic[key] = list()
    dic[key].extend(list_of_values)
    return dic
 
# dictionary containing states and its cities
places = {("Maharashtra"):["Mumbai","Pune","Nagpur"],
          ("Madhya Pradesh"):["Delhi","Bhopal","Indore"]}
 
print(places)
print('\n')

#adding values
add_val=add_values_in_dict(places, "Madhya Pradesh", ["Ujjain", "Sagar"])
print("After adding values")
print(add_val)