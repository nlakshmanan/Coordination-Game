import enum

class communicationType(enum.Enum):
    no_media = 1
    mass_media = 2
    social_media = 3

class type(enum.Enum):
    willing = 1 #willing
    unwilling = 2 #unwilling

class mass_media_information_set:
    def __init__(self,i,t_i,p_i,w_i):
        self.i = i
        self.t_i = t_i
        self.p_i = p_i
        self.w_i = w_i