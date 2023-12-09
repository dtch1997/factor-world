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

from typing import List

import gymnasium as gym
from gymnasium import spaces

from factorworld.envs.factors.xml_wrapper import XmlWrapper


class TableTextureWrapper(XmlWrapper):
    """Wrapper over MuJoCo environments that modifies table texture."""

    def __init__(
        self,
        env: gym.Env,
        texture_names: List[str] = ["clay.png"],
        seed: int = None,
        **kwargs,
    ):
        """Creates a new wrapper.

        Args:
          env: Environment to wrap
          texture_names: Texture names to sample from
          seed: Random seed
        """
        self._default_texture = None
        self.texture_names = texture_names

        super().__init__(
            env,
            factor_space=spaces.Discrete(start=0, n=len(self.texture_names), seed=seed),
            init_factor_value=0,
            **kwargs,
        )

        breakpoint()

    @property
    def factor_name(self):
        return "table_texture"

    def _set_to_factor(self, value: int):
        """Sets to the given factor."""

        if self._default_texture is None:
            print(
                "WARNING(object_size): Default values not set. "
                "Not setting factor value."
            )
            return
