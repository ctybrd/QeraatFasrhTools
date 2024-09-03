# Function to process files in a directory
function Process-Files {
    param (
        [string]$directory
    )
    # Change directory to the specified folder
    Set-Location $directory
    # Run the command to convert PNG files to PNG8 format
    magick mogrify -format png8 .\*.png
    # Go back to the parent directory
    Set-Location ..
}

# Function to traverse directories recursively
function Traverse-Directories {
    param (
        [string]$folder
    )
    # Process files in the current directory
    Process-Files $folder
    # Get a list of subdirectories
    $subdirectories = Get-ChildItem -Path $folder -Directory
    # Traverse each subdirectory
    foreach ($subdir in $subdirectories) {
        Traverse-Directories $subdir.FullName
    }
}

# Starting directory
$startingDirectory = "E:\Qeraat\NewSides\PNG"

# Start traversing directories
Traverse-Directories $startingDirectory
