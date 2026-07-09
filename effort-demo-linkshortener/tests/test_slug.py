from linkshortener.slug import generate_slug

def test_slug_is_deterministic():
    assert generate_slug("https://a.com") == generate_slug("https://a.com")

def test_slug_length():
    assert len(generate_slug("https://a.com")) == 6

def test_different_urls_differ():
    assert generate_slug("https://a.com") != generate_slug("https://b.com")
