from unittest import mock

from homework04.task02 import count_dots_on_i


def test_function():
    def fake_urlopen(url):
        class FakeResponse:
            def __init__(self):
                self.text = b"<title>script</title>"

            def read(self):
                return self.text

        return FakeResponse()

    with mock.patch("urllib.request.urlopen", fake_urlopen):
        assert count_dots_on_i("https://example.com/") == 3
