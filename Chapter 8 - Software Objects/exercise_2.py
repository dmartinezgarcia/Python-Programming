# Exercise 2
#
# Improve the Trivia Challenge game so that it maintains a high scores list in a file. The program should record the
# player's name and score if the player makes the list. Store the high scores using a pickled object.
#

class Television(object):
    MAX_VOLUME = 10
    MIN_VOLUME = 1
    MAX_CHANNEL = 6
    MIN_CHANNEL = 1

    def __init__(self):
        self.__status = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME

    def __str__(self):
        string = "Status: "
        if self.__status:
            string += "Turned On.\n"
            string += "Channel: " + str(self.__channel) + "\n"
            string += "Volume: " + str(self.__volume) + "\n"
        else:
            string += "Turned Off.\n"
        return string

    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, new_channel):
        if Television.MAX_CHANNEL >= new_channel >= Television.MIN_CHANNEL and self.__status:
            self.__channel = new_channel

    def volume_up(self):
        if self.__volume < Television.MAX_VOLUME and self.__status:
            self.__volume += 1

    def volume_down(self):
        if self.__volume > Television.MIN_VOLUME and self.__status:
            self.__volume -= 1

    def status(self, mode):
        self.__status = mode
