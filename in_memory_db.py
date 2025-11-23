class TransactionError(Exception):
    pass


class InMemoryDB:
    def __init__(self):
        self._store = {}
        self._in_tx = False
        self._buffer = {}

    def begin_transaction(self):
        if self._in_tx:
            raise TransactionError("Transaction already started")
        self._in_tx = True
        self._buffer = {}

    def put(self, key, val):
        if not self._in_tx:
            raise TransactionError("No transaction active")
        if type(key) is not str:
            raise TypeError("Key must be a string")
        if type(val) is not int:
            raise TypeError("Value must be an int")
        self._buffer[key] = val

    def get(self, key):
        if type(key) is not str:
            raise TypeError("Key must be a string")
        # does NOT return uncommitted values
        if key in self._store:
            return self._store[key]
        return None

    def commit(self):
        if not self._in_tx:
            raise TransactionError("Nothing to commit")
        for k, v in self._buffer.items():
            self._store[k] = v
        self._in_tx = False
        self._buffer = {}

    def rollback(self):
        if not self._in_tx:
            raise TransactionError("Nothing to rollback")
        self._in_tx = False
        self._buffer = {}

    def __repr__(self):
        return f"InMemoryDB(store={self._store})"
