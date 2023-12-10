import pyrallis
import pathlib
import moviepy.editor as mp
from dataclasses import dataclass


@dataclass
class Config:
    video_dir: str


def create_gif_from_videos(filepaths, output_path):
    # Initialize a list to store video clips
    video_clips = []

    # Load each video and append it to the list
    for filepath in filepaths:
        video_clip = mp.VideoFileClip(filepath)
        video_clips.append(video_clip)

    # Concatenate the video clips into a single video
    final_video = mp.concatenate_videoclips(video_clips)

    # Convert the concatenated video to a GIF
    final_video.write_gif(output_path, fps=20.0)


if __name__ == "__main__":
    config = pyrallis.parse(Config)
    video_dir = pathlib.Path(config.video_dir)

    mp4_fps = [str(fp) for fp in video_dir.iterdir() if fp.suffix == ".mp4"]
    mp4_fps = sorted(mp4_fps)

    create_gif_from_videos(mp4_fps, video_dir / "output.gif")
