__author__ = 'anna'

class Television(object):
    """A television simulator"""

    def __init__(self, channel=None, volume=0, max_volume=30, min_volume=0):
        self.channel = channel
        self.volume = volume
        self.max_volume = max_volume
        self.min_volume = min_volume
        print("I am a new channel. Now I am set up for 0 channel and volume is 0.")

    def change_channel(self,channel=None):
        print("var channel:", channel)
        input_=input("Please enter a channel number:")
        while channel == None or not isinstance(channel, int):
            try:
                channel = int(input_)
                print("var channel:",channel)
                if 0>= channel or channel >= 100:
                    input_ = input("The channel number can be only an integer between 0 and 99.\nEnter the channel number:")
                    channel = None
                else:
                    self.channel = channel
                    print("You successfully changed the channel to %s." % self.channel)
            except:
                input_ = input("You need to enter an integer, not a string or float:")

    def raise_or_lower(self):
        choice = None
        print("""
        r - raise the volume
        l - lower the volume
        """)
        choice = input("Choice:")
        while choice != "r" and choice != "l":
            choice = input("Sorry, the only available choices are: r or l. Enter your choice:")
        print(choice)
        return choice

    def raise_volume(self,volume = None):
        total_volume = int()
        print("self.volume:", self.volume)
        if self.volume == self.max_volume:
            print("Sorry, the volume is already at the maximum, 30, you cannot raise it.")
        else:
            input_ = input("Please enter the number of points to raise your volume on:")
            while volume is None or not isinstance(volume, int):
                    try:
                        volume = int(input_)
                        total_volume = self.volume + volume
                        if total_volume > self.max_volume:
                            input_ = input("It is too loud: the volume exceeds 30 point.\nEnter less points:")
                            volume = None
                            total_volume = int()
                        else:
                            self.volume = total_volume
                            print("You successfully raised volume on %d points. The volume now is %d points." % (volume, self.volume))
                    except:
                        input_=input("Sorry, the only valid input is integer.Enter the number of points to raise on:")

    def lower_volume(self, volume = None):
        total_volume = int()
        print("self.volume", self.volume)
        if self.volume <= self.min_volume:
            print("Sorry, the volume is at the minimum, 0 you cannot lower it.")
        else:
            input_=input("Please enter the number of points to lower your volume on:")
            while volume is None or not isinstance(volume, int):
                try:
                    volume = int(input_)
                    total_volume=self.volume-volume
                    if total_volume < self.min_volume:
                        input_= input("It is too quiet: the volume will be below 0.\nEnter less points:")
                        volume = None
                        total_volume = int()
                    else:
                        self.volume = total_volume
                        print("You successfully lowered the volume on %d points. The volume now is %d points." % (volume, self.volume))
                except:
                    input_=input("Sorry, you can only enter an integer. Enter the number of points to lower on:")

def main():
    telev = Television()

    choice = None
    while choice != "0":
        print("""
        Television game:

        0 - Quit
        1 - Change channel
        2 - Raise or lower volume
        """)

        choice = input("Choice:")
        if choice == "0":
            print("Good-bye!")

        elif choice == "1":
            telev.change_channel()

        elif choice == "2":
            next_choice = telev.raise_or_lower()
            if next_choice == "r":
                telev.raise_volume()
            if next_choice == "l":
                telev.lower_volume()

        else:
            print("\nSorry, but %r is not a valid choice." % choice)

main()


