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
        ("这里是.中国", "中国"),
        ("xn--wnuw27a.xn--fiqs8s", "xn--fiqs8s"),
        ("hello.信息", "信息"),
        ("中国.cn", "cn"),
        ("中国.xn--fiqs8s", "xn--fiqs8s"),
        ("xn--12co0c3b4eva.ไทย", "xn--12co0c3b4eva.xn--o3cw4h"),
    ],
)
def test_get_tld(domain: str, tld: str) -> None:
    assert get_tld(domain) == tld
