from src.services import try_except


class CoingeckoService:

    @staticmethod
    @try_except(Exception, "Coingecko service call failed")
    async def get_cryptocurrency(id: str):
        # TODO: do actual api call
        return id