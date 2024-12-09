import random
import pandas as pd


import random
import pandas as pd

class RandomReviewers:
    def __init__(self, equipment: pd.DataFrame, groups: pd.DataFrame) -> None:
        self.employee_list: list = []
        self.exclusion_list: list = []
        self.owners_list: list = []
        self.groups: pd.DataFrame = groups
        self.equipment: pd.DataFrame = equipment

    def choose_reviewer(self, employees: list = None, exclusions: list = None) -> str:
        """
        Randomly selects a reviewer from a list of employees, excluding specified individuals.
        This wont add reviewer to the exclusion list as this should be confirmed first.

        Args:
            employees (list): A list of employee names.
            exclusions (list): A list of names to exclude from selection.

        Returns:
            str: The name of the selected reviewer.
        """
        # Use class attributes if no arguments are provided
        employees = employees if employees is not None else self.employee_list
        exclusions = exclusions if exclusions is not None else self.exclusion_list

        # Validate inputs
        if not employees:
            raise ValueError("Employee list cannot be empty.")
        if exclusions is None:
            exclusions = []

        # Filter the list to exclude the names in the exclusions list
        eligible_employees = [employee for employee in employees if employee not in exclusions]

        # Check if there are eligible employees to choose from
        if not eligible_employees:
            raise ValueError("No eligible employees available for selection.")

        # Randomly select a reviewer
        reviewer = random.choice(eligible_employees)

        return reviewer
    
    def determine_review_number(self, reviewer:str, owners:list = None)->int:
        """
        Determines the maximum number of reviews a reviewer should handle based on ownership.

        Args:
            reviewer (str): The name of the reviewer.
            owners (list): A list of equipment owners. Defaults to self.owners_list if not provided.

        Returns:
            int: The maximum number of reviews the reviewer should handle.
        """
        #TODO count alternates when active.
        #Use class attribute is none was provided for use outside of class.
        owners: list = owners if owners is not None else self.owners_list
        equipment_owned = owners.count(reviewer)
        match equipment_owned:
            case 0:
                return 3 #Reviewer owns no equipment
            case count if count>3:
                return 0 #Reviewer owns more than three equipment they are exempt from the process.
            case 3:
                return 1
            case _:
                return 2 #Reviewer owns 1 or 2 equipment.
            
    def remove_group_equipment(self, reviewer: str) -> pd.DataFrame:
        """
        Removes all equipment owned by members of the reviewer's group from the equipment list.

        Args:
            reviewer (str): The name of the selected reviewer.

        Returns:
            pd.DataFrame: A filtered DataFrame of equipment excluding items owned by the reviewer's group.
        """
        # Identify the group the reviewer belongs to
        reviewer_group = self.groups.loc[self.groups['Name'] == reviewer, 'Group'].values

        if len(reviewer_group) == 0:
            raise ValueError(f"Reviewer {reviewer} does not belong to any group.")

        reviewer_group = reviewer_group[0]

        # Get the list of group members
        group_members = self.groups[self.groups['Group'] == reviewer_group]['Name'].tolist()

        # Remove equipment owned by group members
        filtered_equipment = self.equipment[~self.equipment['Owner'].isin(group_members)]

        return filtered_equipment

    def choose_equipment(self, equipment_df: pd.DataFrame) -> str:
        """
        Randomly selects a piece of equipment for a reviewer to review.

        Args:
            equipment_df (pd.DataFrame): The filtered DataFrame of available equipment.

        Returns:
            str: The ID of the selected equipment.
        """
        # Validate the input DataFrame
        if equipment_df.empty:
            raise ValueError("No equipment available for selection.")

        # Randomly select a piece of equipment
        selected_equipment = equipment_df.sample(n=1).iloc[0]['Equipment']

        return selected_equipment

    


        
