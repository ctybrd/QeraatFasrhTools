qaree_files = {
    "W": 'e:/Qeraat/Warsh-Asbahani-Shamarly-Shalaby.pdf',
    "I": 'e:/Qeraat/IbnAmer-Shamarly-Shalaby.pdf',
    "T": 'e:/Qeraat/madina10th.pdf',
    "J": 'e:/Qeraat/AbuJaafar-Shamarly-Shalaby.pdf',
    "K": 'e:/Qeraat/Qaloon-Shamarly-Shalaby.pdf',
    "U": 'e:/Qeraat/AshabSela-Shamrly-Shalaby.pdf',
    "M": 'e:/Qeraat/Hamzah-Shamarly-Shalaby.pdf',
    "B": 'e:/Qeraat/IbnKatheer-Shmarly-Shalaby.pdf',
    "S": 'e:/Qeraat/Sho3ba-Shamarly-Shalaby.pdf',
    "A": 'e:/Qeraat/Warsh-Azraq-Shamarly-Shalaby_V1_1.pdf',
    "E": 'e:/Qeraat/Kisai-Shamarly-Shalaby.pdf',
    "F": 'e:/Qeraat/Khalaf-Shamarly-Shalaby.pdf',
    "X": 'e:/Qeraat/Kisai-Khalaf-Shamarly-Shalaby.pdf',
    "Y": 'e:/Qeraat/Yaaqoub-Shamarly-Shalaby.pdf',
    "C": 'e:/Qeraat/AbuAmro-Shamarly-Shalaby.pdf',
    "D": 'e:/Qeraat/Dori-AbuAmro-Shamarly-Shalaby.pdf',
    "G": 'e:/Qeraat/Sosi-AbuAmro-Shamarly-Shalaby.pdf',
    "L": 'e:/Qeraat/Tawasot-Shamarly-Shalaby.pdf',
    "O": 'e:/Qeraat/Asem_IbnAmer-Shamarly-Shalaby.pdf',
    "P": 'e:/Qeraat/AbuAmro-Yaqoub-Shamarly-Shalaby.pdf',
}

# Sort the dictionary items based on filenames
sorted_qaree_files = dict(sorted(qaree_files.items(), key=lambda item: item[1]))

# Print or return the sorted dictionary

# Example usage
sorted_qaree_files = dict(sorted(qaree_files.items(), key=lambda item: item[1]))
for key, value in sorted_qaree_files.items():
    print(f"{key}: {value}")
