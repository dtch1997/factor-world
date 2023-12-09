from typing import Dict, List
from factorworld.envs.factors import ALL_FACTORS, FactorWrapper


def list_factors() -> List[str]:
    """Lists all factor names"""
    return list(ALL_FACTORS.keys())


def get_factor(name: str) -> FactorWrapper:
    return ALL_FACTORS[name]
