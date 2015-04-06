import time, win32gui
import win32com.client as comclt

PRIEST_MODE = True

HP_OFFSET_RATIO_X = 0.85375
HP_OFFSET_RATIO_Y = 0.44

MP_OFFSET_RATIO_X = 0.85375
MP_OFFSET_RATIO_Y = 0.48

EMPTY_R = 84
EMPTY_G = 84
EMPTY_B = 84
EPSILON = 10

HP_POTION_KEYS = "f"
MP_POTION_KEYS = "v"
NEXUS_TP_KEYS = "r"
PRIEST_HEAL_KEYS = " "

wsh = comclt.Dispatch("WScript.Shell")
rotmg_hwnd = None

def io(tag, message, func):
  timestr = time.strftime("%H:%M:%S", time.localtime())
  print("(%s) [%s] %s" % (timestr, tag, message))

def say(tag, message): io(tag, message, print)
def ask(tag, message): io(tag, message, input)

def find_rotmg(hwnd, _):
  global rotmg_hwnd
  if "realm of the mad god" in win32gui.GetWindowText(hwnd).lower():
    rotmg_hwnd = hwnd

def get_pixel_rgb(hdc, x, y):
  color = win32gui.GetPixel(hdc, x, y)
  return (color & 0xff), ((color >> 8) & 0xff), ((color >> 16) & 0xff)

def is_empty_pixel(offset_ratio_x, offset_ratio_y):
  rect = win32gui.GetClientRect(rotmg_hwnd)
  hdc = win32gui.GetDC(rotmg_hwnd)
  r, g, b = get_pixel_rgb(hdc, int(rect[2] * offset_ratio_x), int(rect[3] * offset_ratio_y))
  return abs(r - EMPTY_R) < EPSILON and abs(g - EMPTY_G) < EPSILON and abs(b - EMPTY_B) < EPSILON

def low_hp(): return is_empty_pixel(HP_OFFSET_RATIO_X, HP_OFFSET_RATIO_Y)
def low_mp(): return is_empty_pixel(MP_OFFSET_RATIO_X, MP_OFFSET_RATIO_Y)

say("init/info", "Seeking for game window...")

while True:
  win32gui.EnumWindows(find_rotmg, None)
  if rotmg_hwnd is None:
    ask("init/failure", "Game window not found! Please launch the game and press enter...")
  else:
    say("init/success", "Game window found: %s" % rotmg_hwnd)
    break

while True:
  if low_hp():
    if PRIEST_MODE:
      enough_mp = True
      say("game/event", "Low HP! Trying to cast heal...")
      if low_mp():
        say("game/event", "Low MP! Trying to drink potion...")
        wsh.SendKeys(MP_POTION_KEYS)
        time.sleep(0.5)
        if low_mp():
          enough_mp = False
          say("game/failure", "There are no mana potions!")
        else:
          say("game/success", "Successfully restored MP!")
      if enough_mp:
        wsh.SendKeys(PRIEST_HEAL_KEYS)
        time.sleep(0.5)
        say("game/success", "Successfully healed!")
        continue
    say("game/event", "Low HP! Trying to drink potion...")
    wsh.SendKeys(HP_POTION_KEYS)
    time.sleep(0.5)
    if low_hp():
      say("game/failure", "Nothing works! HP is still low! Teleporting to Nexus...")
      wsh.SendKeys(NEXUS_TP_KEYS)
      time.sleep(5)
    else:
      say("game/success", "Successfully healed!")
  time.sleep(0.5)