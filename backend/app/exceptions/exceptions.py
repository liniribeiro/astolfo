from http import HTTPStatus


class Error(Exception):
    """
    Exceçoes tratadas do sistema.
    Quando ocorre algum erro em API, é retornado o código e o nome do erro que ocorreu.
    Desta forma, podemos criar um tratamento no frontend para mostrar algum feedback para o usuário.
    """
    content = {}
    error = None
    status_code = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__(*args)
        self.name = kwargs.get("name")
        self.description = list(args)
        self.detail = kwargs.get("detail", None)
        self.status_code = kwargs.get("status_code", self.status_code)

    def to_dict(self):
        return {
            "error": {
                "name": self.name,
                "description": self.description,
                "detail": self.detail,
            },
        }


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
    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = "duplicated-data"
        self.status_code = HTTPStatus.BAD_REQUEST

class NotFound(Error):
    def __init__(self, *args: object, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = "not-found"
        self.status_code = HTTPStatus.NOT_FOUND

class UpdateDataError(Error):
    def __str__(self):
        return "update-data-error"


class PlanUsingTaskError(Error):
    def __str__(self):
        return "plan-using-task"
