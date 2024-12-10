import os

def check_permissions(file_path):
    """_summary_
    Input a path to a file to see if the program is able to determine 
    if python is able to access the file.
    
    _Example_
    >>> file_path = "C:/Users/nhorn/Documents/Lab Inspections/Glovebox and hood inspection documents/Program/config.ini"
    >>> check_permissions(file_path)
    """
    print(f"Checking permissions for: {file_path}")
    
    if not os.path.isfile(file_path):
        print("❌ File does not exist.")
        return

    # Check read, write, and execute permissions
    can_read = os.access(file_path, os.R_OK)
    can_write = os.access(file_path, os.W_OK)
    can_execute = os.access(file_path, os.X_OK)

    print(f"✅ Readable: {'Yes' if can_read else 'No'}")
    print(f"✅ Writable: {'Yes' if can_write else 'No'}")
    print(f"✅ Executable: {'Yes' if can_execute else 'No'}")


