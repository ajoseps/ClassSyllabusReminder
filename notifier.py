import os

# The notifier function
def notify(title, subtitle, message):
    """
    Displays an MacOS notification to the user
    ref: http://stackoverflow.com/questions/17651017/python-post-osx-notification

    :param title: Title of the notification
    :param subtitle: Subtitle of the notification
    :param message: Message of the notification
    :return:
    """
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))