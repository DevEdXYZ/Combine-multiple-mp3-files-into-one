import os
import glob
import subprocess

def main():
    # Create the output directory if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Find all MP3 files in the current directory
    mp3_files = glob.glob("*.mp3")
    if not mp3_files:
        print("No MP3 files found in the current directory.")
        return

    # Sort the files (optional, for consistent ordering)
    mp3_files.sort()

    # If there is only one MP3 file, simply copy it to the output folder.
    if len(mp3_files) == 1:
        input_file = mp3_files[0]
        output_file = os.path.join(output_dir, "output.mp3")
        command = ["ffmpeg", "-y", "-i", input_file, "-c", "copy", output_file]
        print("Only one MP3 file found. Copying it to the output folder.")
        subprocess.run(command)
        return

    # Build the FFmpeg command with multiple inputs
    # Start with the basic command and add all input files
    command = ["ffmpeg", "-y"]
    for file in mp3_files:
        command.extend(["-i", file])

    # Construct the filter_complex chain to apply a 5-second acrossfade between files
    # For example, with three files the chain is:
    # [0:a][1:a]acrossfade=d=5[a1]; [a1][2:a]acrossfade=d=5[out]
    filter_chain = ""
    last_label = "[0:a]"
    for i in range(1, len(mp3_files)):
        # Use a temporary label if not processing the last file, else use [out]
        new_label = f"[a{i}]" if i < len(mp3_files) - 1 else "[out]"
        filter_chain += f"{last_label}[{i}:a]acrossfade=d=5{new_label};"
        last_label = new_label
    # Remove the trailing semicolon
    if filter_chain.endswith(";"):
        filter_chain = filter_chain[:-1]

    # Add the filter_complex and map the final output label to the output file
    command.extend(["-filter_complex", filter_chain, "-map", "[out]"])
    output_file = os.path.join(output_dir, "output.mp3")
    command.append(output_file)

    # Display the FFmpeg command (for debugging)
    print("Running FFmpeg command:")
    print(" ".join(command))
    
    # Run the command
    subprocess.run(command)

if __name__ == "__main__":
    main()
