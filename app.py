import requests
from mail import mail
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


def getYellowIpe():
    url = "https://yellowipe.io/api/vacancies/?method=GET"
    response = requests.get(url=url).json()

    for i in range(len(response)):
        if 'Python' in response[i]['tags']:
            idVacancie = response[i]['idVacancie']
            title = response[i]['title']
            positionDescription = response[i]['positionDescription']
            location = response[i]['location']
            workplacePolicy = response[i]['workplacePolicy']
            tags = response[i]['tags']
            url = f'https://yellowipe.io/vacancies/{idVacancie}'
            f = open('database.txt', 'r+')
            if idVacancie in f.read():
                pass
            else:
                mail(idVacancie, title, positionDescription,
                     location, workplacePolicy, tags, url)
                f.write(f'{idVacancie}\n')


sched.add_job(getYellowIpe, "interval", minutes=60)

sched.start()
