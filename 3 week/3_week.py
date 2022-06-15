class TestExample:
    expected_sum = 15
    def test_check_math(self):
        a = 6
        b = 9
        expected_sum = 15
        assert a+b == expected_sum, f"Sum of variable a and b is not equal to {expected_sum}"

    def test_check_math2(self):
        a = 6
        b = 9
        expected_sum = 11
        assert a+b == expected_sum, f"Sum of variable a and b is not equal to {expected_sum}"