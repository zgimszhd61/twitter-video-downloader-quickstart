# 导入pytest测试框架和requests库
import pytest
import requests

# 使用pytest的标记功能定义一个集成测试
@pytest.mark.integration
def test_extern_status():
    """
    测试twitsave.com的托管状态
    """
    # 定义要测试的网站地址
    HOST = "https://twitsave.com"
    
    # 使用requests库发送一个HEAD请求，这种请求方法用于获取服务器头部信息
    response = requests.head(HOST)
    
    # 断言响应的状态码是否为200，200表示请求成功，网站正常运行
    assert response.status_code == 200