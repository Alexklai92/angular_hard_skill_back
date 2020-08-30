from .base import BackendMixin
from lib.util import validation

class HardSkill(BackendMixin):
    
    @validation
    def create(self, skill: dict, **kwargs) -> dict:
        return
    
    @validation
    def update(self, skill: dict, **kwargs) -> dict:
        return
    
    @validation
    def delete(self, skill: dict, **kwargs) -> bool:
        return
    
    def get(self, skill: dict) -> dict:
        return
    
