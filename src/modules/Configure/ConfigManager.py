import os
import configparser

class Singleton(type):
    """
    This class is a metaclass addition to any class to force the creation of one instance of a class within a program. This is key
    for the ConfigManager since it config gets imported 
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class ConfigManager(metaclass=Singleton):
    """
    Manages the config, allowing you to pull information and get info when needed. In addition save information when needed to the
    config file.
    """
    def __init__(self, config_path = None):
        self.config = configparser.ConfigParser() #need to call and not inharent because metalass and subclass are already in Configparser.
        self.config_path = config_path
        self.config.read(config_path)

    def get(self, section: str, option: str):
        try:
            return self.config.get(section, option)
        except configparser.NoOptionError:
            return None

    def get_all(self):
        return {section: dict(self.config.items(section)) for section in self.config.sections()}

def check_redirect() -> str:
    """
    This is a check redirect function. Either config.ini or _redirect.ini is located in the same folder as
    ConfigManager.py. I am wanting to keep all the files for this program that holds data outside of the
    git commit folder. There for in future events, if I wanted to use this code i can keep the config.ini
    here or move it to another location.

    :return: returns the location of the file that is either in the 
    :rtype: str
    """
    # Get the current directory where this script is located
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    # Define the filenames to look for
    config_file = os.path.join(current_folder, "config.ini")
    redirect_file = os.path.join(current_folder, "_redirect.ini")
    
    # Check if config.ini exists in the current directory
    if os.path.isfile(config_file):
        return config_file
    
    # If config.ini is not found, check for _redirect.ini
    elif os.path.isfile(redirect_file):
        
        # Load the redirect file
        parser = configparser.ConfigParser()
        parser.read(redirect_file)
        
        # Get the redirected path from the redirect file
        if parser.has_section("Redirect") and parser.has_option("Redirect", "config_location"):
            redirect_path = parser.get("Redirect", "config_location")
            # Expand user if the path has ~ and return the absolute path
            redirect_path = os.path.expanduser(redirect_path)
            return redirect_path
        else:
            return None
    
    else:
        return None

