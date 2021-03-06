import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

class SpotifyController:
  def __init__(self):
    self.buttonsX = 95
    self.buttonsY = 1060
    self.buttonWeight = 30

    self.songX = 95
    self.songY = 950

    self.titleX = 135
    self.titleY = 1005

    self.addToX = 210
    self.addToY = 850

    self.starX = 450
    self.starY = 425

    self.progress0X = 355
    self.progressY = 1060
    self.progress100X = 1780

    self.volume0X = 190
    self.volumeY = 1060
    self.volume100X = 271

    self.radioX = 200
    self.radioY = 895

  def star(self):
    pyautogui.moveTo(self.titleX, self.titleY)
    pyautogui.click(button="right")
    time.sleep(1)

    pyautogui.moveTo(self.addToX, self.addToY)
    pyautogui.click()
    time.sleep(1)

    pyautogui.moveTo(self.starX, self.starY)
    pyautogui.click()
    time.sleep(1)

    self.song()

  def song(self):
    pyautogui.moveTo(self.songX, self.songY)
    pyautogui.click()

  def play(self):
    pyautogui.moveTo(self.buttonsX + self.buttonWeight, self.buttonsY)
    pyautogui.click()

  def pause(self):
    self.play()

  def next(self):
    pyautogui.moveTo(self.buttonsX + 2 * self.buttonWeight, self.buttonsY)
    pyautogui.click()

  def back(self):
    pyautogui.moveTo(self.buttonsX, self.buttonsY)
    pyautogui.click()

  def progress(self, value):
    self.jump(value, self.progress0X, self.progress100X, self.progressY)

  def volume(self, value):
    self.jump(value, self.volume0X, self.volume100X, self.volumeY)

  def jump(self, value, progress0X, progress100X, progressY):
    diff = (progress100X - progress0X) / 10
    progressX = diff * value + progress0X
    pyautogui.moveTo(progressX, progressY)
    pyautogui.click()

  def radio(self):
    pyautogui.moveTo(self.titleX, self.titleY)
    pyautogui.click(button="right")
    time.sleep(1)

    pyautogui.moveTo(self.radioX, self.radioY)
    pyautogui.click()
    time.sleep(1)
    
    self.song()

