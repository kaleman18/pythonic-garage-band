
class Band:

    instances = []

    def __init__(self, name='unknown', people=None):
        self.name = name
        self.members = people
        self.instances.append(self)
    def __str__(self):
        pass
    
    def __repr__(self):
        pass

    def play_solos(self):
        return [member.play_solo() for member in self.members]
    
    @classmethod
    def to_list(cls):
        return cls.instances

class Musician:
    def play_solos(cls):
        pass

class Guitarist(Musician):
    def __init__(self, name='unknown'):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play guitar'
    
    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'
    
    def get_instrument(cls):
        return 'guitar'
    
    def play_solo(cls):
        return "face melting guitar solo"

class Bassist(Musician):
    def __init__(self, name='unknown'):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play bass'
    
    def __repr__(self):
        return f'Bassist instance. Name = {self.name}'
    
    def get_instrument(cls):
        return 'bass'
    
    def play_solo(cls):
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name='unknown'):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play drums'
    
    def __repr__(self):
        return f'Drummer instance. Name = {self.name}'
    
    def get_instrument(cls):
        return 'drums'
    
    def play_solo(cls):
        return "rattle boom crash"
