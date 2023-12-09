from factorworld.envs.asset_path_utils import (
    METAWORLD_ASSET_DIR_V2,
    FACTORWORLD_ASSETS_DIR,
    get_fw_asset_dir_relative_to_mw_asset_dir,
)


def test_asset_path_utils():
    mw_to_fw = get_fw_asset_dir_relative_to_mw_asset_dir()
    fw_pred = METAWORLD_ASSET_DIR_V2 / mw_to_fw
    assert fw_pred.resolve() == FACTORWORLD_ASSETS_DIR
