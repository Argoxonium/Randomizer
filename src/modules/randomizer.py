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
        #Use class attribute is none was provided for use outside of class.
        owners: list = owners if owners is not None else self.owners_list
        equipment_owned = owners.count(reviewer)
        match equipment_owned:
            case 0:
                return 3 #Reviewer owns no equipment
            case count if count>=3:
                return 1 #Reviewer owns 3 or more equipment
            case _:
                return 2 #Reviewer owns 1 or 2 equipment.
            
    def remove_group_equipment(self)->pd.DataFrame:
        ...
    
    

        
