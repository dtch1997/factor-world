""" Make a Metaworld env with factors, and render """

import pytest

from factorworld.envs.tasks.sawyer_pick_place_v2 import SawyerPickPlaceEnvV2
from factorworld.envs import make_env_with_factors, list_factors

domain = "pick-place-v2"
factors = [
    "object_pos",
    "object_size",
    "table_pos",
    "arm_pos",
    "light",
    "table_texture",
    "object_texture",
    "floor_texture",
    "camera_pos",
]


@pytest.mark.parametrize("factor_name", list_factors())
def test_env(factor_name: str):
    env_cls = SawyerPickPlaceEnvV2
    env_kwargs = {}
    factor_kwargs = {factor_name: {}}
    env = make_env_with_factors(env_cls, env_kwargs, factor_kwargs)
    env.reset()

    obs = env.reset()
    for _ in range(100):
        env.step(env.action_space.sample())
