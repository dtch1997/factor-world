# Factor-World

Extends Metaworld environments with 10 visual factors of variation. 
Uses modern `mujoco` bindings and the `gymnasium` interface. 

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm-project.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![test](https://github.com/dtch1997/factor-world/actions/workflows/ci.yml/badge.svg)](https://github.com/dtch1997/factor-world/actions/workflows/ci.yml)

## Citation

Factor-World was proposed in [Decomposing the Generalization Gap in Imitation Learning for Visual Robotic Manipulation](https://sites.google.com/view/generalization-gap)

If you use this repository, consider citing the paper:
```bash
@misc{xie2023decomposing,
      title={Decomposing the Generalization Gap in Imitation Learning for Visual Robotic Manipulation}, 
      author={Annie Xie and Lisa Lee and Ted Xiao and Chelsea Finn},
      year={2023},
      eprint={2307.03659},
      archivePrefix={arXiv},
      primaryClass={cs.RO}
}
```

Please also consider citing this repository:
```bash
@software{tan2023factorworld,
    author = {Tan, Daniel CH},
    month = {12},
    title = {{Factor-World}},
    url = {https://github.com/dtch1997/factor-world},
    version = {0.0.1},
    year = {2023}
}
```

## Acknowledgements

This repository builds upon the following codebases:
- Official Factor-World implementation: https://github.com/RLAgent/factor-world
- Farama Foundation's Metaworld repository: https://github.com/Farama-Foundation/Metaworld
