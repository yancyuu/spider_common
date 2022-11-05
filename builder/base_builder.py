class BaseBuilder:

    @property
    def params(self):
        return self._params

    @property
    def headers(self):
        return self._headers

    def __init__(self, params=None, headers=None):
        self._params = params
        self._headers = headers

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]

    def __setattr__(self, key, value):
        self.__dict__[key] = value
