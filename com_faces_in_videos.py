import moviepy.editor as mpy

clip = mpy.VideoFileClip('videos/video_of_people_walking.mp4')

# Calculate new dimensions ensuring divisibility by 16
new_width = (clip.w // 16) * 16
new_height = (clip.h // 16) * 16

resized_clip = clip.resize(width=new_width, height=new_height) 
resized_clip.write_videofile('videos/resized_video.mp4')
