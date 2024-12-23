from django.core.management import setup_environ
import os
import sys
import django

# Add this line to import your command
from .create_test_user import Command as create_test_user_command
