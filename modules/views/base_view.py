

class BaseView:
    
    def __init__(self):
        self._rule = None
        self._endpoint = None
        self.get_alloweds = ["GET"]
        self.initial_view
    
    @staticmethod
    def view(cls):
        pass
    
    @property
    def get_rule(self):
        return self._rule

    @property
    def get_endpoint(self):
        return self._endpoint
    
    @property
    def initial_view(self):
        return
