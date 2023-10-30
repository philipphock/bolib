
class Float01(float):
    def __new__(cls, value):
        if 0 <= value <= 1:
            return super(Float01, cls).__new__(cls, value)
        else:
            raise ValueError(f"Value must be between 0 and 1, this one is {value}")

    @staticmethod
    def get_max_dist(num):
        diff_from_0 = abs(num - 0)
        diff_from_1 = abs(num - 1)
    
        # Choose the number with the larger absolute difference
        if diff_from_0 > diff_from_1:
            return Float01(0), diff_from_0
        else:
            return Float01(1), diff_from_1