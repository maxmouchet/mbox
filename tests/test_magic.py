from mtoolbox.magic import CompressionFormat, detect_compression


def test_detect_compression():
    assert detect_compression("tests/data/hello.txt") == CompressionFormat.Unknown
    assert detect_compression("tests/data/hello.txt.zst") == CompressionFormat.Zstandard
