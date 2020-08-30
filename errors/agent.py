# Кастомный обработчик ошибок

class BaseAgent(Exception): pass

class BackendError(BaseAgent): pass

class ApiError(BaseAgent): pass

class ApiErrorNotYetSkill(BaseAgent): pass
