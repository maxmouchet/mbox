from pathlib import Path

from requests import Session

from mtoolbox.requests import FTPAdapter, RequestsMock

hello = Path(__file__).parent / "data" / "hello.txt"
iso3166 = Path(__file__).parent / "data" / "iso3166-countrycodes.txt"


def test_ftp():
    session = Session()
    session.mount("ftp://", FTPAdapter())
    res = session.get("ftp://ftp.ripe.net/iso3166-countrycodes.txt")
    assert res.text == iso3166.read_text()


def test_mock():
    mock = RequestsMock()
    mock.register(r".*hello.world", hello)

    res1 = mock.request("GET", "www.hello.world")
    assert res1.text == hello.read_text()

    res2 = mock.request("GET", "www.example.com")
    assert res2.status_code == 404
