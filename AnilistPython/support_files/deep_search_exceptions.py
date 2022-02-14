class BaseError(Exception):
    """
    base error structure class
    """

    def __init__(self, val, message):
        """
        @param val: actual value
        @param message: message shown to the user
        """
        self.val = val
        self.message = message
        super().__init__()

    def __str__(self):
        return "Error Code {} --> {}".format(self.val, self.message)


class DeepSearchError(BaseError):
    """
    exception thrown if the deep-search has failed
    """

    def __init__(self, val, message="There is an error in while executing deep-search. Deep-search is dependent on Google services. Please try again later."):
        super().__init__(val, message)


class InvalidInput(BaseError):
    """
    exception thrown if the user inputted an invalid name
    """

    def __init__(self,
                 val,
                 message='Your search input is invalid. Please try a different name or refrain from using deep-search with this name.'):
        super().__init__(val, message)