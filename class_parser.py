from datetime import datetime, timedelta
import json
import notifier


class ConfigJsonParser:

    """
    Represents a parse for a configuration json
    """
    @staticmethod
    def parse(path):
        """
        Parses the config JSON and returns a json object representing
        a class
        :param path: The path to the configuration json
        :return: a JSON object representing a class
        """
        config = None
        with open(path) as config_json:
            config = json.load(config_json)
        return config['class']


class Class:
    """
    Represents a Class schedule for a quarter/semester
    """
    _start = None
    _name = None
    _code = None
    _weeks = []

    def __init__(self, config):
        """
        Initializes Class member variables according to the config
        :param config: configuration JSON object representing a class
        """
        self._name = config['name']
        self._code = config['code']
        self._weeks = config['weeks']
        self._start = datetime.strptime(config['start'], "%Y-%m-%d").date()

    def notify(self):
        """
        Checks the current date and calculates the week difference from start
        date of the class. Sends out Mac notification with the corresponding
        week topic
        :return:
        """
        current_date = datetime.now().date()
        # subtracts week_between result by 1 to get index for _weeks
        week_index = self.weeks_between(self._start, current_date) - 1
        week_num_string = "Week {}".format(self._weeks[week_index]['number'])
        week_topic = self._weeks[week_index]['topic']
        # Mac Notification
        notifier.notify(self._code, week_num_string, week_topic)

    @staticmethod
    def weeks_between(start_date, end_date):
        """
        Calculates the number of weeks between a start and end date
        :param start_date: The date to start at
        :param end_date: The date to end at
        :return: Int representation of the number of weeks between start_date
                 and end date
        """
        weeks_count = (end_date - start_date).days / 7
        return int(weeks_count)


cs236 = Class(ConfigJsonParser.parse('cs236.json'))
cs236.notify()
