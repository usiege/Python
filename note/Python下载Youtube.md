# Python下载Youtube

标签（空格分隔）： Python

---


参考文章：[pytube](https://blog.csdn.net/hezhefly/article/details/102531398)

## proxy

`VPN`

> https://glados.work

```
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
```

## youtube-dl（推荐）

> zsh: no matches found: https://www.youtube.com/watch?v=Bk7PRu_QZL0

```
unsetopt nomatch
```

- 视频质量
![image_1fpu6nnaj133f4fm8in142j1fos9.png-62kB][1]
```
youtube-dl -f best
youtube-dl -f bestvideo+bestaudio
youtube-dl -f 'bestvideo,bestaudio'
```

- 指定格式
```
youtube-dl -f mp4
```

- 仅下载音频
```
youtube-dl -x url
youtube-dl -x --audio-format mp3 url # 指定格式
```


- Windows脚本
```
@echo off
:start
set /p dir=请输入保存路径：
set dir=%dir:/=\%
pushd %dir%
if /i not %dir%==%cd% goto :start
echo 保存路径：%cd%
:download
set /p input=请输入视频链接：
set input=%input:&=^^^&%
youtube-dl -F %input%
if errorlevel 1 goto :download
set /p code=请输入视频格式编号：
youtube-dl -f %code% %input%
goto :download
```

## you-get

```
you-get --info(-i) https://www.youtube.com/watch?v=Bk7PRu_QZL0
```

## pytube

### 命令行

- 简单下载
```
pytube https://www.youtube.com/watch?v=Bk7PRu_QZL0
```

- 文档
> https://pytube.io/en/latest/index.html


### 完整代码

需要指定`itag`下载特定格式的内容：
```
from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=d08EdMcCS7s')
yt.streams.get_highest_resolution().download()

yt.streams.filter(file_extension="mp4").all()
itag = yt.streams.get_by_itag(299).download(output_path="")
# itag = 299 + 140
```




## yt-dlp

```
yt-dlp -f 299+140 --proxy socks5://127.0.0.1:7890 https://www.youtube.com/watch?v=UYmihSG2XLA

--merge-output-format mp4 --external-downloader aria2c --downloader-args aria2c:"-x 16 -k 1M"
```


  [1]: http://static.zybuluo.com/usiege/lcgsblw0d054e0zc6ir2rkg5/image_1fpu6nnaj133f4fm8in142j1fos9.png