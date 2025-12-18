def slugify(text: str) -> str:
    """Turn 'Report Name' → 'report-name'."""
    return text.lower().replace(" ", "-")

print(slugify("My Report 01"))