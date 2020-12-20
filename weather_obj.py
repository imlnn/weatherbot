ABSOLUTE_ZERO = -273.15


class Weather:
    def __init__(self, date, place, temperature, status, humidity, wind_speed):
        self.date = date
        self.place = place
        self.temperature = temperature
        if temperature < -150:
            self.temperature -= ABSOLUTE_ZERO
        self.status = status
        self.humidity = humidity
        self.wind_speed = wind_speed

    def to_string(self):
        return str("Weather for " + self.date
                   + "\nPlace: " + self.place
                   + "\nTemperature: " + str("%.2f" % self.temperature)
                   + "\n" + str(self.status)
                   + "\nHumidity: " + str(self.humidity)
                   + "\nWind speed: " + str(self.wind_speed))
