""" Make a Metaworld env with factors, and render """

import pytest
from metaworld import MT1
from factorworld import list_factors, get_factor

domain = "pick-place-v2"
factors = list_factors()


@pytest.mark.parametrize("factor_name", list_factors())
def test_env(factor_name: str):
    factor = get_factor(factor_name)
    benchmark = MT1(domain)
    env_constructor = benchmark.train_classes[domain]
    base_env = env_constructor()
    base_env.set_task(benchmark.train_tasks[0])
    base_env.reset()

    env = factor(base_env)

    obs = env.reset()
    for _ in range(100):
        env.step(env.action_space.sample())
