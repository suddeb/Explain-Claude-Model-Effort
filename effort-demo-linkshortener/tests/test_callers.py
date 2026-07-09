from linkshortener.store import LinkStore
from linkshortener.cli import shorten_command
from linkshortener.stats import preview_code

def test_store_roundtrip():
    s = LinkStore()
    code = s.save("https://x.com")
    assert s.resolve(code) == "https://x.com"

def test_cli_builds_url():
    assert shorten_command("https://x.com").startswith("https://tpo.link/")

def test_stats_preview():
    out = preview_code("https://x.com")
    assert "code" in out and len(out["code"]) == 6
