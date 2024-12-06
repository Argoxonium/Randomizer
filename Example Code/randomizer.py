import random
import pandas as pd

def load_data(employee_file, equipment_file):
    # Load employee and equipment data
    employees = pd.read_csv(employee_file)
    equipment = pd.read_csv(equipment_file)
    return employees, equipment

def assign_reviewers(employees, equipment):
    assignments = []
    
    for _, row in equipment.iterrows():
        equipment_id = row['Equipment']
        owner = row['Owner']
        owner_group = employees.loc[employees['Name'] == owner, 'Group'].values[0]

        # Exclude reviewers from the same group as the owner
        eligible_reviewers = employees[employees['Group'] != owner_group]

        # Weight reviewers by group size
        weights = eligible_reviewers['Group'].value_counts(normalize=True)
        weighted_reviewers = eligible_reviewers.sample(weights=weights)

        # Select a reviewer with limits
        selected_reviewer = None
        for reviewer in weighted_reviewers['Name']:
            if reviewer_can_review(reviewer, assignments):  # Check review limits
                selected_reviewer = reviewer
                break

        # Assign reviewer
        if selected_reviewer:
            assignments.append({
                'Equipment': equipment_id,
                'Owner': owner,
                'Reviewer': selected_reviewer
            })

    return pd.DataFrame(assignments)

def reviewer_can_review(reviewer, assignments, max_reviews=3):
    # Check if the reviewer has hit their limit
    review_count = sum(1 for a in assignments if a['Reviewer'] == reviewer)
    return review_count < max_reviews

def export_to_excel(assignments, output_file):
    # Export assignments to Excel
    assignments.to_excel(output_file, index=False)

# Main script
if __name__ == "__main__":
    employees, equipment = load_data('data/employees.csv', 'data/equipment.csv')
    assignments = assign_reviewers(employees, equipment)
    export_to_excel(assignments, 'output/assignments.xlsx')
