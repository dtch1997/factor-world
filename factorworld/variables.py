import pathlib
import metaworld


class Paths:
    MetaworldDir: pathlib.Path = pathlib.Path(metaworld.__file__).parent.absolute()
    # MetaworldDir points to source directory of Metaworld
    FactorworldDir: pathlib.Path = pathlib.Path(__file__).parent.absolute()
    # FactorworldDir points to source directory of Factorworld
