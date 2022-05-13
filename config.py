
class Config:

    TESTING = True
    SECRET_KEY             = ''
    MAIL_SERVER            = 'smtp.office365.com'
    MAIL_PORT              = '587'
    MAIL_USE_TLS           = True
    MAIL_USE_SSL           = False
    # MAIL_DEBUG             = True
    MAIL_USERNAME          = ''
    MAIL_PASSWORD          = ''
    MAIL_DEFAULT_SENDER    = ''
    MAIL_MAX_EMAILS        = 1
    MAIL_SUPPRESS_SEND     = TESTING
    MAIL_ASCII_ATTACHMENTS = False
    FLASK_ENV =  'development'
    


class DevelopmentConfig(Config):
    DEBUG = True
    


config ={
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
