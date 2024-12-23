import os
import sys
import django

# Add this line to import your command
from .commands.create_test_user import Command as create_test_user_command
