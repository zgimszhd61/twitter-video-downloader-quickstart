# 导入所需的库
import sys
import os
import re
import requests
import bs4
from tqdm import tqdm
from pathlib import Path

# 定义一个函数，用于下载视频
def download_video(url, file_name) -> None:
    """
    从URL下载视频到指定的文件名中。

    参数:
        url (str): 要下载的视频URL
        file_name (str): 保存视频的文件名或路径。
    """

    # 发起请求，获取响应
    response = requests.get(url, stream=True)
    # 获取内容总大小
    total_size = int(response.headers.get("content-length", 0))
    # 设置块大小
    block_size = 1024
    # 初始化进度条
    progress_bar = tqdm(total=total_size, unit="B", unit_scale=True)

    # 构建下载路径
    download_path = os.path.join(Path.home(), "Downloads", file_name)

    # 以二进制写模式打开文件
    with open(download_path, "wb") as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    # 关闭进度条
    progress_bar.close()
    print("视频成功下载！")
    print("视频地址"+download_path)

# 定义一个函数，用于下载Twitter视频
def download_twitter_video(url):
    """
    提取并下载Twitter帖子中的最高质量视频URL。

    参数:
        url (str): 要下载的Twitter帖子URL
    """

    # 构建API URL
    api_url = f"https://twitsave.com/info?url={url}"

    # 发起请求，获取响应
    response = requests.get(api_url)
    data = bs4.BeautifulSoup(response.text, "html.parser")
    # 查找下载按钮
    download_button = data.find_all("div", class_="origin-top-right")[0]
    # 查找质量选择按钮
    quality_buttons = download_button.find_all("a")
    # 获取最高质量视频的URL
    highest_quality_url = quality_buttons[0].get("href")
    
    # 获取视频文件名
    file_name = data.find_all("div", class_="leading-tight")[0].find_all("p", class_="m-2")[0].text
    # 清理文件名中的特殊字符
    file_name = re.sub(r"[^a-zA-Z0-9]+", ' ', file_name).strip() + ".mp4"
    
    # 调用下载视频函数
    download_video(highest_quality_url, file_name)

# 检查命令行参数
if len(sys.argv) < 2:
    print("请提供Twitter视频URL作为命令行参数。\n例如: python twitter_downloader.py <URL>")
else:
    url = sys.argv[1]
    if url:
        download_twitter_video(url)
    else:
        print("提供的Twitter视频URL无效。")