# class creates a new quote objects.


class QuoteModel:
    """Create new quote."""

    def __init__(self, body, author):
        """Initialize quote."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return str with "quote body text" - author."""
        return f"{self.body} - {self.author}"
