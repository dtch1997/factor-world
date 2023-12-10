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

from typing import Any, Dict

from factorworld.envs.factors.factor_wrapper import FactorWrapper
from factorworld.envs.factors.light import LightWrapper
from factorworld.envs.factors.camera_pos import CameraPosWrapper
from factorworld.envs.factors.arm_pos import ArmPosWrapper
from factorworld.envs.factors.table_pos import TablePosWrapper
from factorworld.envs.factors.obj_pos import ObjectPosWrapper
from factorworld.envs.factors.obj_size import ObjectSizeWrapper
from factorworld.envs.factors.table_texture import TableTextureWrapper

from factorworld.envs.xml_utils import generate_xml
from factorworld.envs.xml_utils import get_texture_names
from factorworld.envs.asset_path_utils import (
    full_factorworld_assets_path_for,
    full_metaworld_assets_v2_path_for,
    get_fw_asset_dir_relative_to_mw_asset_dir,
)

ALL_FACTORS: Dict[str, FactorWrapper] = {
    "arm_pos": ArmPosWrapper,
    # "camera_pos": CameraPosWrapper,
    # 'distractor_pos': DistractorPosWrapper,
    # 'floor_texture': FloorTextureWrapper,
    "light": LightWrapper,
    "object_pos": ObjectPosWrapper,
    "object_size": ObjectSizeWrapper,
    # 'object_texture': ObjectTextureWrapper,
    "table_pos": TablePosWrapper,
    "table_texture": TableTextureWrapper,
}
