import shutil
import zipfile

file_path = 'E:/Qeraat/farsh_v5.db'
destination_folders = [
    'E:/Qeraat/Wursha_QuranHolder/other/data/',
    'E:/Qeraat/Wursha_QuranHolder/platforms/android/app/build/intermediates/assets/debug/mergeDebugAssets/www/',
    'E:/Qeraat/Wursha_QuranHolder/platforms/android/app/src/main/assets/www/',
    'E:/Qeraat/Wursha_QuranHolder/www/',
    'E:/Qeraat/'
]


for folder in destination_folders:
    destination_file = folder + 'farsh_v4.db'
    shutil.copy(file_path, destination_file)

# #add to archive
# zip_file_path = "E:/Qeraat/Wursha_QuranHolder/other/data/farsh_v4.db.zip"
# with zipfile.ZipFile(zip_file_path, 'r+') as zip_file:
#     zip_file.write(file_path, arcname='farsh_v4.db')

print("File copied to the specified folders.")