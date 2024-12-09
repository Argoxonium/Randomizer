from src.modules.randomizer import RandomReviewers
import pandas as pd

# Example data
equipment_df = pd.DataFrame({
    "Equipment": ["E1", "E2"],
    "Owner": ["Alice", "Bob"]
})

groups_df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Group": ["Group1", "Group1", "Group2", "Group2", "Group3"]
})

# Instantiate the RandomReviewers class
randomizer = RandomReviewers(equipment=equipment_df, groups=groups_df)

# Populate the class's employee list and exclusion list
randomizer.employee_list = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
randomizer.exclusion_list = ["Alice"]

# Use the choose_reviewer function
try:
    selected_reviewer = randomizer.choose_reviewer()
    print(f"Selected Reviewer: {selected_reviewer}")
except ValueError as e:
    print(f"Error: {e}")

### Test 2 ###
# Example owners list
owners_list = ["Alice", "Bob", "Alice", "Alice", "Charlie"]

# Class attribute
randomizer.owners_list = owners_list

# Determine review numbers
print(randomizer.determine_review_number("Alice"))  # Output: 1 (owns 3+ equipment)
print(randomizer.determine_review_number("Bob"))    # Output: 2 (owns 1 equipment)
print(randomizer.determine_review_number("Eve"))    # Output: 3 (owns 0 equipment)

## TEST 3
# Example data
equipment_df = pd.DataFrame({
    "Equipment": ["E1", "E2", "E3", "E4"],
    "Owner": ["Alice", "Bob", "Charlie", "Diana"]
})

groups_df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "Group": ["Group1", "Group1", "Group2", "Group2", "Group3"]
})

# Instantiate the RandomReviewers class
randomizer = RandomReviewers(equipment=equipment_df, groups=groups_df)

# Selected reviewer
selected_reviewer = "Bob"

# Remove equipment owned by members of the selected reviewer's group
filtered_equipment = randomizer.remove_group_equipment(selected_reviewer)

print(filtered_equipment)

## Test 4
# Example data
filtered_equipment = pd.DataFrame({
    "Equipment": ["E3", "E4"],
    "Owner": ["Charlie", "Diana"]
})

# Select a piece of equipment
try:
    selected_equipment = randomizer.choose_equipment(filtered_equipment)
    print(f"Selected Equipment: {selected_equipment}")
except ValueError as e:
    print(f"Error: {e}")
