class BaseConfig:
    """ Base Configuration """

    TESTING = False


class DevelopmentConfig(BaseConfig):
    """ Development Configuration """

    pass


class TestingConfig(BaseConfig):
    """ Development Configuration """

    TESTING = True


class ProductionConfig(BaseConfig):
    """ Development Configuration """

    pass
