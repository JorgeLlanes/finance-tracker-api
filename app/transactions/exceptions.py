class TransactionError(Exception):
    """Base exception for all transaction-related errors."""

    pass


class TransactionNotFoundError(TransactionError):
    def __init__(self, transaction_id: int):
        self.transaction_id = transaction_id
        message = f"Transaction with id {transaction_id} not found"
        super().__init__(message)
