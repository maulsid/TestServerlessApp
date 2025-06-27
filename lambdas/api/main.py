import os
from uuid import uuid4

from litestar import Litestar, Router, get
from litestar.openapi import OpenAPIConfig
from litestar.openapi.spec import Components, SecurityScheme
from litestar.response import Redirect
from mangum import Mangum

from controllers.order_controller import OrderController

@get("/", include_in_schema=False)
def redirect_to_docs() -> Redirect:
    return Redirect(path="/portal/schema")

def create_app() -> Litestar:
    return Litestar(
        route_handlers=[
            redirect_to_docs,
            Router(
                path="/portal",
                route_handlers=[
                    OrderController,
                ],
            )
        ],
        before_request=lambda req: req.app.state.setdefault("correlation_id", str(uuid4())),
        debug=True,
        openapi_config=OpenAPIConfig(
            title="B2B Admin API",
            version="1.0.0",
            description=(
                "## Usage\n\n"
                "To use this API, obtain an access token using client credentials flow:\n\n"
                "**Token Endpoint:**\n"
                "POST https://auth.{env}.cdf.otsuka-oph.org/oauth2/token\n\n"
                "**Payload:**\n"
                "```x-www-form-urlencoded\n"
                "grant_type=client_credentials\n"
                "client_id=YOUR_CLIENT_ID\n"
                "client_secret=YOUR_CLIENT_SECRET\n"
                "```\n\n"
                "**Response:**\n"
                "```json\n"
                "{'access_token': 'XYZ'}\n"
                "```"
            ),
            components=Components(
                security_schemes={
                    "BearerToken": SecurityScheme(
                        type="http",
                        scheme="bearer"
                    )
                }
            ),
            security=[{"BearerToken": []}],
        )
    )

app = create_app()
handler = Mangum(app)