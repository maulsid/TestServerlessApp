import pathlib
from uuid import uuid4

from litestar import Litestar, Request, Router, get
from litestar.openapi import OpenAPIConfig
from litestar.openapi.spec import Components, SecurityScheme
from litestar.response import Redirect
from mangum import Mangum

from controllers.order_controller import OrderController


@get("/", include_in_schema=False)
async def redirect_to_docs() -> Redirect:
    return Redirect(path="/portal/schema")


route_handlers = [
    redirect_to_docs,
    Router(
        path="/portal",
        route_handlers=[
            OrderController,
        ],
    ),
]

openapi_components = Components(
    security_schemes={"BearerToken": SecurityScheme(type="http", scheme="bearer")}
)

openapi_config = OpenAPIConfig(
    title="B2B Admin API",
    version="1.0.0",
    description=(pathlib.Path(__file__).parent / "openapi_description.md").read_text(),
    security=[{"BearerToken": []}],
    components=openapi_components,
)


def _get_correlation_id(request: Request) -> str:
    """Return AWS' request id if possible, otherwise randomize the id."""
    try:
        return request.scope["aws.context"].aws_request_id
    except (AttributeError, KeyError):
        return str(uuid4())


app = Litestar(
    route_handlers=route_handlers,
    before_request=lambda req: req.app.state.setdefault(
        "correlation_id", _get_correlation_id(req)
    ),
    debug=True,
    openapi_config=openapi_config,
)

handler = Mangum(app)
