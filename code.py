import requests

API_KEY = "your-youtube-api-v3-key"
YOUTUBE_LINK_WITHOUT_VIDEO_ID = "https://www.youtube.com/watch?v="
dic = {}


# Method made by Kalob Taulien from Stack Overflow
def get_youtube_video_duration(video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={video_id}&key={API_KEY}"

    response = requests.get(url)  # Perform the GET request
    data = response.json()  # Read the json response and convert it to a Python dictionary

    return data['items'][0]['contentDetails']['duration']


def get_youtube_video_id(youtube_link):
    return youtube_link[32:-1]


def get_youtube_video_links_in_order_by_time():
    with open("youtube.txt", 'w') as final_file:
        for i in sorted(dic.keys()):
            # print(i, sorted(dic[i]))]
            for j in sorted(dic[i]):
                url = YOUTUBE_LINK_WITHOUT_VIDEO_ID + j[1] + '\n'
                final_file.write(url)


def insert(time):
    if time[0] in dic:
        dic[time[0]].append((time[1], time[2]))
    else:
        dic[time[0]] = [(time[1], time[2])]


with open("links.txt", 'r') as file:
    youtube_links = file.readlines()

    for link in youtube_links:
        vid_id = get_youtube_video_id(link)
        duration = get_youtube_video_duration(vid_id)[2:]
        video_time = [0, 0, vid_id]

        if duration[-1] == 'S':
            dur_str = duration[:-1].split("M")
            video_time[0], video_time[1] = int(dur_str[0]), int(dur_str[1])
        elif duration[-1] == 'M' and len(duration) < 4:
            video_time[0] = int(duration[:-1])
        else:
            dur_str = duration[:-1].split("H")
            video_time[0] = int(dur_str[0]) * 60 + int(dur_str[1])
            video_time[1] = 0

        insert(video_time)

    get_youtube_video_links_in_order_by_time()
