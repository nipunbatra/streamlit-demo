# Import all distribution modules and combine them into a single dictionary
import os
import importlib
import sys

# Get the directory of this file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize the distributions dictionary
CONTINUOUS_DISTRIBUTIONS = {}

# Loop through all Python files in the directory
for filename in os.listdir(current_dir):
    if filename.endswith('.py') and filename != '__init__.py':
        # Get the module name without the .py extension
        module_name = filename[:-3]
        
        # Import the module
        module = importlib.import_module(f'config.continuous.{module_name}')
        
        # Get the distribution constant (assuming it's named in uppercase)
        distribution_constant = getattr(module, module_name.upper(), None)
        
        if distribution_constant:
            # Add the distribution to the dictionary with a formatted name
            # Convert snake_case to CamelCase for the display name
            display_name = ''.join(word.capitalize() for word in module_name.split('_'))
            CONTINUOUS_DISTRIBUTIONS[display_name] = distribution_constant