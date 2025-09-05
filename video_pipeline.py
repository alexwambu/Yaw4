from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os

def generate_movie(script_text: str, input_path: str = None, output_path: str = "output.mp4"):
    """
    Generate a simple HD movie from script + optional input video.
    """
    clips = []

    if input_path and os.path.exists(input_path):
        # Use uploaded clip
        base_clip = VideoFileClip(input_path).resize(height=720)  # HD resize
        clips.append(base_clip)
    else:
        # Empty background with text
        base_clip = TextClip("Movie Scene", fontsize=70, color='white', size=(1280,720)).set_duration(5)
        clips.append(base_clip)

    # Add script text overlay
    text = TextClip(script_text, fontsize=50, color='yellow', size=(1280,720))
    text = text.set_duration(clips[0].duration).set_pos("bottom")

    final = CompositeVideoClip([clips[0], text])
    final.write_videofile(output_path, codec="libx264", audio=False)

    return output_path
