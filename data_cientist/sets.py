#Sets are a type of collection, They are unordered, only have unique elements
set_1 = {"pop", "rock", "bob", "rock", "pop", "bob"}
print(set_1) #output {'pop', 'rock', 'bob'}

#This is a list
list_example = ["pop", "rock", "bob", "rock", "pop", "bob","pop", "rock", "bob", "rock", "pop", "bob","pop", "rock", "bob", "rock", "pop", "bob"]
#We create a set in base to list
list_to_set = set(list_example)
print(list_to_set)

#Use .add to add a new value
set_1.add("NY") 
print(set_1)

#Use .remove to remove a value
set_1.remove("NY") 
print(set_1)


# Define the set
set_1 = {"NY", "CA", "TX"}
# Check if the value "NY" is in the set
is_in_set = "NA" in set_1 # Output True or False
# Print the result
print(is_in_set)  # This will print True if "NY" is in set_1, otherwise it will print False
# Print the set
print(set_1)


# Define the first set
set_1 = {"NY", "CA", "TX"}
# Define the second set
set_2 = {"TX", "FL", "NY"}
# Find the intersection of set_1 and set_2
intersection = set_1 & set_2
# Print the result
print(intersection)  # This will print {'NY', 'TX'}


# Define the first set
set_1 = {"NY", "CA", "TX"}
# Define the second set
set_2 = {"FL", "GA", "NV"}
# Find the intersection of set_1 and set_2
intersection = set_1 & set_2
# Print the result
print(intersection)  # This will print set(), which means an empty set



# Define the first set
set_1 = {"NY", "CA", "TX"}
# Define the second set
set_2 = {"FL", "GA", "TX"}
# Find the union of set_1 and set_2
union_set = set_1.union(set_2)
# Print the result
print(union_set)  # This will print {'NY', 'CA', 'TX', 'FL', 'GA'}


# Define the first set
set_1 = {"NY", "CA", "TX"}
# Define the second set
set_2 = {"FL", "GA", "TX"}
# Find the union of set_1 and set_2
union_set = set_1.union(set_2)
# Convert the set to a sorted list to maintain a specific order
ordered_union_list = sorted(union_set)
# Print the result
print(ordered_union_list)  # This will print ['CA', 'FL', 'GA', 'NY', 'TX']




# Define the first set
set_1 = {"NY", "CA", "TX"}
# Define the second set
set_2 = {"NY", "CA", "TX", "FL", "GA"}
# Check if set_1 is a subset of set_2
is_subset = set_1.issubset(set_2)
# Print the result
print(is_subset)  # This will print True because all elements of set_1 are in set_2



# Define the first set
set_1 = {"NY", "CA", "TX"}
# Define the second set
set_2 = {"FL", "GA"}
# Check if set_1 is a subset of set_2
is_subset = set_1.issubset(set_2)
# Print the result
print(is_subset)  # This will print False because not all elements of set_1 are in set_2



# Define the first set (subset)
set_1 = set()  # Empty set
# Define the second set
set_2 = {"NY", "CA", "TX", "FL", "GA"}
# Check if set_1 is a subset of set_2
is_subset = set_1.issubset(set_2)
# Print the result
print(is_subset)  # This will print True because the empty set is a subset of any set
