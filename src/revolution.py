import matplotlib.pyplot as plt
import random

class revolution():
    def __init__(self,n,t_percent,w_percent):
        '''
        :param n: Total number of players
        :param t_percent: Percentage of players needed for the revolt to succeed
        :param w_percent: Percentage of players willing to revolt
        '''
        self.n = n
        self.t =( (t_percent/100) * n)
        self.t_percent = t_percent
        self.frequency_deviation = 0
        self.force_revolution_possibility = True
        self.total_willing_individuals = ((w_percent / 100) * n)
        self.type_set = []

    def set_force_revolution_possibility(self,mandatory):
        '''

        :param mandatory: True if W (no.of willing individuals) should always be greater than t (minimum threshold of people needed for revolt to suceed)
        :return:
        '''
        self.force_revolution_possibility = mandatory

    def set_frequency_deviation(self,frequency):
        '''

        :param frequency: if n=10 and frequency = 2 , then for every 10 individuals willing, 2 ppl deviate
        :return:
        '''
        self.frequency_deviation = frequency


    def game_Setup(self):
        '''

        :return:
        '''
        if self.force_revolution_possibility:
            while True:
                self.type_set = []
                willing_count = 0
                for x in range(0, self.n):
                    type = random.sample(set(['w', 'x']), 1)
                    self.type_set.append(type[0])
                    if type[0] == 'w':
                        willing_count = willing_count + 1
                if (willing_count >= self.total_willing_individuals):
                    break
        else:
            for x in range(0, self.n):
                type = random.sample(set(['w', 'x']), 1)
                self.type_set.append(type[0])
                if type[0] == 'w':
                    willing_count = willing_count + 1
        print(self.type_set)
        print(willing_count)


    def getActions(self):
        self.actions = []
        revolted = 0
        to_revolt = self.total_willing_individuals
        forced_change = 0
        willing_indv_count = 0
        for i in range(0, self.n):

            if (self.type_set[i] == 'w'):
                willing_indv_count = willing_indv_count + 1
                if (willing_indv_count == self.frequency_deviation):
                    willing_indv_count = 0
                    self.actions.append('s')
                if self.t <= (revolted + to_revolt - 1):
                    self.actions.append('r')
                    revolted = revolted + 1
                    to_revolt = to_revolt - 1
                else:
                    self.actions.append('s')

            else:
                self.actions.append('s')

    def is_revolution_possible(self):
        if self.total_willing_individuals > self.t:
            print("Revolution possible")
        else:
            print("Revolution not possible")
            exit()


    def simulate(self):
        self.no_of_willing_individuals_revolted = 0
        self.no_of_willing_individuals_not_revolted = 0
        for i in range(0, self.n):
            if (self.actions[i] == 'r' and self.type_set[i] == 'w'):
                self.no_of_willing_individuals_revolted = self.no_of_willing_individuals_revolted + 1
            elif (self.actions[i] == 's' and self.type_set[i] == 'w'):
                self.no_of_willing_individuals_not_revolted = self.no_of_willing_individuals_not_revolted + 1
        x1 = []
        y1 = []

        for x in range(0, self.n):
            x1.append(x)
            count = 0
            for y in range(0, x):
                if self.actions[y] == 'r':
                    count = count + 1
            y1.append(count)
        plt.plot(x1, y1)
        print("no_of_willing_individuals_not_revolted {}".format(self.no_of_willing_individuals_not_revolted))
        print("no_of_willing_individuals_revolted {}".format(self.no_of_willing_individuals_revolted))


        # threshold line
        x2 = []
        y2 = []
        for x in range(0, self.n):
            x2.append(x)
            y2.append((self.t_percent / 100) * x)
        plt.plot(x2, y2, label="threshold")

        plt.xlabel('Individuals')
        plt.ylabel('Revolting individuals')

        plt.title('Success rate of revolution')
        plt.show()

    def get_suceess_rate(self):
        success_rate = (self.no_of_willing_individuals_revolted / self.t) * 100
        print("Success Rate {}".format(self.success_rate))
        return success_rate

    def run(self):

        self.game_Setup()
        self.getActions()
        self.simulate()
        self.get_suceess_rate()


r = revolution(1000,49,50)
r.set_frequency_deviation(5)
r.run()





