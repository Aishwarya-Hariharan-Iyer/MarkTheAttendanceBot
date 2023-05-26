from datetime import datetime

def responses(input):
    user_message = str(input).lower()

    if user_message in ('hello'):
        return "Hey! How's it going?"

    if user_message in ('who are you'):
        return "I am Mark, the Attendance Bot!"

    if user_message in ("give me the time now"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "What's that again?"