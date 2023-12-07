""" Make a Metaworld env with factors, and render """

import pyrallis
from dataclasses import dataclass
from metaworld import MT1
from factorworld.envs.factors import ALL_FACTORS

@dataclass
class Config:
    domain: str = 'pick-place-v2'
    factor: str = 'light'
    render_mode: str = 'human'

if __name__ == "__main__":

    config = pyrallis.parse(Config)

    benchmark = MT1(config.domain)
    env_constructor = benchmark.train_classes[config.domain]
    base_env = env_constructor(render_mode = config.render_mode)
    base_env.set_task(benchmark.train_tasks[0])
    base_env.reset()

    env = ALL_FACTORS[config.factor](base_env)

    for e in range(10):
        obs = env.reset()
        print("Current factor: ", env.current_factor_value)

        for _ in range(100):
            env.step(env.action_space.sample())
            env.render()