import os
import imageio.core.util
os.mkdir("output_folder")
# Define the path to the output folder to save rotated video files
output_folder = os.path.join(os.getcwd(), "output_folder")

# Loop through all files in the current directory
for filename in os.listdir():
    # Check if the file is a video file
    if filename.endswith(".MP4") or filename.endswith(".avi") or filename.endswith(".mov"):
        # Define the path to the input video file
        input_path = filename

        # Define the path to the output video file
        output_path = os.path.join(output_folder, "rotated_" + filename)

        # Open the input video file using imageio
        video_reader = imageio.get_reader(input_path)

        # Get the width and height of the video
        height, width = video_reader.get_meta_data()['source_size']

        # Create a new writer to save the rotated video
        video_writer = imageio.get_writer(output_path, fps=29.97)

        # Loop through each frame in the video
        for frame in video_reader:
            # Rotate the frame 90 degrees to the left
            rotated_frame = frame.transpose(1, 0, 2)[::-1, :, :]

            # Write the rotated frame to the output video file
            video_writer.append_data(rotated_frame)

        # Close the video reader and writer
        video_reader.close()
        video_writer.close()
