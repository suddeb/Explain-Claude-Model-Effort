from .slug import generate_slug

# CALLER #1
class LinkStore:
    def __init__(self):
        self._by_code = {}

    def save(self, url: str) -> str:
        code = generate_slug(url)
        self._by_code[code] = url
        return code

    def resolve(self, code: str) -> str | None:
        return self._by_code.get(code)
