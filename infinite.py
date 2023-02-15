
import time
from colorama import init, Fore, Back, Style
import datetime
# essential for Windows environment
init()
# all available foreground colors
FORES = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
# all available background colors
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
# brightness values
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]

anniversary = datetime.date(2023, 2, 14)
def print_with_color(p,s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function 
    but with colors and brightness"""
    print(f"{color}{p}{s}{Style.RESET_ALL}", **kwargs)

# printing all available foreground colors with different brightness

while True:
    for fore in FORES:
            print_with_color(anniversary.strftime("%d-%m-%Y:"),"anh yêu em vô hạn!", color=fore)
            time.sleep(0.01)
            anniversary += datetime.timedelta(days=1)
