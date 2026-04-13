from enum import Enum


class SupplierTypes(str, Enum):
    FREE_MARKET = 'free_market'
    DISTRIBUTED_GENERATION = 'distributed_generation'
    BOTH = 'both'
