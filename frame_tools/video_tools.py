# cols = 1280  # 1920 1280
# rows = 480
# num = 2
# FPS = 8
from pathlib import Path
import os
import cv2 as cv 



def create_video_png(subj_folder_input,subj_folder_out,name,frame_rate):
    print("start of  video creation ")


    subjects =sorted(Path(subj_folder_input).iterdir(), key=os.path.getmtime)
    for fichier in subjects[:]: 
        last_part = fichier.parts[-1]
        if not(last_part.endswith(".png")):
            subjects.remove(fichier)
    setup_frame = cv.imread(str(subjects[0]))
    video = cv.VideoWriter((subj_folder_out+name+".mp4"),
                            cv.VideoWriter_fourcc(*'mp4v'),
                            frame_rate, (setup_frame.shape[1],setup_frame.shape[0]))
    for path_frame in subjects :
          current_frame = cv.imread(str(path_frame))
          video.write(current_frame)
    video.release()
    
    print("end of video creation")


def create_video_jpeg(subj_folder_input,subj_folder_out,name,frame_rate):
    print("start of  video creation ")


    subjects =sorted(Path(subj_folder_input).iterdir(), key=os.path.getmtime)
    for fichier in subjects[:]: 
        last_part = fichier.parts[-1]
        if not(last_part.endswith(".jpeg")):
            subjects.remove(fichier)
    
    setup_frame = cv.imread(str(subjects[0]))
    video = cv.VideoWriter((subj_folder_out+name+".mp4"),
                            cv.VideoWriter_fourcc(*'mp4v'),
                            frame_rate, (setup_frame.shape[1],setup_frame.shape[0]))
    for path_frame in subjects :
          current_frame = cv.imread(str(path_frame))
          video.write(current_frame)

    
    print("end of video creation")


# subj_folder_input = "C:/Users/rdurs/Desktop/Stage/ROBOT/video/sc0_2023-07-04_20h09/"
# create_video_png(subj_folder_input,"C:/Users/rdurs/Desktop/Stage/ROBOT/video/","test_exp",20)