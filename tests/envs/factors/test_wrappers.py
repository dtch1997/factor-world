""" Make a Metaworld env with factors, and render """

import pytest
from metaworld import MT1
from factorworld.envs import make_env_with_factors, list_factors

domain = "pick-place-v2"
factors = [
    "object_pos",
]


@pytest.mark.parametrize("factor_name", list_factors())
def test_env(factor_name: str):
    benchmark = MT1(domain)
    env_cls = benchmark.train_classes[domain]
    env_kwargs = {}
    factor_kwargs = {factor_name: {}}
    env = make_env_with_factors(env_cls, env_kwargs, factor_kwargs)
    env.set_task(benchmark.train_tasks[0])
    env.reset()

    obs = env.reset()
    for _ in range(100):
        env.step(env.action_space.sample())
