""" Make a Metaworld env with factors, and render """

import pyrallis
from dataclasses import dataclass
import pathlib
import moviepy.editor as mp
from factorworld.envs import make_env_with_factors, list_factors
from factorworld.envs.tasks.sawyer_pick_place_v2 import SawyerPickPlaceEnvV2
from metaworld.policies.sawyer_pick_place_v2_policy import SawyerPickPlaceV2Policy
from gymnasium.wrappers import record_video, time_limit


@dataclass
class Config:
    domain: str = "pick-place-v2"  # unused for now...
    factor: str = "light"
    render_mode: str = "rgb_array"


def get_sweep(config: Config):
    for factor in list_factors():
        config.factor = factor
        yield config


def record_expert_video(config):
    env_cls = SawyerPickPlaceEnvV2
    env_kwargs = {"render_mode": config.render_mode}
    factor_kwargs = {config.factor: {}}
    env = make_env_with_factors(env_cls, env_kwargs, factor_kwargs)
    env = time_limit.TimeLimit(env, 100)

    # Set up video recording
    if config.render_mode == "rgb_array":
        env = record_video.RecordVideo(
            env, f"videos/{config.factor}", episode_trigger=lambda x: True
        )

    policy = SawyerPickPlaceV2Policy()

    for e in range(5):
        obs = env.reset()
        done = False
        print("Current factor: ", env.current_factor_value)

        while not done:
            action = policy.get_action(obs)
            obs, _, term, trunc, _ = env.step(action)
            env.render()
            done = term or trunc

    env.close()


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
    for sweep in get_sweep(config):
        record_expert_video(sweep)
        video_dir = pathlib.Path("videos") / sweep.factor
        mp4_fps = [str(fp) for fp in video_dir.iterdir() if fp.suffix == ".mp4"]
        mp4_fps = sorted(mp4_fps)
        create_gif_from_videos(mp4_fps, video_dir / f"{sweep.factor}.gif")
