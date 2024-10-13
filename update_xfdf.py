import re

# Path to your XFDF file
xfdf_file = 'E:/Qeraat/New_Qaloon-Shamarly-Shalaby.xfdf'

# Function to update the rect values
def update_rect_values(rect):
    values = rect.split(',')
    # Convert to float and add 1300 to the Y values (2nd and 4th values)
    values[1] = str(float(values[1]) + 1333)
    values[3] = str(float(values[3]) + 1333)
    return ','.join(values)

# Read the XFDF file
with open(xfdf_file, 'r', encoding='utf-8') as file:
    content = file.read()

# Find all rect attributes and update the Y values
updated_content = re.sub(r'rect="([^"]+)"', lambda m: f'rect=\"{update_rect_values(m.group(1))}\"', content)

# Write the updated content back to the XFDF file or save it as a new file
with open(  'E:/Qeraat/New_Qaloon-Shamarly-Shalaby1.xfdf', 'w', encoding='utf-8') as file:
    file.write(updated_content)

print("XFDF file updated successfully!")
