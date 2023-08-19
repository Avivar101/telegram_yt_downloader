from moviepy.editor import *

# convert .webm format to .mp3
def convert_webm_to_mp3(input_file, output_file):
    try:
        # load the webm file
        audio_clip = AudioFileClip(input_file)
        print(audio_clip)


        # extract audio from clip
        audio_file = audio_clip

        # save the audio as .mp3 file
        audio_file.write_audiofile(output_file)

        # close the video and audio clips
        audio_clip.close()
        audio_file.close()
        print("conversion successful")
    except Exception as e:
        print(f"Error occurred during conversion of {e}")

if __name__ == "__main__":
    # Replace 'input.webm' with the path to your .webm file
    input_file_path = "Rockstar.webm"

    # Replace 'output.mp3' with the desired name for your .mp3 file
    output_file_path = "Rockstar.mp3"

    convert_webm_to_mp3(input_file_path, output_file_path)
