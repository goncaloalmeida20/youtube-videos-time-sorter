import isodate
import requests

API_KEY = "AIzaSyDYVzfYiGOmiYfC0xTGFYgQJStYvkp0kkE"
YOUTUBE_LINK_WITHOUT_VIDEO_ID = "https://www.youtube.com/watch?v="
dic = {}


# Method adapted to get the name too from Kalob Taulien code on Stack Overflow
def get_youtube_video_name_and_duration(video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={video_id}&key={API_KEY}&fields=items(contentDetails(duration), snippet(title))&part=snippet,contentDetails"

    response = requests.get(url)  # Perform the GET request
    data = response.json()  # Read the json response and convert it to a Python dictionary
    n_d = [data['items'][0]['snippet']['title'], data['items'][0]['contentDetails']['duration']]

    return n_d


def get_youtube_video_id(youtube_link):
    return youtube_link[32:-1]


def get_youtube_video_links_in_order_by_time():
    with open("C:\\Users\gonca\OneDrive - Universidade de Coimbra\Ambiente de Trabalho\youtube.txt", 'w', encoding='utf-8') as final_file:
        for i in sorted(dic.keys()):
            # print(i, sorted(dic[i]))]
            for j in sorted(dic[i]):
                name_and_url = j[0] + " - " + YOUTUBE_LINK_WITHOUT_VIDEO_ID + j[1] + '\n'
                final_file.write(name_and_url)


def insert(video_info):
    if video_info[0] in dic:
        dic[video_info[0]].append((video_info[1], video_info[2]))
    else:
        dic[video_info[0]] = [(video_info[1], video_info[2])]


with open("py.txt", 'r') as file:
    youtube_links = file.readlines()

    for link in youtube_links:
        vid_id = get_youtube_video_id(link)
        name_and_duration = get_youtube_video_name_and_duration(vid_id)
        name = name_and_duration[0]
        duration = isodate.parse_duration(name_and_duration[1]).total_seconds()

        vid_info = [duration, name, vid_id]

        insert(vid_info)

    get_youtube_video_links_in_order_by_time()
