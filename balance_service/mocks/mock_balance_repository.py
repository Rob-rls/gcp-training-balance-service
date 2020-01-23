from json import loads, dumps


class MockBalanceRepository():
    def __init__(self, config_prefix='FIRESTORE_BALANCE_COLLECTION'):
        self._store = dict()
        self.config_prefix = config_prefix

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions[self.config_prefix.lower()] = self

    def store(self, account_number, account_data):
        self._store[account_number] = dumps(account_data)

    def fetch_by_account_number(self, account_number):
        result = self._store.get(account_number)
        if result is None:
            return None
        return loads(result)
