class Time:
    def _init_(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def _str_(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def display_time(self):
        print(f"Time: {self}")

    def add_seconds(self, seconds):
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second + seconds
        self.hour = (total_seconds // 3600) % 24
        self.minute = (total_seconds % 3600) // 60
        self.second = total_seconds % 60

# Creating two Time objects
time1 = Time(10, 30, 15)
time1.display_time()

# Function to add 5000 seconds and display updated time
def add_5000_seconds(time_obj):
    time_obj.add_seconds(5000)
    time_obj.display_time()

add_5000_seconds(time1)