import pytest

@pytest.fixture(params=["", "Первая\nВторая", "   ", "Привет", "a\r\nb", "a\tb", "🙂", "café"])
def text_value(request):
    return request.param
