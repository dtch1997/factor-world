import pathlib
from typing import Any, Dict, List

from factorworld.envs.factors import ALL_FACTORS
from factorworld.envs.xml_utils import generate_xml
from factorworld.envs.xml_utils import get_texture_names
from factorworld.envs.asset_path_utils import (
    full_factorworld_assets_path_for,
    full_metaworld_assets_v2_path_for,
    get_fw_asset_dir_relative_to_mw_asset_dir,
)


def list_factors() -> List[str]:
    """Lists all factor names"""
    return list(ALL_FACTORS.keys())


def has_env_cls_model_name_been_set(env_cls):
    # We need this because of undesirable side-effects of
    # set_env_cls_model_name
    model_name = env_cls().model_name
    return "factors" in model_name


def make_env_with_factors(
    env_cls,
    env_kwargs,
    factor_kwargs: Dict[str, Dict[str, Any]] = None,
    use_train_xml: bool = True,
):
    """Creates  that generates a new XML file from factor value being set.

    Args:
        env_cls: metaworld.envs.mujoco.sawyer_xyz.sawyer_xyz_env.SawyerXYZEnv
        env_kwargs: Arguments for env_cls.
        factor_kwargs: Dictionary of {factor_name, factor_kwargs}
            - E.g. {'object_pos', {}}
        use_train_xml: Whether to load train or eval XML (e.g., textures).
    """
    factors_relative_path = (
        "factors/factors_train.xml" if use_train_xml else "factors/factors_eval.xml"
    )

    # Points from .../metaworld/envs/assets_v2/sawyer_xyz
    # To .../factorworld/envs/assets
    base_xml_path = env_cls.MODEL_NAME
    incl_path = (
        pathlib.Path("..")
        / get_fw_asset_dir_relative_to_mw_asset_dir()
        / factors_relative_path
    )
    xml_path = generate_xml(base_xml_path, include_paths=[str(incl_path)])
    env_kwargs.update(model_name=xml_path)

    # Construct base environment
    env = env_cls(**env_kwargs)

    # Wrap env with all factors
    texture_names = get_texture_names(
        full_factorworld_assets_path_for(factors_relative_path)
    )

    texture_wrapper_seeds = []
    for factor_name, env_kwargs in factor_kwargs.items():
        factor_cls = ALL_FACTORS[factor_name]
        if factor_name in ["floor_texture", "object_texture", "table_texture"]:
            # By default, use all available textures.
            if "texture_names" not in env_kwargs:
                env_kwargs.update(texture_names=texture_names)

            # Make sure seed is different across all texture wrappers.
            if "seed" in env_kwargs:
                seed = env_kwargs["seed"]
                while seed in texture_wrapper_seeds:
                    seed += 1
                env_kwargs.update(seed=seed)
                texture_wrapper_seeds.append(seed)

        env = factor_cls(env, **env_kwargs)

    return env
