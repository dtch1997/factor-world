# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Tuple

import gymnasium as gym
from gymnasium import spaces
import numpy as np

from factorworld.envs.factors import constants
from factorworld.envs.factors.factor_wrapper import FactorWrapper


class ObjectSizeWrapper(FactorWrapper):
    """Wrapper over MuJoCo environments that modifies object size."""

    def __init__(
        self,
        env: gym.Env,
        scale_range: Tuple[float, float] = (0.4, 1.4),
        seed: int = None,
        **kwargs,
    ):
        """Creates a new wrapper."""
        # Note: Must set this to None before calling super()__init__().
        self._geom_id2size = None
        super().__init__(
            env,
            factor_space=spaces.Box(
                low=np.atleast_1d(scale_range[0]),
                high=np.atleast_1d(scale_range[1]),
                dtype=np.float32,
                seed=seed,
            ),
            **kwargs,
        )

        # Store default values
        try:
            body = self.model.body(constants.OBJECT_BODY_NAME)
        except KeyError as e:
            print(
                f"WARNING(object_size): {constants.OBJECT_BODY_NAME} not found. "
                "Body names: {self.model.body_names}"
            )

        self._geom_id2size = {
            geom_id: self.model.geom_size[geom_id].copy()
            for geom_id, body_id in enumerate(self.model.geom_bodyid)
            if body_id == body.id
        }

    @property
    def factor_name(self):
        return "object_size"

    def _set_to_factor(self, value: float):
        """Sets to the given factor."""
        if self._geom_id2size is None:
            print(
                "WARNING(object_size): Default values not set. "
                "Not setting factor value."
            )
            return

        for geom_id, geom_size in self._geom_id2size.items():
            self.unwrapped.model.geom(geom_id).size = geom_size * value
