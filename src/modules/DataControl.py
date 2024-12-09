import pandas as pd
from randomizer import RandomReviewers

def load_data(employee_file, equipment_file) -> pd.DataFrame:
    # Load employee and equipment data
    employees = pd.read_csv(employee_file)
    equipment = pd.read_csv(equipment_file)
    return employees, equipment

def export_to_excel(assignments, output_file) -> None:
    # Export assignments to Excel
    assignments.to_excel(output_file, index=False)

def run_random_event(equipment: pd.DataFrame, personnel: pd.DataFrame, personnel_exclusion: list = [])->pd.DataFrame:
    assignments: pd.DataFrame = create_export_df() #Create an empty dataframe
    random_event = RandomReviewers(equipment, personnel) #Create an instance for random event
    number_of_equipment = len(equipment.index) #set loop number before loop is eddited
    
    #Itterate through ever item though the list of equipment
    for i in range(number_of_equipment):
        review_num:int = 0

        #find a reviewer that is able to review
        while review_num == 0:
            #determine a reviewer
            reviewer = random_event.choose_reviewer()
            #determine how many reviews a reviewer can do
            review_num = random_event.determine_review_number(reviewer)
            #remove reviewer from list once selected
            personnel_exclusion.append(reviewer)

        #Determine possible equipment to review by removing group equipment
        possible_equipment:pd.DataFrame = random_event.remove_group_equipment(reviewer, equipment)

        #Assign equipment for max reviews
        for j in review_num:
            #increase the values of i to account for review number
            i += j        

            #Determine Equipment
            equipment:dict = random_event.choose_equipment(possible_equipment, assignments)

            #create a dict in correct order and add the assigned equipment to dataframe
            assignment: dict = {
                'Location': equipment["Location"], 
                'Room': equipment["Room"], 
                'Equipment':equipment["Eqipment ID"], 
                'Owner':equipment["Owner"], 
                'Reviewer':reviewer
                }   
            assignments.append(assignment, ignore_index=True)
            equipment = remove_assigned_equipment(equipment, assignments)

            # Append to the assignments DataFrame
            assignments = pd.concat([assignments, pd.DataFrame([assignment])], ignore_index=True)
    
    return assignments

def remove_assigned_equipment(equipment: pd.DataFrame, assignments: pd.DataFrame) -> pd.DataFrame:
    """
    Removes equipment already assigned from the available equipment DataFrame.

    Args:
        equipment (pd.DataFrame): The DataFrame containing all available equipment.
        assignments (pd.DataFrame): The DataFrame containing assigned equipment.

    Returns:
        pd.DataFrame: A filtered DataFrame with unassigned equipment.
    """
    # Merge assignments to filter out rows
    filtered_equipment = equipment.merge(
        assignments[['Location', 'Room', 'Equipment', 'Owner']],
        on=['Location', 'Room', 'Equipment', 'Owner'],
        how='left',
        indicator=True
    )

    # Keep only rows not in the assignments DataFrame
    unassigned_equipment = filtered_equipment[filtered_equipment['_merge'] == 'left_only'].drop(columns=['_merge'])

    return unassigned_equipment

def create_export_df()->pd.DataFrame:
    """
    A function to create the empty dataframe to house the assigned personnel.
    """
    #Define the columns names
    columns = ['Location','Room','Equipment','Owner','Reviewer']
    #Create the empty Dataframe
    empty_df = pd.DataFrame(columns=columns)
    return empty_df