from typing import Dict
import falcon, pdb
from api.middleware.mid1 import Mid1Middleware
from api.resources.collections import (
    CollectionsResource
)
from haps import Container
from core.exceptions import NotAuthenticatedError
Container.autodiscover(["core"])

middleware = [
    Mid1Middleware(),
]



routes = [
    ("/test", CollectionsResource),
]


app = falcon.API(middleware=middleware)


def log(arg):
    pass
    with open('log.txt', 'a') as f:
        f.write(repr(arg))

for route, resource in routes:
    log([route, resource])
    app.add_route(route, resource())

def handle_authentication_error(
    exception: Exception,
    request: falcon.Request,
    response: falcon.Response,
    params: Dict,
) -> None:
    raise falcon.HTTPUnauthorized()


# configure dependency injection


app.add_error_handler(NotAuthenticatedError, handle_authentication_error)