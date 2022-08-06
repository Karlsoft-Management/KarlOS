# Created by Karlsoft

"""

"""
import os



__ALL__ = [ 'colored' ]


ATTRIBUTES = dict(
        list(zip([
            'bold',
            'dark',
            '',
            'underline',
            'blink',
            '',
            'reverse',
            'concealed'
            ],
            list(range(1, 9))
            ))
        )
del ATTRIBUTES['']


HIGHLIGHTS = dict(
        list(zip([
            'on_grey',
            'on_red',
            'on_green',
            'on_yellow',
            'on_blue',
            'on_magenta',
            'on_cyan',
            'on_white'
            ],
            list(range(40, 48))
            ))
        )


COLORS = dict(
        list(zip([
            'grey',
            'red',
            'green',
            'yellow',
            'blue',
            'magenta',
            'cyan',
            'white',
            ],
            list(range(30, 38))
            ))
        )


RESET = '\033[0m'


def colored(text, color=None, on_color=None, attrs=None):
    
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        fmt_str = '\033[%dm%s'
        if color is not None:
            text = fmt_str % (COLORS[color], text)

        if on_color is not None:
            text = fmt_str % (HIGHLIGHTS[on_color], text)

        if attrs is not None:
            for attr in attrs:
                text = fmt_str % (ATTRIBUTES[attr], text)

        text += RESET
    return text



def main():
    try:
        print()
        
        
    except:
        print((colored('Please install the library: "Time"', 
        on_color='on_red', attrs=['blink'])))
def paint(text,colour):
    
    
    print((colored(text, colour)))
     
    
    
def clear():
    clearConsole = lambda: print('\n' * 150)

    clearConsole()
def graph(pos1,size1,size2,font1,font2): 
    pos2 = 0
    
    
    try:
        for i in range(size2):
            print()
            for c in range(size1):
                if pos1 == pos2:
                    print(font2,end="")
                else:
                    print(font1,end="")
                pos2 += 1
                
            
        print()
    except:
        print("lol you suck at coding")


if __name__ == "__main__":
    main()
