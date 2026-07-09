import hashlib

# The core helper. In the demo you ask Claude to RENAME this to
# `generate_short_code` and add a `length` parameter.
# A low-effort run tends to rename the def + maybe one caller,
# then stop WITHOUT running the tests -> other callers break.
def generate_slug(url: str) -> str:
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()
    return digest[:6]
