import os
import platform

# Get the root path of the system
root_path = os.path.abspath("/")

def check_mobile_or_pc():
    # Get the system's platform
    system_platform = platform.system()
    print(os)
    print(system_platform)

    # Define a list of keywords commonly found in mobile device platforms
    mobile_keywords = ["Android", "iOS"]

    # Check if the system platform contains any of the mobile keywords
    is_mobile = any(keyword in system_platform for keyword in mobile_keywords)

    if is_mobile:
        print("mobile path: ", root_path)
        # Create a 'video' folder in the root path
        video_folder_path = os.path.join(root_path, "video")
        print(video_folder_path)
        # Check if the folder already exists, and if not, create it
        # if not os.path.exists(video_folder_path):
        #     os.mkdir(video_folder_path)
        #     print("Video folder created successfully.")
        # else:
        #     print("Video folder already exists.")
        print("The operating system is running on a mobile device.")
    else:
        
        print("PC Path: ", root_path)
        # Create a 'video' folder in the root path
        video_folder_path = os.path.join(root_path, r"Users\user\Videos")
        print(video_folder_path)
        # Check if the folder already exists, and if not, create it
        if not os.path.exists(video_folder_path):
            os.mkdir(video_folder_path)
            print("Video folder created successfully.")
        else:
            print("Video folder already exists.")
        print("The operating system is running on a PC.")
