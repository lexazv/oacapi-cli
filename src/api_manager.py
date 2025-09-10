import json
from typing import Any
from urllib.request import urlopen


def make_request(url: str) -> str | dict[Any, Any]:
    with urlopen(url) as response:
        body = response.read()
        try:
            output = json.loads(body)
        except json.decoder.JSONDecodeError:
            output = body
    return output
