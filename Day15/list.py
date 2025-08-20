StatesOfAmerica = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin"]

# Accessing elements in the list
print(StatesOfAmerica[2]) # Accessing the third state
print(StatesOfAmerica[2][2]) # Accessing the third character of the third state
print(StatesOfAmerica[-1]) # Accessing the last state
print(StatesOfAmerica[-1][-1]) # Accessing the last character of the last state
print(StatesOfAmerica[0:5]) # Slicing the first five states
print(StatesOfAmerica[5:10]) # Slicing states from index 5 to 9
print(StatesOfAmerica[5:]) # Slicing from index 5 to the end
print(StatesOfAmerica[:5]) # Slicing from the start to index 4
print(StatesOfAmerica[-5:-8]) # Slicing the last five states in reverse order
print(StatesOfAmerica[-5:]) # Slicing the last five states
print(StatesOfAmerica[:-5]) # Slicing all states except the last five
print(StatesOfAmerica[::2]) # Slicing every second state
print(StatesOfAmerica[::-1]) # Slicing the list in reverse order
print(StatesOfAmerica[::-2]) # Slicing the list in reverse order, taking every second state
print(StatesOfAmerica[1:10:2]) # Slicing from index 1 to 9, taking every second state
print(StatesOfAmerica[1:10:3]) # Slicing from index 1 to 9, taking every third state

# Modifying the list
StatesOfAmerica[0] = "New Alabama" # Changing the first state
StatesOfAmerica[1:3] = ["New Alaska", "New Arizona"] # Changing the second and third states
StatesOfAmerica.append("Wyoming") # Adding a new state at the end
StatesOfAmerica.insert(0, "New State") # Inserting a new state at the beginning
StatesOfAmerica.extend(["New State 1", "New State 2"]) # Extending the list with multiple new states
StatesOfAmerica.remove("New State") # Removing a specific state
StatesOfAmerica.pop() # Removing the last state
StatesOfAmerica.pop(0) # Removing the first state
StatesOfAmerica.clear() # Clearing the entire list
print(StatesOfAmerica) # Printing the empty list after clearing
