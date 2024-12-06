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
randomizer.exclusion_list = ["Alice", "Diana"]

# Use the choose_reviewer function
try:
    selected_reviewer = randomizer.choose_reviewer()
    print(f"Selected Reviewer: {selected_reviewer}")
except ValueError as e:
    print(f"Error: {e}")
