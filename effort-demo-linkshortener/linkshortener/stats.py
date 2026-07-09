from .slug import generate_slug

# CALLER #3 — the easy-to-forget one, in a different-feeling module.
def preview_code(url: str) -> dict:
    return {"url": url, "code": generate_slug(url)}
