from urllib import request

responce = request.urlopen('https://www.youtube.com/@user-gx9fu7rb7q/videos')

x=responce.read().decode('utf-8')

def last_video():
    new_video = x.split('{"videoId":"')[1].split('",')[0]
    return new_video
    #print('Ссылка на последнее видо МИШИ ТОРА')


print(last_video())