import pathlib


def get_project_dir() -> pathlib.Path:
    return pathlib.Path(__file__).parent.parent.absolute()


class Paths:
    MetaworldDir: pathlib.Path = (
        get_project_dir() / "third_party" / "metaworld" / "metaworld"
    )
    # MetaworldDir points to source directory of Metaworld
    FactorworldDir: pathlib.Path = get_project_dir() / "factorworld"
    # FactorworldDir points to source directory of Factorworld
