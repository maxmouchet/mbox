from pathlib import Path

from mtoolbox.requests import RequestsMock

hello = Path(__file__).parent / "data" / "hello.txt"


def test_mock():
    mock = RequestsMock()
    mock.register(r".*hello.world", hello)

    res1 = mock.request("GET", "www.hello.world")
    assert res1.text == hello.read_text()

    res2 = mock.request("GET", "www.example.com")
    assert res2.status_code == 404
