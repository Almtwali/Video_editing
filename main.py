from moviepy.editor import VideoFileClip , CompositeVideoClip , ImageClip
class Video_Editing():
    def __init__ (self,Video_path):
        self.Video_clip = VideoFileClip(Video_path)
        self.Final_Video = self.Video_clip

    def Integration_process(self,Image_path,Start_time,X_position,Y_position,Duration):
        Image_clip = ImageClip(Image_path,duration=Duration).set_start(Start_time).set_position((X_position, Y_position))
        Transition_Duration =1
        Image_clip = Image_clip.fadein(Transition_Duration).fadeout(Transition_Duration)
        self.Final_Video =CompositeVideoClip([self.Final_Video,Image_clip.set_position('center')])
    def Final_Video_Clip (self, output_path="input_video.mp4"):
        self.Final_Video.write_videofile(output_path, codec='libx264', audio_codec='aac')
if __name__ =="__main__":
    video_editor = Video_Editing(Video_path="input_video.mp4")
    video_editor.Integration_process(Image_path="input_Image.jpg",Start_time=3,X_position=100,Y_position=74,Duration=2)
    video_editor.Final_Video_Clip()