# Кастомный обработчик ошибок

class BaseAgent(Exception): pass

class BackendError(BaseAgent): pass
