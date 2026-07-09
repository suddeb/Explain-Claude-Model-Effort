from .slug import generate_slug

# CALLER #2
def shorten_command(url: str) -> str:
    code = generate_slug(url)
    return f"https://tpo.link/{code}"
