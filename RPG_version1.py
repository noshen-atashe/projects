#-------------------------------------------------------

#RPG (party vs enemies)
 
class Character:
    def __init__(self, name, hp, xp, xpGained, level, attack, defense, magic=0):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.xp = xp
        self.xpGained = xpGained
        self.level = level
        self.attackpower = attack
        self.defensepower = defense
        self.magic = magic
     
    def isDead(self):
        if self.hp <= 0:
           return True
        return False

    def attack(self, otherCharacter):
        if self.isDead():
            print(self.name, 'cannot attack because he/she is dead.')
        else:
            if self.attackpower>otherCharacter.defensepower:
                damage = self.attackpower - otherCharacter.defensepower
                otherCharacter.hp -= damage
            else:
                damage = 0
            
            print(self.name, 'does', damage, 
                  'points of damage to', otherCharacter.name)
            if otherCharacter.hp <= 0:
                otherCharacter.hp = 0
                print(otherCharacter.name, 'has been defeated.')
                print(self.name, 'gained', otherCharacter.xpGained, 'XP.')
                self.gainXP(otherCharacter)
            

    def heal(self, party):
        if self.isDead():
            print(self.name, 'cannot heal because he/she is dead.')
        else:
            for partyMember in party:
                if not partyMember.isDead():
                    healHP = self.magic
                    partyMember.hp += healHP                    
                    if partyMember.hp > partyMember.maxhp:
                        healHP= partyMember.maxhp - (partyMember.hp - healHP)
                        partyMember.hp = partyMember.maxhp                        
                        
                    print(self.name, 'heals', healHP, 'hp for',
                            partyMember.name)

    def gainXP(self, otherCharacter):
        self.xp += otherCharacter.xpGained
        self.levelUP()
    
    def levelUP(self):
        #levels: 
        levels           = [2,  3,  4,  5,  6]
        levelMinXP       = [100,200,300,400,500]
        levelAttackGain  = [5.0,2.5,2.5,2.5,2.5]
        levelDefenseGain = [2.5,2.5,2.5,2.5,2.5]
        levelMagicGain   = [2.0,1.0,2.0,2.0,2.0]
        newLevel = False 
        #update stats for new level 
        for l in range (5):
            if self.xp>=levelMinXP[l] and levels[l]>self.level:
                newLevel=True
                self.level = levels[l]
                self.attackpower+= levelAttackGain[l]
                self.defensepower+=levelDefenseGain[l]
                self.magic+=levelMagicGain[l]
        
        if newLevel:
            print(self.name, 'reached level',self.level)      
     
        
    def __str__(self):
        if self.isDead():
            return self.name + ' [DEAD]'
        else:
            str1 = self.name + ' ('+ 'HP:'+str(self.hp)
            str2 = ', XP:'+str(self.xp)+', Level:'+str(self.level)
            str3 = ', Attack:'+str(self.attackpower)+', Defense:'
            str4 = str(self.defensepower)+')' 
            return str1+str2+str3+str4                     
#end of character class 


#characters: 
krogg = Character('Krogg', 180, 0, 0, 1, 20, 20)
glinda = Character('Glinda', 120, 0, 0, 1, 5, 20, 5)
geoffrey = Character('Geoffrey', 150, 0, 0, 1, 15, 15)
party = [krogg, glinda, geoffrey]
enemy1 = Character('Spider 1', 50, 0, 100, 1, 10, 1)
enemy2 = Character('Spider 2', 50, 0, 100, 1, 10, 1)
enemy3 = Character('Wolf 1', 100, 0, 250, 1, 15, 5)
enemy4 = Character('Wolf 2', 100, 0, 250, 1, 15, 5)
enemy5 = Character('Bear 1', 200, 0, 350, 1, 20, 10)
enemy6 = Character('Bear 2', 200, 0, 350, 1, 20, 10)
enemy7 = Character('Red Dragon', 300, 0, 800, 1, 30, 20)
enemy8 = Character('Blue Dragon', 400, 0, 1000, 1, 35, 20)
enemies = [enemy1, enemy2, enemy3, enemy4, 
           enemy5, enemy6, enemy7, enemy8] 

 


round = 1
#always run through entire cource of actions 
#unless a team has been deafeted 
#program then announces winner and exits
while (True):     
    print('Round',round,'\n')
    print('Action: ')
    #actions:
    #party attacks: 
    index=0
    activeEnemy = enemies[index] 
    #find enemy that is not dead 
    while activeEnemy.isDead():
        if index<8:
            index +=1
            activeEnemy = enemies[index]
        else:
            print('All enemies are dead. You are victorious')
            exit() 
    
    #entire party except the healer attacks the active enemy 
    #'index' makes sure party wins when 8 enemies have been defeated 
    for partyMember in party:
        if partyMember != party[1]: 
            if not activeEnemy.isDead():
                partyMember.attack(activeEnemy)
            else:
                index+=1
                if index<8:
                    activeEnemy = enemies[index]
                    partyMember.attack(activeEnemy)
                else:
                    print('All enemies are dead. You are victorious')
                    exit() #Party wins!
    #glinda heals
    glinda.heal(party)

    #enemy attacks
    #active enemy attacks all members (dead/alive)
    #enemy wins if entire Party is dead     
    while activeEnemy.isDead():
        index +=1
        activeEnemy = enemies[index]
    for partyMember in party:
        activeEnemy.attack(partyMember)
        if(party[0].isDead()and party[0].isDead()and party[0].isDead()):
            print('Entire party is dead. Enemy wins.')
            exit() #Enemy wins :( 
    round+=1

    #print stats:
    print('\nCharacter status:')
    #party status: 
    for partyMember in party:
        print(partyMember.__str__())
    #enemy status: 
    for enemyMember in enemies:
        print(enemyMember.__str__())
    print('\n')    
     
