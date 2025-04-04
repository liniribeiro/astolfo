from http import HTTPStatus


class Error(Exception):
    """
    Exceçoes tratadas do sistema.
    Quando ocorre algum erro em API, é retornado o código e o nome do erro que ocorreu.
    Desta forma, podemos criar um tratamento no frontend para mostrar algum feedback para o usuário.
    """
    data = {}
    error = None
    status = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__(*args)
        self.data = kwargs.get("data")
        self.status = kwargs.get("status", self.status)
        self.error = kwargs.get("error")


class CreateError(Error):
    def __str__(self):
        return f"create-error: {self.error}"

class PayloadError(Error):
    def __str__(self):
        return "payload-error"


class NotAuthorizedError(Error):
    def __str__(self):
        return "not-authorized-error"


class DuplicatedData(Error):
    def __str__(self):
        return "duplicated-data"


class UpdateDataError(Error):
    def __str__(self):
        return "update-data-error"


class PlanUsingTaskError(Error):
    def __str__(self):
        return "plan-using-task"
