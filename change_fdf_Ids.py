import re

# Function to modify the ID while preserving the pattern
def modify_id(id_str):
    # Split the ID into segments
    segments = id_str.split('-')
    if len(segments) == 4:
        # Modify the last character of each segment
        segments[0] = segments[0][:-1] + (chr((ord(segments[0][-1]) + 1 - 48) % 10 + 48))
        segments[1] = segments[1][:-1] + (chr((ord(segments[1][-1]) + 1 - 48) % 10 + 48))
        segments[2] = segments[2][:-1] + (chr((ord(segments[2][-1]) + 1 - 48) % 10 + 48))
        segments[3] = segments[3][:-1] + (chr((ord(segments[3][-1]) + 1 - 48) % 10 + 48))
        # Reconstruct the modified ID
        modified_id = '-'.join(segments)
        return modified_id
    else:
        raise ValueError("ID does not match the expected pattern")

# Regular expression to match /NM (ID) or /Nm (ID)
pattern = re.compile(r'(/NM|/Nm) \(([^)]+)\)')

# Read the original FDF file
with open('f:/Qeraat/Yaaqoub-Shamarly-Shalaby.fdf', 'r') as file:
    content = file.read()

# Function to replace each matched ID with the modified ID
def replace_id(match):
    key = match.group(1)  # /NM or /Nm
    original_id = match.group(2)  # The original ID within parentheses
    new_id = modify_id(original_id)  # Modify the ID
    return f'{key} ({new_id})'

# Replace IDs using the pattern and replace_id function
modified_content = pattern.sub(replace_id, content)

# Write the modified content to a new FDF file
with open('f:/Qeraat/Yaaqoub-Shamarly-Shalaby_Mod.fdf', 'w') as file:
    file.write(modified_content)

print("IDs have been modified and saved to 'Yaaqoub-Shamarly-Shalaby_Mod.fdf'")
