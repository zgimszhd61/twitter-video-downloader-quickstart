# Twitter视频下载器 2.0

![使用Python制作的徽章](http://ForTheBadge.com/images/badges/made-with-python.svg)

![点击量](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fz1nc0r3%2Ftwitter-video-downloader&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)

---
这是一个Python脚本，可以让你通过终端从Twitter下载视频。你只需要提供一个Twitter帖子的URL，脚本就会提取出最高质量的视频链接并下载。

## 使用前提

- Python 3.x
- requests库（使用`pip install requests`命令安装）
- bs4库（使用`pip install beautifulsoup4`命令安装）
- tqdm库（使用`pip install tqdm`命令安装）

## 使用方法

1. 克隆仓库：

   ```bash
   git clone https://github.com/your-username/twitter-video-downloader.git

2. 进入项目目录：

   ```bash
   cd twitter-video-downloader

3. 安装所需的包

   ```bash
   pip install -r requirements.txt

4. 运行脚本，并将视频URL作为参数

   ```bash
   python twitter_downloader.py {视频url}

   例如：python twitter_downloader.py https://x.com/realmadriden/status/1743790569866821949?s=20

## 注意

- 本脚本依赖外部网站[twitsave.com](https://twitsave.com)来检索视频URL进行下载。它使用twitsave.com提供的API来获取视频详情。
- 请确保你有稳定的互联网连接，并能够访问twitsave.com，以便脚本正常工作。
- 我和这个项目与[twitsave.com](https://twitsave.com)没有任何关联。使用该脚本通过twitsave.com的服务时，请审查并遵守[twitsave.com/terms](https://twitsave.com/terms)的条款和条件。