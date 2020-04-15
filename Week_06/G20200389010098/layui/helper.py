from flask import Blueprint

class NestableBlueprint(Blueprint):
    def register_blueprint(self, blueprint, **options):
        def deferred(state):
            url_prefix = (state.url_prefix or u"") + (options.get('url_prefix', blueprint.url_prefix) or u"")
            if 'url_prefix' in options:
                del options['url_prefix']
            state.app.register_blueprint(blueprint, url_prefix=url_prefix, **options)
        self.record(deferred)
import random

def getRandStr(length = 16 , specialChars = False):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    if (specialChars):
        chars += '!@#$%^&()'
    return random.sample(chars,length)
