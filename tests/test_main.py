import sys

import pytest

import main


@pytest.mark.parametrize("url, expected", [
    ("https://www.njit.edu", True),
    ("http://github.com/Chima765432", True),
    ("not a url", False),
    ("www.missing-scheme.com", False),
])
def test_is_valid_url(url, expected):
    assert main.is_valid_url(url) is expected


def test_create_directory_makes_nested_folders(tmp_path):
    target = tmp_path / "a" / "b"
    main.create_directory(target)
    assert target.is_dir()


def test_generate_qr_code_saves_png(tmp_path):
    path = tmp_path / "code.png"
    main.generate_qr_code("https://www.njit.edu", path)
    assert path.read_bytes().startswith(b"\x89PNG")


def test_generate_qr_code_skips_invalid_url(tmp_path):
    path = tmp_path / "code.png"
    main.generate_qr_code("not a url", path)
    assert not path.exists()


def test_main_writes_qr_code_to_directory(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["main.py", "--url", "https://www.njit.edu"])
    main.main()
    files = list((tmp_path / main.QR_DIRECTORY).glob("QRCode_*.png"))
    assert len(files) == 1
