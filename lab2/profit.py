from typing import TypedDict, Optional


class ProfitScenario(TypedDict):
    """Profit scenario model."""

    cost_price: float
    sell_price: float
    inventory: int


def profit(profit_dict: ProfitScenario) -> Optional[int]:
    """Calculate profit with given profit scenario."""
    sell_price, cost_price, inventory = profit_dict["sell_price"], profit_dict["cost_price"], profit_dict["inventory"]
    if sell_price < 0 or cost_price < 0 or inventory < 0:
        return None
    res = (sell_price - cost_price) * inventory
    return round(res)