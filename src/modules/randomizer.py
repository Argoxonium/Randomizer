import random
import pandas as pd


import random
import pandas as pd

class RandomReviewers:
    def __init__(self, equipment: pd.DataFrame, groups: pd.DataFrame) -> None:
        self.employee_list: list = []
        self.exclusion_list: list = []
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
