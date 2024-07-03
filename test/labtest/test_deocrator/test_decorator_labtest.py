import labtest
from labtest.registry import Registry


def test_decorator_labtest_one_function():
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_decorator_labtest_one_function():
        """mock function"""

    assert len(registry.labtests) == 1
    assert sorted(registry.labtests) == [
        f"{__name__}:mock_test_decorator_labtest_one_function",
    ]


def test_decorator_labtest_two_functions():
    registry = Registry(is_singleton=False)

    @labtest.register(registry)
    def mock_test_decorator_labtest_two_functions_alpha():
        """mock function"""

    @labtest.register(registry)
    def mock_test_decorator_labtest_two_functions_beta():
        """mock function"""

    assert len(registry.labtests) == 2
    assert sorted(registry.labtests) == [
        f"{__name__}:mock_test_decorator_labtest_two_functions_alpha",
        f"{__name__}:mock_test_decorator_labtest_two_functions_beta",
    ]