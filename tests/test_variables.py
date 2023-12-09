from factorworld.variables import Paths


def test_metaworld_dir():
    path = Paths.MetaworldDir
    assert path.name == "metaworld"


def test_factorworld_dir():
    path = Paths.FactorworldDir
    assert path.name == "factorworld"
