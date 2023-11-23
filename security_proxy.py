class SecurityProxy:
    def __init__(self, target):
        self._target = target

    def get_army_data(self, user):
        if user == "authorized_user":
            return self._target.get_army()
        else:
            raise PermissionError("Unauthorized access")
