from llconfig import Config
from llconfig.converters import bool_like


def init_config() -> Config:
    c = Config(env_prefix="CK_")

    c.init("SERVICE_NAME", str, "crypkit-service")
    c.init("ENV", str, "production")
    c.init("DEBUG", bool_like, False)

    c.init("HOST", str, "0.0.0.0")
    c.init("PORT", int, 8080)

    # DB
    c.init("DB_HOST", str)
    c.init("DB_PASSWORD", str)
    c.init("DB_DB", str)
    c.init("DB_USER", str)

    c.load()

    return c


base_config = init_config()
