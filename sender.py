import thecampy
from credential import user_id, user_pw, soldier_name

my_soldier = thecampy.Soldier(soldier_name)

def send(title, message):
    if len(message) > 1500:
        return False
    
    message = '<p>' + message.replace('\n', '</p><p>') + '</p>'
    message = message.replace('<p></p>', '<p>&nbsp</p>')

    try:
        msg = thecampy.Message(title, message)
        tc = thecampy.Client(user_id, user_pw)
        tc.get_soldier(my_soldier)
        tc.send_message(my_soldier, msg)
        return True
    except Exception as p:
        return False