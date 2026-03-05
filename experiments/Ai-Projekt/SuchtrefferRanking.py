query = "resume python basics"

items = [
  {"id": 101, "title": "Python Basics – A Résumé", "tags": ["python", "beginner"]},
  {"id": 102, "title": "Advanced Python Metaprogramming", "tags": ["python", "advanced"]},
  {"id": 103, "title": "Writing a Resume that Works", "tags": ["career", "resume"]},
  {"id": 104, "title": "The Basics of Cooking", "tags": ["cooking", "basics"]},
  {"id": 105, "title": "Data Science with PyThon", "tags": ["python", "data"]},
]

# TODO find out, which tags fit the best
# TODO We want to check if a string is inside another string
# TODO We need to get the string from a position of the List and compare it to the string if the stuff inside of the array

# TODO making a 2d array
n = len(items)
word_list = [[0] *n for _ in range(2)]
print(word_list)

# TODO We now, need to sort the titles in the first line of the Array

title = t.get("title", "")

# TODO We need to iterate that trough the List and check which score is the highest