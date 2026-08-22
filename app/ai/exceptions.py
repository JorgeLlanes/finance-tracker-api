class AICategorizationError(Exception):
    """Base exception for all AI Categorization-related errors."""

    pass


class AIServiceUnavailableError(AICategorizationError):
    def __init__(self):
        message = "AI categorization service unavailable"
        super().__init__(message)
