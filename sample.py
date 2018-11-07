# sample.py

import falcon

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote
class HelloWorld:
    def on_get(self, req, resp):
        """Handles GET requests"""
        mes = "Hello"

        resp.media = mes

api = falcon.API()
api.add_route('/quote', QuoteResource())
api.add_route('/hello', HelloWorld())

