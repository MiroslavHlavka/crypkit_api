from typing import Union

from pycoingecko import CoinGeckoAPI


class CoingeckoService:
    def __init__(self, cg=CoinGeckoAPI()) -> None:
        self.cg = cg

    # No need for re-try since CoinGeckoAPI has build in re-try mechanism
    async def get_cryptocurrency(self, id: str) -> Union[dict, None]:
        try:
            return self.cg.get_coin_by_id(id)
        except ValueError:
            # Return None when coingecko doesn't know you cryptocurrency
            return None
