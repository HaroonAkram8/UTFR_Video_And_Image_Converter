import cv2
import numpy as np
import glob

# Takes a video specified in the input path and converts each frame to an image in the output path. Returns the frame rate of the video.
def convert_video_to_frames(inputPath, outputPath):
    # Get video from the input path
    videoCapture = cv2.VideoCapture(inputPath)
    
    # Get the frames per second for the video
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    
    # Loop through each frame of the video and export it as a jpg image
    success,image = videoCapture.read()
    count = 0
    while success:
        cv2.imwrite(outputPath + str(count).zfill(6) + ".jpg", image)     
        success,image = videoCapture.read()
        print("\rRead frame " + str(count) + ".", end="")
        count += 1

    print("\nDONE.")
    return fps

# Takes the images specifies in the input path and converts it to a video in the output path. The video will have the input frame rate.
def convert_frames_to_video(inputPath, outputPath, fps):
    image_array = []
    count = 0;
    
    # Get the images from the input path and place them into an array
    for fileName in sorted(glob.glob(inputPath)):
        image = cv2.imread(fileName)
        image_array.append(image)
        print("\rReading frame " + str(count) + ".", end="")
        count += 1
    print()
    
    height, width, layers = image_array[0].shape
    size = (width, height)
    
    # Set the video's parameters
    outputVideo = cv2.VideoWriter(outputPath, fourcc=cv2.VideoWriter_fourcc(*"mp4v"), fps=fps, frameSize=size, isColor=True)
    
    # Take each image from the image_array and add it to the video
    count = 0;
    for image in image_array:
        outputVideo.write(image)
        print("\rAdded frame " + str(count) + " to video.", end="")
        count += 1
    
    outputVideo.release()
    print("\nDONE.")


inputPath = "Test_Videos\\input.mp4"
outputPath = "Test_Frames_Output\\frame"
fps = convert_video_to_frames(inputPath, outputPath)

# DO THE !python detect.py --weights runs/train/exp/weights/best.pt --conf 0.1 --source {dataset.location}/test/images AT THIS STEP AND CHANGE THE INPUT AND OUTPUT PATHS

inputPath = "Test_Frames_Output\\*.jpg"
outputPath = "Test_Videos_Output\\output.mp4"
convert_frames_to_video(inputPath, outputPath, fps)