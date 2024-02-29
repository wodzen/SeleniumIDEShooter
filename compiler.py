'''
This file parses Selenium IDE pytest export files for action methods and appends them to a file for successive dynamic testing
'''

import os

# overwrite shooter file with template
def use_template(template_path, shooter_path):

    try:
        with open(template_path, 'r') as template_file, open(shooter_path, 'w') as shooter_file:
            
            for line in template_file:
                shooter_file.write(line)

    except Exception as e:
        print(e)
    
# parse and append action methods from selenium export scripts to shooter file
def parse_and_append_action(export_path, shooter_path, method_string, method_number):
    
    try:
        with open(export_path, 'r') as input_file, open(shooter_path, 'a') as shooter_file:
            
            appending = False

            for line in input_file:
                
                # once method is found, start appending
                if method_string in line:
                    appending = True

                    # create unique function name
                    shooter_file.write("\n")
                    shooter_file.write(f'  def execute_method_{str(method_number)}(self, target):\n')

                    continue

                if appending:
                    shooter_file.write(line)
        

    except Exception as e:
        print(e)


method_string = "self.driver.get"
export_directory_path = "./export_scripts/"
shooter_path = "shooter.py"
template_path = "template.py"

# overwrite shooter with template
use_template(template_path, shooter_path)

# append action methods from selenium exports
i=0
for file in os.listdir(export_directory_path):
    export_path = os.path.join(export_directory_path, file)
    if os.path.isfile(export_path):
        parse_and_append_action(export_path, shooter_path, method_string, i)
        i+=1
