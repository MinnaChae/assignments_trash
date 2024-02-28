from Monster import Monster, Skeleton, Ogre, Gremlin
from Hero import Hero, Thief, Warrior, Priestess


def create_characters():
    s = Skeleton('s john')
    o = Ogre('o jacob')
    g = Gremlin('g jingle')
    t = Thief()
    w = Warrior()
    p = Priestess()
    # t.attack(s)
    # p.attack(o)
    g.special_skill(t)
    # attack_opponent_based_on_attack_speed(s, t)

# def attack_opponent_based_on_attack_speed(self, opponent):

    #
    # if self.attack_speed >= opponent.attack_speed:  # self is the hero and opponent is the monster
    #     a_attack_speed = self.attack_speed / self.attack_speed
    #     b_attack_speed = opponent.attack_speed / self.attack_speed
    # else:
    #     a_attack_speed = self.attack_speed / opponent.attack_speed
    #     b_attack_speed = opponent.attack_speed / opponent.attack_speed
    # while self.hit_points > 0 and opponent.hit_points > 0:
    #     a_dps = a_attack_speed * self.calculate_damage()  # a_dps means a's damage per second
    #     b_dps = b_attack_speed * opponent.calculate_damage()  # b_dps means b's damage per second
    #     self.get_damage(b_dps)
    #     opponent.get_damage(a_dps)

create_characters()