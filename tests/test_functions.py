import pytest

from onlytld import get_tld


@pytest.mark.parametrize(
    "domain, tld",
    [
        ("chinese.cn", "cn"),
        ("hk", "hk"),
        ("abersheeran.com", "com"),
        ("google.cn", "cn"),
        ("www.lijinlong.cc", "cc"),
        ("a.com.cn", "com.cn"),
        ("ahnu.edu.cn", "edu.cn"),
        ("www.ck", "ck"),
        ("www.moanasands.co.ck", "co.ck"),
        ("co.ck", "co.ck"),
        ("adf.yokohama.jp", "adf.yokohama.jp"),
        ("city.yokohama.jp", "yokohama.jp"),
        ("aber.dfsdf", None),
        ("aber", None),
    ],
)
def test_get_tld(domain: str, tld: str) -> None:
    assert get_tld(domain) == tld
