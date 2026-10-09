""" Question 4  -  JSON file   [20 marks]
1. Make a dictionary about YOURSELF with these keys: name, city, skills (skills must be a list of 3 things you can do).
2. Save it to profile.json using the json module.
3. Read profile.json back into a new variable.
4. Print the SECOND skill from the list.
5. Add a new key course with the value Agentic AI, then save the file again.
6. Print the final dictionary.

Marks: dictionary built correctly (4), saved to file (5), read back (5), second skill printed (3), new key added and re-saved (3).
"""

import json

#create a dic
dict_profile={"name": "Anuj", "city": "Delhi", "skills": ["Python", "JavaScript", "SQL"]}

# Save to JSON file
with open("profile.json", "w") as file:
    json.dump(dict_profile, file)

# Read JSON file
with open("profile.json", "r") as file:
    dict_profile = json.load(file)

# Print the second skill
print(f"Second skill: {dict_profile['skills'][1]}")

# Add new key
dict_profile["course"] = "Agentic AI"

# Save the updated dictionary to the JSON file
with open("profile.json", "w") as file:
    json.dump(dict_profile, file)

# Print the final dictionary
print(f"Final dictionary: {dict_profile}")