import subprocess

def run_script(script_name):
    print(f"Starting {script_name}...")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    print(f"Completed {script_name}")
    # print(f"Return code: {result.return_code}")
    # if result.return_code != 0:
    #     print(f"Error running {script_name}: {result.stderr}")
    # else:
    #     print(f"Output of {script_name}: {result.stdout}")

#export pdf to slices png files
run_script('F:/Qeraat/QeraatFasrhTools/Export_pdf_png_ALL.py')

# remove white make transparent slices
run_script('F:/Qeraat/QeraatFasrhTools/removewhite_ALL.py')

# concat each 5 slices in one image 
run_script('F:/Qeraat/QeraatFasrhTools/ConcatImages_ALL.py')

#Mogrify ALL
run_script('F:/Qeraat/QeraatFasrhTools/mogrify_ALL.py')
