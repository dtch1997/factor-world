""" Make a Metaworld env with factors, and render """

import pyrallis
from dataclasses import dataclass
from factorworld.envs import make_env_with_factors
from factorworld.envs.tasks.sawyer_pick_place_v2 import SawyerPickPlaceEnvV2


@dataclass
class Config:
    domain: str = "pick-place-v2"
    factor: str = "light"
    render_mode: str = "human"


if __name__ == "__main__":
    config = pyrallis.parse(Config)

    env_cls = SawyerPickPlaceEnvV2
    env_kwargs = {"render_mode": "human"}
    factor_kwargs = {config.factor: {}}
    env = make_env_with_factors(env_cls, env_kwargs, factor_kwargs)
    env.reset()

    for e in range(10):
        obs = env.reset()
        print("Current factor: ", env.current_factor_value)

        for _ in range(100):
            env.step(env.action_space.sample())
            env.render()
