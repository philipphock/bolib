
class Float01(float):
    def __new__(cls, value):
        if 0 <= value <= 1:
            return super(Float01, cls).__new__(cls, value)
        else:
            raise ValueError(f"Value must be between 0 and 1, this one is {value}")
