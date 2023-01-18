import json

class TermColors:
    def colorize(self, _type: str = 'info', _content: str = ''):
        _colors = {
            'info': '\033[100m',
            'success': '\033[1m',
            'warning': '\033[93m',
            'fail': '\033[91m',
            'end': '\033[0m'
        }

        return '{}{}{}'.format(_colors[_type], _content, _colors['end'])


class BuildCoverLetter:

    def __init__(self, mapping):
        self._company = None
        self._title = None
        self._closing = None
        self._tc = TermColors()
        self._mapping = mapping
        self._intro_art = " ______  __ __    ___      __ __  __ __  ____   " \
                          "______\n|      ||  |  |  /  _]    |  |  ||  |  ||" \
                          "    \ |      |\n|      ||  |  | /  [_     |  |  ||" \
                          "  |  ||  _  ||      |\n|_|  |_||  _  ||    _]    |" \
                          "  _  ||  |  ||  |  ||_|  |_|\n  |  |  |  |  ||   [" \
                          "_     |  |  ||  :  ||  |  |  |  |\n  |  |  |  |  |" \
                          "|     |    |  |  ||     ||  |  |  |  |\n  |__|  |" \
                          "__|__||_____|    |__|__| \__,_||__|__|  |__|     " \
                          "                                                   "
        self._intro_title = "                 Coverlettermajig               " \
                            "       "

        self._custom_salutation = {
            "question": "Do you know the name of the person you are contacting (Default: \"hiring manager\")?",
            "answer": False
        }
        self._salutation = "hiring manager"
        self._input_valprop = {
            "question": "Do you want to customize the valprop?",
            "answer": False
        }
        self._default_valprop = "With a deep understanding of the problem-solving process from start to finish, my " \
                                "recent job experience and education make me confident in applying for this position."

        # Initializing prints the intro art
        print('\n')
        print(self._intro_art)
        print(self._tc.colorize(_content=self._intro_title))
        print('\n')
        pass

    def identify_job(self):
        def _boolean_question(option):
            while True:
                _ans = input(self._tc.colorize(_content=option["question"] + " (y/N) "))
                break

            if _ans == '':
                pass
            else:
                if not _ans[0].lower() in ['y', 'n']:
                    print('Please answer with yes or no!')
                elif _ans[0].lower() == 'y':
                    option["answer"] = True
                    pass

        # Ask for name of company
        self._company = input(self._tc.colorize(
            _content="What is the name of the company? "))

        # Ask for job title
        self._title = input(self._tc.colorize(
            _content="What is the job title? "))

        _boolean_question(self._custom_salutation)
        if self._custom_salutation["answer"]:
            # Ask to customize the salutation
            self._salutation = input(self._tc.colorize(
                _content="What's the name of the person you are contacting? "
            ))

        _boolean_question(self._input_valprop)

        if self._input_valprop["answer"]:
            # Ask to customize the intro
            self._default_valprop = input(self._tc.colorize(
                _content="Change the valprop here (this will be the first part of a comma-separated clause) "
            ))

        for i in self._mapping:
            _boolean_question(self._mapping[i])

        # _boolean_question(self._type_uxd)
        # _boolean_question(self._type_dev)
        # _boolean_question(self._type_des)

        self.build_output()

    def build_output(self):
        _content = []
        with open("data/content/content_intro.txt", "r", encoding="utf-8") as input_file:
            _copy = input_file.read()
            _copy = _copy.replace('{{ salutation }}', self._salutation)
            _copy = _copy.replace('{{ company }}', self._company)
            _copy = _copy.replace('{{ position }}', self._title)
            _copy = _copy.replace('{{ valprop }}', self._default_valprop)
            _content.append(_copy)

        for i in self._mapping:
            if self._mapping[i]["answer"]:
                with open("data/content/" + self._mapping[i]["file"], "r", encoding="utf-8") as input_file:
                    _content.append(input_file.read())
        # if self._type_uxd['answer'] is True:
        #     with open("data/content/content_experiencedesign.txt", "r", encoding="utf-8") as input_file:
        #         _content.append(input_file.read())
        #
        # if self._type_dev['answer'] is True:
        #     with open("data/content/content_development.txt", "r", encoding="utf-8") as input_file:
        #         _content.append(input_file.read())
        #
        # if self._type_des['answer'] is True:
        #     with open("data/content/content_design.txt", "r", encoding="utf-8") as input_file:
        #         _content.append(input_file.read())

        with open("data/content/content_outro.txt", "r", encoding="utf-8") as input_file:
            _content.append(input_file.read())

        print("\n".join(_content))
        # ctypes.windll.user32.MessageBoxW(0, "\n".join(_content),
        #                                  "Cover Letter", 0)
        pass


if __name__ == "__main__":
    f = open("./data/map.json")
    mapping = json.load(f)
    cover = BuildCoverLetter(mapping)
    cover.identify_job()
