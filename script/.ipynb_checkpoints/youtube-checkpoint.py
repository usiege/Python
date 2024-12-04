from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=7G6FfKXvZX8')
# yt.streams.get_highest_resolution().download()

yt.streams.filter(file_extension="mp4").all()

# 400 1440P video mp4
# yt.streams.get_by_itag(400).download(output_path="UE4_WOW_400") 
# 140 audio/mp4 128kbps
# yt.streams.get_by_itag(140).download(output_path="TBC_Ret_Paladin_VoidReaver_2900DPS_140")

# 299 1080P60 video mp4
# 399 1080P video mp4
# yt.streams.get_by_itag(299).download(output_path="StromCity299")

yt.streams.get_by_itag(140).download(output_path="Fj-z1bakYMg140")
# yt.streams.get_by_itag(137).download(output_path="Fj-z1bakYMg")
# yt.streams.get_by_itag(299).download(output_path="Fj-z1bakYMg299")
# yt.streams.get_by_itag(399).download(output_path="Fj-z1bakYMg")