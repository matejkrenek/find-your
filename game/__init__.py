from game.player import Player
from game.map import Map
from game.helpers import writer

import time
import os
import ctypes
import msvcrt
import subprocess
import shutil
from ctypes import wintypes

class Game:
    def __init__(self, name, data = {}, player = None, map = None):
        self.name = name
        self.data = data
        self.map(map)
        self.player(player)

        self.init()

    def map(self, map = None):
        if not map:
            return

        if isinstance(map, Map):
            self._map = map
            self._map.origin._game = self
        else:
            print("map parameter has to be type of game.map.Map")

    def player(self, player = None):
        if not player:
            return
        if isinstance(player, Player):
            self._player = player
        else:
            print("player parameter has to be type of game.player.Player")

    def select_direction(self):
        for child in self._player.position.children:
            if child.direction:
                print(f"[{child.direction['name']}] můžeš jít {child.direction['4']}".center(shutil.get_terminal_size().columns))
        
        prefix = ":)".ljust(int(shutil.get_terminal_size().columns / 2) - 4)
        choice = input(prefix)
        
        if self._player.position.is_valid_direction(choice):
            room = self._player.position.find_room(choice)
            self._player.move(room)
        else:
            print("neexistuje".center(shutil.get_terminal_size().columns))
            self.select_direction()


    def intro(self, screenplay = None):
        if not screenplay:
            screenplay = self.data["screenplay"]
            

        if(isinstance(screenplay, list)):
            for phrase in screenplay:
                formated_phrase = phrase.format(player = self._player.name).center(shutil.get_terminal_size().columns)

                writer(formated_phrase, 0.05)
                if phrase in self.data["input"]:
                    eval(self.data["input"][phrase])
        else:
            print("screenplay parameter has to be type of list")

    def start(self):
        self.intro()
        self._player.move(self._map.origin)

    def stop(self):
        pass

    def fullscreen(self):
        kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        user32 = ctypes.WinDLL('user32', use_last_error=True)

        SW_MAXIMIZE = 3

        kernel32.GetConsoleWindow.restype = wintypes.HWND
        kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
        kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
        user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)

        def maximize_console(lines=None):
            fd = os.open('CONOUT$', os.O_RDWR)
            try:
                hCon = msvcrt.get_osfhandle(fd)
                max_size = kernel32.GetLargestConsoleWindowSize(hCon)
                if max_size.X == 0 and max_size.Y == 0:
                    raise ctypes.WinError(ctypes.get_last_error())
            finally:
                os.close(fd)
            cols = max_size.X
            hWnd = kernel32.GetConsoleWindow()
            if cols and hWnd:
                if lines is None:
                    lines = max_size.Y
                else:
                    lines = max(min(lines, 9999), max_size.Y)
                subprocess.check_call('mode.com con cols={} lines={}'.format(
                                        cols, lines))
                user32.ShowWindow(hWnd, SW_MAXIMIZE)

        maximize_console()

    def font(self):
        LF_FACESIZE = 32
        STD_OUTPUT_HANDLE = -11

        class COORD(ctypes.Structure):
            _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

        class CONSOLE_FONT_INFOEX(ctypes.Structure):
            _fields_ = [("cbSize", ctypes.c_ulong),
                        ("nFont", ctypes.c_ulong),
                        ("dwFontSize", COORD),
                        ("FontFamily", ctypes.c_uint),
                        ("FontWeight", ctypes.c_uint),
                        ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

        font = CONSOLE_FONT_INFOEX()
        font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
        font.nFont = 12
        font.dwFontSize.X = 11
        font.dwFontSize.Y = 18
        font.FontFamily = 54
        font.FontWeight = 400
        font.FaceName = "Lucida Console"

        handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        ctypes.windll.kernel32.SetCurrentConsoleFontEx(
                handle, ctypes.c_long(False), ctypes.pointer(font))

    def init(self):
        self.font()
        self.fullscreen()
        time.sleep(0.5)
        os.system("cls")
