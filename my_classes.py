class RandomEntityParagraph:
    def __init__(self, number: int, textures: str, weights="", biomes=[], heights="", name="", professions=[],
                 colors=[], baby=False, health="", moon_phase="", day_time="", weather=[], sizes=""):
        self.number = number
        self.textures = textures
        self.weights = weights
        self.biomes = biomes
        self.heights = heights
        self.name = name
        self.professions = professions
        self.colors = colors
        self.baby = baby
        self.health = health
        self.moon_phase = moon_phase
        self.day_time = day_time
        self.weather = weather
        self.sizes = sizes

    def __str__(self):
        s = ""
        n = str(self.number)
        if self.textures:
            s += f"textures.{n}=" + self.textures + "\n"
            if self.weights:
                s += f"weights.{n}=" + self.weights + "\n"
            if self.biomes:
                s += f"biomes.{n}=" + " ".join(self.biomes) + "\n"
            if self.heights:
                s += f"heights.{n}=" + self.heights + "\n"
            if self.name:
                s += f"name.{n}=" + self.name + "\n"
            if self.professions:
                s += f"professions.{n}=" + " ".join(self.professions) + "\n"
            if self.colors:
                s += f"colors.{n}=" + " ".join(self.colors) + "\n"
            if self.baby:
                s += f"baby.{n}=" + str(self.baby).lower() + "\n"
            if self.health:
                s += f"health.{n}=" + self.health + "\n"
            if self.moon_phase:
                s += f"moonPhase.{n}=" + self.moon_phase + "\n"
            if self.day_time:
                s += f"dayTime.{n}=" + self.day_time + "\n"
            if self.weather:
                s += f"weather.{n}=" + " ".join(self.weather) + "\n"
            if self.sizes:
                s += f"sizes.{n}=" + self.sizes
            return s
        else:
            return "empty textures paragraph"

    def __bool__(self):
        return bool(self.textures)

    def textures_str(self):
        return " ".join(self.textures)

    def __repr__(self):
        return str(self.number)