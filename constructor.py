import ctypes

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

    def __init__(self):
        self._company = None
        self._title = None
        self._closing = None
        self._dev = False
        self._ux = False
        self._design = False
        self._tc = TermColors()

        self._input_valprop = ''
        self._type_uxd = {
            "question": " Is this a UX focused job?",
            "answer": False
        }
        self._type_dev = {
            "question": " Is this a development focused job?",
            "answer": False
        }
        self._type_des = {
            "question": " Is this a design focused job?",
            "answer": False
        }

        self._intro_art = " ______  __ __    ___      __ __  __ __  ____   " \
                          "______\n|      ||  |  |  /  _]    |  |  ||  |  ||" \
                          "    \ |      |\n|      ||  |  | /  [_     |  |  ||" \
                          "  |  ||  _  ||      |\n|_|  |_||  _  ||    _]    |" \
                          "  _  ||  |  ||  |  ||_|  |_|\n  |  |  |  |  ||   [" \
                          "_     |  |  ||  :  ||  |  |  |  |\n  |  |  |  |  |" \
                          "|     |    |  |  ||     ||  |  |  |  |\n  |__|  |" \
                          "__|__||_____|    |__|__| \__,_||__|__|  |__|     " \
                          "                                                   "
        self._intro_title = "                 Cover Letter Builder           " \
                            "       "
        # Initializing prints the intro art
        print('\n')
        print(self._intro_art)
        print(self._tc.colorize(_content=self._intro_title))
        print('\n')
        pass

    def identify_job(self):
        # Ask for name of company
        self._company = input(self._tc.colorize(
            _content=" What is the name of the company?"))

        # Ask for job title
        self._title = input(self._tc.colorize(
            _content=" What is the job title?"))

        def _boolean_question(option):
            while True:
                _ans = input(self._tc.colorize(_content=option["question"]))
                if _ans == '' \
                        or not _ans[0].lower() in ['y', 'n']:
                    print('Please answer with yes or no!')
                else:
                    break
            if _ans[0].lower() == 'y':
                option["answer"] = True
                pass

        _boolean_question(self._type_uxd)
        _boolean_question(self._type_dev)
        _boolean_question(self._type_des)

        self.build_output()

    def build_output(self):
        _content = []
        with open("intro.txt", "r", encoding="utf-8") as input_file:
            _copy = input_file.read()
            _copy = _copy.replace('{{ company }}', self._company)
            _copy = _copy.replace('{{ position }}', self._title)
            _content.append(_copy)

        if self._type_uxd['answer'] is True:
            with open("uxd.txt", "r", encoding="utf-8") as input_file:
                _content.append(input_file.read())

        if self._type_dev['answer'] is True:
            with open("dev.txt", "r", encoding="utf-8") as input_file:
                _content.append(input_file.read())

        if self._type_des['answer'] is True:
            with open("des.txt", "r", encoding="utf-8") as input_file:
                _content.append(input_file.read())

        with open("closing.txt", "r", encoding="utf-8") as input_file:
            _content.append(input_file.read())

        print("\n".join(_content))
        # ctypes.windll.user32.MessageBoxW(0, "\n".join(_content),
        #                                  "Cover Letter", 0)
        pass


cover = BuildCoverLetter()
cover.identify_job()
