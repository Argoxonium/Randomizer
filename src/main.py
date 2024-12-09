from modules import *
import configparser
import pandas as pd

def main(): ...

def run_random_event(equipment: pd.DataFrame, personnel: pd.DataFrame)->pd.DataFrame:
    personnel_exclusion: list = [] #A exclusion list of personnel removed from inspeciton or have already been assigned.
    avalible_equipment: pd.DataFrame = equipment
    assignments: pd.DataFrame = create_export_df()
    random_event = RandomReviewers(equipment, personnel)
    
    #Itterate through ever item though the list of equipment
    for i in range(len(equipment.index)):
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
        possible_equipment:pd.DataFrame = random_event.remove_group_equipment(reviewer)

        #Assign equipment for max reviews
        for j in review_num:
            #increase the values of i to account for review number
            i += j        

            #Determine Equipment
            equipment:dict = random_event.choose_equipment(avalible_equipment, assignments)

            #create a dict in correct order and add the assigned equipment to dataframe
            assignment: dict = {
                'Location': equipment["Location"], 
                'Room': equipment["Room"], 
                'Equipment':equipment["Eqipment ID"], 
                'Owner':equipment["Owner"], 
                'Reviewer':reviewer
                }   
            assignments.append(assignment, ignore_index=True)

            # Append to the assignments DataFrame
            assignments = pd.concat([assignments, pd.DataFrame([assignment])], ignore_index=True)

    
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

if __name__ == '__main__':
    main()

