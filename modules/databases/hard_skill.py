from .base import BackendMixin
from lib.util import validation

class HardSkill(BackendMixin):
    
    @validation
    def add(self, skill, **kwargs):
        print(skill)
        return
    
    @validation
    def remove(self, skill, **kwargs):
        return
    
    @validation
    def update(self, skill, **kwargs):
        return
    
    @validation
    def delete(self, skill, **kwargs):
        return
    
    def get(self, skill):
        return
    
