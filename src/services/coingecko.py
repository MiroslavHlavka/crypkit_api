from pycoingecko import CoinGeckoAPI

from src.services import try_except


class CoingeckoService:
    def __init__(self, cg=CoinGeckoAPI()) -> None:
        self.cg = cg

    # probably useless since in coingecko lib there is retry already
    # @try_except(Exception, "Coingecko service call failed")
    async def get_cryptocurrency(self, id: str) -> dict:
        return self.cg.get_coin_by_id(id)
