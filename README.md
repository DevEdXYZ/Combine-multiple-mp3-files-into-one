MP3 Merger with Smooth Transitions
This is a simple Python script that combines multiple MP3 files from the directory it is executed in into a single output MP3 file. The script applies a smooth 5-second fade-out and fade-in transition between tracks. It is designed for Windows and has been tested with Python 3.13.

Requirements
Python 3.13 (or later)
FFmpeg (must be installed and accessible from the command line)
Installation
Step 1: Install Python
Make sure you have Python 3.13 installed. You can download it from the official site:

Python Downloads

Step 2: Install FFmpeg
The script requires FFmpeg to process MP3 files. You can install it using Chocolatey (recommended for Windows):

Open Command Prompt (CMD) as Administrator.

Run the following command:

sh
Copy
Edit
choco install ffmpeg
Verify the installation:

sh
Copy
Edit
ffmpeg -version
If installed correctly, you should see version details.

Step 3: Clone or Download This Repository
Clone the repository using Git:

sh
Copy
Edit
git clone https://github.com/yourusername/mp3-merger.git
cd mp3-merger
Or download the script directly from GitHub.

Usage
Place all your MP3 files in the same directory as the script.

Open Command Prompt (CMD) as Administrator.

Navigate to the directory containing the script:

sh
Copy
Edit
cd path\to\script\directory
Run the script:

sh
Copy
Edit
python merge_mp3.py
The script will:

Detect all MP3 files in the current directory.
Merge them with a 5-second fade transition.
Save the final output as output/output.mp3.
Features
✅ Automatically finds all MP3 files in the directory
✅ Applies a smooth 5-second crossfade between tracks
✅ Handles a single MP3 file by copying it to the output folder
✅ Outputs a merged MP3 file in the output/ directory
✅ Tested on Windows with Python 3.13

Notes
If FFmpeg is not installed or not in the system PATH, the script will fail.
The script works best with MP3 files that have a similar bitrate and encoding settings.
License
This project is open-source. Feel free to modify and improve it.
