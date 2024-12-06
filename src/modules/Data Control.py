import pandas as pd

def load_data(self, employee_file, equipment_file):
    # Load employee and equipment data
    employees = pd.read_csv(employee_file)
    equipment = pd.read_csv(equipment_file)
    return employees, equipment

def export_to_excel(self, assignments, output_file):
    # Export assignments to Excel
    assignments.to_excel(output_file, index=False)