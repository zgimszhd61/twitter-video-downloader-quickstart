# 导入pytest测试框架
import pytest
# 导入urllib.parse模块中的urlparse函数，用于解析URL
from urllib.parse import urlparse

# 使用pytest的mark功能标记这是一个单元测试
@pytest.mark.unit
def test_domain_valid():
    """
    测试函数：验证URL的域名是否为预期的值。
    本例中，我们将检查域名是否等于'twitter.com'。
    """
    # 定义一个URL字符串，这里应该是一个标准的Twitter媒体链接。
    # 但是为了测试，这里使用了"x.com"作为域名。
    url = "https://x.com/realmadriden/status/1743790569866821949?s=20"

    # 使用urlparse函数解析上面定义的URL
    parsed_url = urlparse(url)

    # 使用assert断言检查解析出的域名是否与预期的"x.com"一致
    # 如果不一致，测试将失败。
    assert parsed_url.hostname == "x.com"