import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    NEWS_API_KEY = '3b47014ee72a44118cdc3520fe0d0d84'
    SECRET_KEY = 'PIEDPIPER4186'
    
    @staticmethod
    def init_app(app):
            pass

class ProdConfig(Config):
    '''articles_result = Articles(
                id, author, title, description, url, image, date)
        articles_object.append(articles_result)

    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}  