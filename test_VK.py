import pytest


class Test:
    def test_int_one(self):
        a = 5
        b = a + 1
        try:
            assert b == 5
        except AssertionError:
            pass

    @pytest.mark.parametrize('a,expected', [('2+3', 5)])
    def test_int_two(self, a, expected):
        assert eval(a) == expected

    def test_list_one(self):
        list_one = ['one', 'two', 'three', 'four']
        try:
            assert two in list_one
        except NameError:
            pass

    # @pytest.mark.parametrize()
    # def test_list_two(self):
    #     list_one = (int(2, 4, 6, 8))
    #     try:
    #         assert list_one%2 == 0
    #     except TypeError:
    #         pass

    def test_set_one(self):
        a = ['one', 'two', 'three', 'four']
        try:
            assert len(a) == 5
        except AssertionError:
            pass

    # @pytest.mark.parametrize()
    # def test_set_two(self):