from definations import  *

def will_revolt_happen(n,w,t,commun_type):
    if commun_type == communicationType.mass_media:
        value = (n/(n-w+1) + 1)
        if t < value:
            print("Revolution suceeds")
        else:
            print("Revolution may fail")

person_4 = mass_media_information_set(4,type.willing,0,2)
person_3 = mass_media_information_set(3, type.willing, 0, 1)
person_2 = mass_media_information_set(2, type.willing, 0, 0)
person_1 = mass_media_information_set(1, type.unwilling, 0, 0)


def __init__(self, i, t_i, p_i, w_i):
    self.i = i
    self.t_i = t_i
    self.p_i = p_i
    self.w_i = w_i

def prob_each_person_revolting(n,w,t,commun_type,information_set):
    prob = {}
    for person in information_set:
        if person.t_i == type.willing:
            if person.p_i == person.w_i and (person.i != 1): #all the willing people before him have revolted
                prob[person.i] = 1.0
            #else:
            #    #atleast t-willing_ppl_reqd_after_hime willing people are after him
            #    willing_people_reqd = w - person.w_i - 1
            #    if(n-i > )
            #    prob[person.i] =


        else:
            prob[person.i] = 0.0 #unwilling joining the revolt








#will_revolt_happen(10,7,5,communicationType.mass_media)
#will_revolt_happen(4,3,3,communicationType.mass_media)
prob_each_person_revolting(4,3,3,communicationType.mass_media)