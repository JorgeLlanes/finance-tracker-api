from anthropic import Anthropic
from app.config import settings
from app.ai.constants import ANTHROPIC_MODEL
from app.ai.exceptions import AIServiceUnavailableError

client = Anthropic(api_key=settings.anthropic_api_key)


def categorize_transaction(description: str) -> str:
    """
    Categorize a transaction based on its description.

    Args:
        description: The description of the transaction
    Returns:
        The category name in lowercase
    """
    try:
        message = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=20,
            system="You are a helpful assistant that categorizes transactions based on their description, return just the category name, no other text. Example: 'Netflix subscription' → subscription",
            messages=[{"role": "user", "content": description}],
        )
        return message.content[0].text.strip().lower()
    except Exception:
        raise AIServiceUnavailableError()
