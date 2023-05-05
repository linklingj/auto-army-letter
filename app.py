from datetime import datetime, timedelta
from press_crawler import send_press
from sports_crawler import send_sports_data
from sender import send

if __name__ == '__main__':
    letter_cnt = 1
    sent = False

    while True:
        now = datetime.today()
        if now.hour == 15 and (now.minute == 44 or now.minute == 46):
            if not sent:
                today = now.strftime('%Y%m%d')
                yesterday = (now - timedelta(days=1)).strftime('%Y%m%d')

                try:
                    title = '¿Œ∆Ì' + str(letter_cnt) + ' ' + today[4:]
                    letter = ''
                    letter += send_press()
                    letter += send_sports_data(yesterday)
                    letter += send_sports_data(today)

                    #print(letter)
                    send(title, letter)

                    with open('army_letter_project/letter_log.txt','a') as f:
                        f.write(letter)
                        f.write('-' * 20 + '\n')
                    with open('army_letter_project/excecution_log.txt','a') as f:
                        f.write(f"\n[+] {datetime.now()} - Success")

                    letter_cnt += 1
                    sent = True

                except:
                    print(f"[+] {now} - Fail")
        else:
            sent = False