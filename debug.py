import time


class Debug:

    Default      = "\033[39m"
    Black        = "\033[30m"
    Red          = "\033[31m"
    Green        = "\033[32m"
    Yellow       = "\033[33m"
    Blue         = "\033[34m"
    Magenta      = "\033[35m"
    Cyan         = "\033[36m"
    LightGray    = "\033[37m"
    DarkGray     = "\033[90m"
    LightRed     = "\033[91m"
    LightGreen   = "\033[92m"
    LightYellow  = "\033[93m"
    LightBlue    = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan    = "\033[96m"
    White        = "\033[97m"

    BackgroundDefault      = "\033[49m"
    BackgroundBlack        = "\033[40m"
    BackgroundRed          = "\033[41m"
    BackgroundGreen        = "\033[42m"
    BackgroundYellow       = "\033[43m"
    BackgroundBlue         = "\033[44m"
    BackgroundMagenta      = "\033[45m"
    BackgroundCyan         = "\033[46m"
    BackgroundLightGray    = "\033[47m"
    BackgroundDarkGray     = "\033[100m"
    BackgroundLightRed     = "\033[101m"
    BackgroundLightGreen   = "\033[102m"
    BackgroundLightYellow  = "\033[103m"
    BackgroundLightBlue    = "\033[104m"
    BackgroundLightMagenta = "\033[105m"
    BackgroundLightCyan    = "\033[106m"
    BackgroundWhite        = "\033[107m"

    ENDC = '\033[0m'
    BOLD = '\033[1m'

    def debug(self,content):
        print(f"{self.LightMagenta}[{time.ctime()}][DEBUG]:{content}{self.ENDC}")

    def data(self,content):
        print(f"{self.Green}[{time.ctime()}][DATA]:{content}{self.ENDC}")

    def info(self,content):
        print(f"{self.LightCyan}[{time.ctime()}][INFO]:{content}{self.ENDC}")

    def warning(self,content):
        print(f"{self.LightYellow}[{time.ctime()}][WARNING]:{content}{self.ENDC}")

    def error(self,content):
        print(f"{self.Red}[{time.ctime()}][ERROR]:{content}{self.ENDC}")

    def fatal(self,content):
        print(f"{self.White}{self.BOLD}{self.BackgroundRed}[{time.ctime()}][FATAL_ERROR]:{content}{self.ENDC}")