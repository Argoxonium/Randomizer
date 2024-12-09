from modules import *
import os

def main():
    #get file path and make sure files exist.
    employee_file_path = os.path.expanduser(config.get('File Paths','employee_list'))
    os.makedirs(employee_file_path,exist_ok=True)

    equipment_file_path = os.path.expanduser(config.get('File Paths','equipment_list'))
    os.makedirs(equipment_file_path,exist_ok=True)

    #Get the data from both of these files
    personnel, equipment = load_data(employee_file_path, equipment_file_path)

    #Run the random even determination
    assignment = run_random_event(equipment, personnel)

    #Export Data to an excel file to share.
    output_file_path = os.path.expanduser(config.get('File Paths','output_path'))
    export_to_excel(assignment,output_file_path)


if __name__ == '__main__':
    main()

