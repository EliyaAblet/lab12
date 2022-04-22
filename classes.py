class Television:
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        """
        - Create a private variable to store the TV channel. It should be set to the minimum TV channel by default.
        - Create a private variable to store the TV volume. It should be set to the minimum TV volume by default.
        - Create a private variable to store the TV status. The TV should start when it is off.
        """
        self.__tv_channel = Television.MIN_CHANNEL
        self.__tv_volume = Television.MIN_VOLUME
        self.__tv_status = False

    def power(self) -> None:
       """
       This method should be used to turn the TV on/off.
       :return: None
       """
       if not self.__tv_status:
            self.__tv_status = True
       else:
            self.__tv_status = False
        # pass

    def channel_up(self) -> None:
        """
        - This method should be used to adjust the TV channel by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_CHANNEL, it should take the TV channel back to the MIN_CHANNEL.
        """
        if self.__tv_status == True:
            if self.__tv_channel + 1 > Television.MAX_CHANNEL:
                self.__tv_channel = Television.MIN_CHANNEL
            else:
                self.__tv_channel += 1

        # pass

    def channel_down(self) -> None:
        """
        - This method should be used to adjust the TV channel by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_CHANNEL, it should take the TV channel back to the MAX_CHANNEL.
        """
        if self.__tv_status == True:
            if self.__tv_channel - 1 < Television.MIN_CHANNEL:
                self.__tv_channel = Television.MAX_CHANNEL
            else:
                self.__tv_channel -= 1

            # pass

    def volume_up(self) -> None:
        """
        - This method should be used to adjust the TV volume by incrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MAX_VOLUME, the volume should not be adjusted.
        """
        if self.__tv_status == True:
            if self.__tv_volume + 1 > Television.MAX_VOLUME:
                self.__tv_volume = self.__tv_volume + 0
            else:
                self.__tv_volume = self.__tv_volume + 1

        # pass

    def volume_down(self) -> None:
        """
        - This method should be used to adjust the TV volume by decrementing its value.
        - It should only work for a TV that is on.
        - If the method is called when one is on the MIN_VOLUME, the volume should not be adjusted.
        """
        if self.__tv_status == True:
            if self.__tv_volume - 1 < Television.MAX_VOLUME:
                self.__tv_volume = self.__tv_volume + 0
            else:
                self.__tv_volume = self.__tv_volume - 1
        # pass

    def __str__(self) -> str:
        """
        - This method should be used to return the TV status using the format shown in the comments of main.py
        """
        # TV status: Is on = False, Channel = 0, Volume = 0
        return (f"TV Status: Is on = {self.__tv_status}, Channel = {self.__tv_channel}, Volume = {self.__tv_volume}")

 """
        - This method should be used to turn the TV on/off.
        - If called on a TV object that is off, the TV object should be turned on.
        - If called on a TV object that is on, the TV object should be turned off.
 """