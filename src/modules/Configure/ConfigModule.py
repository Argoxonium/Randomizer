import os
from .ConfigManager import ConfigManager, check_redirect

config_path = os.path.expanduser(rf"~{check_redirect()}")
config = ConfigManager(config_path) #when inporting inport config.
