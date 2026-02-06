class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds
        self.EARTH_YEARS_IN_SECONDS = 31557600
        self.orbital_period = {
        'Mercury':0.2408467,
        'Venus':0.61519726,
        'Earth':1.0,
        'Mars':1.8808158,
        'Jupiter':11.862615,
        'Saturn':29.447498,
        'Uranus':84.016846,
        'Neptune':164.79132
        }
        
    def on_mercury(self):
        return round(self.seconds/(self.orbital_period['Mercury']*self.EARTH_YEARS_IN_SECONDS),2)
    def on_venus(self):
        return round(self.seconds/(self.orbital_period['Venus']*self.EARTH_YEARS_IN_SECONDS),2)
    def on_earth(self):
        return round(self.seconds/(self.orbital_period['Earth']*self.EARTH_YEARS_IN_SECONDS),2)
    def on_mars(self):
        return round(self.seconds/(self.orbital_period['Mars']*self.EARTH_YEARS_IN_SECONDS),2)
    def on_jupiter(self):
        return round(self.seconds/(self.orbital_period['Jupiter']*self.EARTH_YEARS_IN_SECONDS),2)
    def on_saturn(self):
        return round(self.seconds/(self.orbital_period['Saturn']*self.EARTH_YEARS_IN_SECONDS),2)
    def on_uranus(self):
        return round(self.seconds/(self.orbital_period['Uranus']*self.EARTH_YEARS_IN_SECONDS),2)
    def on_neptune(self):
        return round(self.seconds/(self.orbital_period['Neptune']*self.EARTH_YEARS_IN_SECONDS),2)
