# Definitions File

import os
import sys

# OS
PLATFORM = sys.platform

# Directories
ROOT = os.path.dirname(os.path.abspath(__file__))
TEMP = os.path.join(ROOT, "temp")
LOGS = os.path.join(ROOT, "logs")

# Log Files
SYSTEM_LOG = os.path.join(LOGS, "system.log")

# Config Files
CONFIG_DIR = os.path.join(ROOT, "config")
CONFIG_JSON = os.path.join(CONFIG_DIR, "config.json")
CONFIG_TEMPLATE_JSON = os.path.join(CONFIG_DIR, "config_template.json")


# RaspberryPi GPIO Pin Defs
PAN_SERVO = 33
TILT_SERVO = 35
