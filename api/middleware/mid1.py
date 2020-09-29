from typing import Any, Dict

import falcon, pdb
from haps import Inject

from api.middleware import Middleware
from api.resources import Resource
from core.registry import Registry


class Mid1Middleware(Middleware):
    '''
    Registry - is a place to store your variables/objects that you need in a global scope.
    '''
    registry: Registry = Inject()

    def process_request(self, req: falcon.Request, resp: falcon.Response) -> None:
        token = req.auth
        print('TTTTTTTTTTTTTTTTTOKEN TOKEN TOKEN')
        print(repr(req.auth))
        print('TOKEN TOKEN TOKEN')
        if not token:
            return
        token_type, _, access_token = token.partition(" ")
        if token_type == "Bearer":
            self.registry.access_token = access_token  # type: ignore

    def process_resource(
        self,
        req: falcon.Request,
        resp: falcon.Response,
        resource: Resource,
        params: Dict[str, Any],
    ) -> None:
        pass  # do nothing
        # raise BaseException('%%%% -- BB process_resource-- test test test %%%%')

    def process_response(
        self, req: falcon.Request, resp: falcon.Response, resource: Resource
    ) -> None:
        pass
        # raise BaseException('%%%% -- CC process_responce-- test test test %%%%')
