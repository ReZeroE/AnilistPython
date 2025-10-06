"""
Translation and search related exceptions.
"""

class BaseError(Exception):
    """
    Base error structure class.
    """

    def __init__(self, val, message):
        """
        Initialize base error.

        :param val: actual value
        :param message: message shown to the user
        """
        self.val = val
        self.message = message
        super().__init__()

    def __str__(self):
        return "Error Code {} --> {}".format(self.val, self.message)


class TranslationError(BaseError):
    """
    Exception thrown if the translation has failed.
    """

    def __init__(self, val, message="There is an error while executing translation. Translation is dependent on Google services. Please try again later."):
        super().__init__(val, message)


class InvalidInput(BaseError):
    """
    Exception thrown if the user inputted an invalid name.
    """

    def __init__(self,
                 val,
                 message='Your search input is invalid. Please try a different name or refrain from using translation with this name.'):
        super().__init__(val, message)


# Legacy aliases for backward compatibility
DeepSearchError = TranslationError