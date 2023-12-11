from typing import Tuple

import gymnasium as gym
from gymnasium import spaces
import numpy as np

from factorworld.envs.factors.factor_wrapper import FactorWrapper


class GoalPosWrapper(FactorWrapper):
    """Wrapper over MuJoCo environments that modifies object position."""

    def __init__(
        self,
        env: gym.Env,
        x_range: Tuple[float, float] = (-0.3, 0.3),
        y_range: Tuple[float, float] = (-0.1, 0.2),
        z_range: Tuple[float, float] = (-0.05, 0.3),
        seed: int = None,
        **kwargs,
    ):
        """Creates a new wrapper."""
        super().__init__(
            env,
            factor_space=spaces.Box(
                low=np.array([x_range[0], y_range[0], z_range[0]]),
                high=np.array([x_range[1], y_range[1], z_range[1]]),
                dtype=np.float32,
                seed=seed,
            ),
            **kwargs,
        )

        goal_site_name = self._get_goal_site_name()

        try:
            goal_site = self.model.site(goal_site_name)
        except KeyError as e:
            print(f"WARNING(object_pos): Site {goal_site} not found.")
            self.goal_pos = None

        # Store object qpos/qvel indices
        self._default_goal_pos = goal_site.pos.copy()
        self.goal_pos = self._default_goal_pos.copy()

    def reset(self, force_randomize_factor: bool = False, **kwargs):
        super().reset(force_randomize_factor=force_randomize_factor, **kwargs)

        # Reset object pos.
        self._set_goal_pos(self.goal_pos)

        return self.unwrapped._get_obs()

    @property
    def factor_name(self):
        return "goal_pos"

    def _set_to_factor(self, value: Tuple[float, float, float]):
        """Sets to the given factor."""
        if not hasattr(self, "_default_goal_pos"):
            print("WARNING(goal_pos): Missing _default_goal_pos. Not setting factor.")
            return

        self.goal_pos = self._default_goal_pos + value[:3]

    def _get_goal_site_name(self):
        # if hasattr(self, "goal_site_name"):
        #     goal_site_name = self.goal_site_name
        # else:
        goal_site_name = "goal"
        return goal_site_name

    def _set_goal_pos(self, pos: np.ndarray):
        if not hasattr(self, "goal_pos"):
            print("WARNING(goal_pos): Missing goal_pos. Not setting goal_pos.")
            return

        self.unwrapped.goal = self.goal_pos
        # goal_site_name = self._get_goal_site_name()

        # try:
        #     goal_site = self.model.site(goal_site_name)
        #     goal_site.pos = self.goal_pos
        # except KeyError as e:
        #     print(f"WARNING(goal_pos): Site {goal_site} not found.")

        # self.reset_model()
