programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", 
                          "Function": "A piece of code that you can easily call over and over again."}

val=programming_dictionary.get("i")
print(val)

for key in  programming_dictionary:
    print(key)
    print(programming_dictionary[key])
    
    
my_dict={}

# nested dict in dict
travel_log={
    "France": {"cities_visited":["Paris","Lolli"]},
    "India": {"cities_visited":["Paris","Lolli"],"hello":5}

}

# nested dict in List

travel_log=[
   {"country" :"France", "cities_visited":["Paris","Lolli"]},
    {"country" :"India","cities_visited":["Paris","Lolli"],"hello":5}
]

