import random
import sys
import os
def cleanup():
    raw_input("**Press any button to continue...")
    os.system("clear")

def banner(txt):
    print ("*")*(len(txt)+4)
    print ("* " + txt + " *")
    print ("*")*(len(txt)+4)

def pow(txt):
    print ("^")*(len(txt)+4)
    print ("| " + txt + " |")
    print ("^")*(len(txt)+4)


class Item:
    def __init__(self, name, price, count, description):
        self.name = self
        self.price = price
        self.count = count
        self.description = description
    def __str__(self):
        return (str(self.name) + ": " + str(self.price) + "-Gold, " + str(self.count) + "-left")
    def pack(self, user, backpack):
       backpack.append(self)

class SuperTonic(Item):
    def __init__(self):
        self.name = "Super Tonic"
        self.count = 5
        self.price = 20*((self.count-6) * (-1))
        self.description = "Brings your character back to max health.(Usable in battle)"
    def use(self, user, enemy):
        user.health = user.max
    def pic(self):
        print"______________________________8888888"
        print"_____________________________88"
        print"____________________________88"
        print"___________________________88"
        print"__________________________88"
        print"_________________________88"
        print"______________$$$$$$$$$$$$$$$$$$"
        print"_______________$______________$"
        print"________________$________ZZZZ$"
        print"_________________$_____ZZZZZ$"
        print"__________________$__ZZZZZZ$ "
        print"___________________$ZZZZZZ$"
        print"____________________$ZZZZ$"
        print"_____________________$ZZ$"
        print"______________________$$"
        print"______________________$$"
        print"____________________$$$$$$" 
        print"__________________$$$$$$$$$$"
        print"________________$$$$$$$$$$$$$$" 

class HolyHandGrenade(Item):
    def __init__(self):
        self.name = "Holy Hand Grenade"
        self.count = 25
        self.price = 20
        self.description = "Thous shalt count to three, no more, no less. (Never misses and does 15 damage, for use in a battle)"
    def use(self, user, enemy):
        enemy.health = enemy.health - 15
    def pic(self):
        print"                 .             "  
        print"                 .              " 
        print"                 .       :       "
        print"                 :      .        "
        print"        :..   :  : :  .          "
        print"           ..  ; :: .            "
        print"              ... .. :..         "
        print"             ::: :...            "
        print"         ::.:.:...;; .....       "
        print"      :..     .;.. :;     ..     "
        print"            . :. .  ;.           "
        print"             .: ;;: ;.           "
        print"            :; .BRRRV;           "
        print"             YB BMMMBR         "
        print"            ;BVIMMMMMt         "
        print"        .=YRBBBMMMMMMMB          "
        print"      =RMMMMMMMMMMMMMM;          "
        print"    ;BMMR=VMMMMMMMMMMMV.         "
        print"   tMMR::VMMMMMMMMMMMMMB:        "
        print"  tMMt ;BMMMMMMM  MMMMMMB.       "
        print" ;MMY ;MMMMMMMMM  MMMMMMMV       "
        print" XMB .BMMMMMMMMM  MMMMMMMM:      "
        print" BMI +MMMM     M  MMMMMMMMMi      "
        print".MM= XMMMMMMMM  M      MMMMY      "
        print" BMt YMMMMMMMM  MMMMMMMMMMi      "
        print" VMB +MMMMMMMM  MMMMMMMMMM:      "
        print" ;MM+ BMMMMMMM  MMMMMMMMMR       "
        print"  tMBVBMMMMMM  MMMMMMMMMB.       "
        print"   tMMMMMMMMM  MMMMMMMMB:        "
        print"    ;BMMMMMMMMMMMMMMMMY          "
        print"      +BMMMMMMMMMMMBY:           "
        print"        :+YRBBBRVt; "
        
class ArmorPlate(Item):
    def __init__(self):
        self.name = "Armor"
        self.count = 5
        self.price = 20*((self.count-6) * (-1))
        self.description = "Instant: Adds two armor to your character. (each point of armor negates one damage per attack)"
    def pack(self, user, backpack):
        user.armor = user.armor + 2
    def pic(self):
        print"\_________________/"
        print"|       | |       |"
        print"|       | |       |"
        print"|       | |       |"
        print"|_______| |_______|"
        print"|_______   _______|"
        print"|       | |       |"
        print"|       | |       |"
        print" \      | |      /"
        print"  \     | |     /"
        print"   \    | |    /"
        print"    \   | |   /"
        print"     \  | |  /"
        print"      \ | | /"
        print"       \| |/"
        print"        \_/"

class Nurse(Item):
    def __init__(self):
        self.name = "NURSE!"
        self.count = 9999
        self.price = 10
        self.description = "Instant: Our realm famous fairy medical staff will heal you up here and now. No refunds. (brings health back to max)"
    def pack(self, user, backpack):
        user.health = user.max
    def pic(self):
        print"        .----. "
        print"       ===(_)==   THIS WONT HURT A BIT..."
        print"      // 6  6 \ \ " 
        print"      (    7   )   "                    
        print"       \ \'--\' /     "       
        print"        \_ ._/       "      
        print"       __)  (__       "    
        print"    /\"`/`\`V/`\`\ "
        print"   /   \  `Y _/_ \ "
        print"  /     \_ |/ / /\ "
        print"  |     ( \/ / / / "
        print"   \  \  \      / "
        print"    \  `-/`  _.`"
        print"      `=._`=./ "

class ProtienShake(Item):
    def __init__(self):
        self.name = "Protien shake"
        self.count = 15
        self.price = 20 + ((self.count-15)*5) 
        self.description = "Instant: Adds 5 to your max health and 5 to your current health."
    def pack(self, user, backpack):
        user.max = user.max + 5
        user.health = user.health +5
    def pic(self):
        print"                 ,#####, "
        print"                 #_   _# "
        print"                 |a` `a| "
        print"                 |  u  | "
        print"                 \  =  / "
        print"                 |\___/| "
        print"        ___ ____/:     :\____ ___ "
        print"      .\'   `.-===-\   /-===-.`   \'. "
        print"     /      .-\"\"\"\"\"-.-\"\"\"\"\"-.      \ "
        print"    /\'             =:=             \'\ "
        print"  .\'  \' .:    o   -=:=-   o    :. \'  `. "
        print"  (.\'   /\'. \'-.....-\'-.....-\' .\'\   \'.) "
        print"  /\' ._/   \".     --:--     .\"   \_. \'\ "
        print" |  .\'|      \".  ---:---  .\"      |\'.  | "
        print" |  : |       |  ---:---  |       | :  | "
        print"  \ : |       |_____._____|       | : / "

class Axe(Item):
    def __init__(self):
        self.name = "Axe"
        self.count = 1
        self.price = 10
        self.description = "Instant: AND MY AXE... for +1 power."
    def pack(self, user, backpack):
        user.power = user.power + 1
    def pic(self):
        print"                   /^\ "
        print"          _.-`:   /   \   :\'-._"
        print"        ,`    :  |     |  :    \'."
        print"      ,`       \,|     |,/       \'."
        print"     /           \ \...//           \ "
        print"    :             \ \ \'//             :"
        print"    |             .\ \/.             |"
        print"    |             \'/\ \ \'             |"
        print"    :             //.\ \             :"
        print"     \           //\"\"\"\ \           /"
        print"      `.       /\'|     |\'\       ,\' "
        print"        `._   ;  |     |  ;   _,\' "
        print"           `-.:  |     |  :,-\' "
        print"                 |     |"
        print"                 |     |"
        print"                 |     |"
        print"                 |     |"
        print"                 |     |"
    
class Winchester(Item):
    def __init__(self):
        self.name = "Winchester"
        self.count = 1
        self.price = 25
        self.description = "Instant: Good ol' Winchester rifle, for those long shots... and +2 power."
    def pack(self, user, backpack):
        user.power = user.power + 2
    def pic(self):
        print" ,______________________________________"
        print"|_______________________________ [____]  \"\"-,__  __....-----====="
        print"                              \___________/   \"\"                |"
        print"                                      [ ))\"-,                   |"
        print"                                       \"\"    `,  _,--....___    |"
        print"                                               `/  "

class MagicMissilelauncher(Item):
    def __init__(self):
        self.name = "Magic Missile Launcher"
        self.count = 1
        self.price = 40
        self.description = "Instant: All the magic missiles you could ever want! Dont let it get dispelled! (+3 to power)"
    def pack(self, user, backpack):
        user.power = user.power + 3
    def pic(self):
        print"                                                   ,: "
        print"                                                 ,\' |"
        print"                                                /   :"
        print"                                             --\'   /"
        print"                                             \/ />/"
        print"                                             / <//_\ "
        print"                                          __/   /"
        print"                                          )\'-. /"
        print"                                          ./  :\ "
        print"                                           /.\' \'"
        print"                                         \'/\'"
        print"                                         +"
        print"                                        \'"
        print"                                      `."
        print"                                  .-\"-"
        print"                                 (    |"
        print"  ==============*            . .-\'  \'."
        print"                             ( (.   )8:"
        print"                         .\'    / (_  )"
        print"                          _. :(.   )8P  ` "
        print"                      .  (  `-\' (  `.   ."
        print"                       .  :  (   .a8a)"
        print"                      /_`( \"a `a. )\"\' "
        print"                  (  (/  .  \' )==\'"
        print"                 (   (    )  .8\"   +"
        print"                   (`\'8a.( _(   ("
        print"                ..-. `8P    ) `  )  +"
        print"              -\'   (      -ab:  )"
        print"            \'    _  `    (8P\"Ya"
        print"          _(    (    )b  -`.  ) +"
        print"         ( 8)  ( _.aP\" _a   \( \   *"
        print"       +  )/    (8P   (88    )  )"
        print"          (a:f   \"     `\"       `"

class LightSaber(Item):
    def __init__(self):
        self.name = "Light Saber"
        self.count = 1
        self.price = 55
        self.description = "Instant: Batteries and force crystal sold seperately. (+4 power)"
    def pack(self, user, backpack):
        user.power = user.power + 4
    def pic(self):
        print"                    ____"
        print"                 _.\' :  `._"
        print"             .-.\'`.  ;   .\'`.-."
        print"    __      / : ___\ ;  /___ ; \      __"
        print"  ,\'_ \"\"--.:__;\".-.\";: :\".-.\":__;.--\"\" _`,"
        print"  :\' `.t\"\"--.. \'<@.`;_  \',@>` ..--\"\"j.\' `;"
        print"       `:-.._J \'-.-\'L__ `-- \' L_..-;\'"
        print"         \"-.__ ;  .-\"  \"-.  : __.-\""
        print"             L \' /.------.\ \' J"
        print"              \"-.   \"--\"   .-\""
        print"             __.l\"-:_JL_;-\";.__"
        print"          .-j/\'.;  ;\"\"\"\"  / .\'\ \"-."
        print"        .\' /:`. \"-.:     .-\" .\';  `."
        print"     .-\"  / ;  \"-. \"-..-\" .-\"  :    \"-."
        print"  .+\"-.  : :      \"-.__.-\"      ;-._   \ "
        print"  ; \  `.; ;                    : : \"+. ;"
        print"  :  ;   ; ;                    : ;  : \:"
        print" : `.\"-; ;  ;                  :  ;   ,/;"
        print"  ;    -: ;  :                ;  : .-\"\'  :"
        print"  :\     \  : ;             : \.-\"      :"
        print"   ;`.    \  ; :            ;.\'_..--  / ;"
        print"   :  \"-.  \"-:  ;          :/.\"      .\'  :"
        print"     \       .-`.\        /t-\"\"  \":-+.   :"
        print"      `.  .-\"    `l    __/ /`. :  ; ; \  ;"
        print"        \   .-\" .-\"-.-\"  .\' .\'j \  /   ;/"
        print"         \ / .-\"   /.     .\'.\' ;_:\'    ;"
        print"          :-\"\"-.`./-.\'     /    `.___.\'"
        print"                \ `t  ._  /  "
        print"                 \"-.t-._:\'"

class Hire_DeadPool(Item):
    def __init__(self):
        self.name = "Wade Wilson"
        self.count = 1
        self.price = 150
        self.description = "Instant: Otherwise known as Deadpool.. He will fight with you.. for a price. (+10 power)"
    def pack(self, user, backpack):
        user.power = user.power + 10
    def pic(self):
        print "You have to buy me to get my picture. I dont put out for just anyone. ;)"
  
#####################

class Charachter:
    def __init__(self, name, health, power, level):
        self.name = name
        self.health = health
        self.max = health
        self.power = power
        self.evade = evade
        self.armor = armor
        self.level = 1

    def __str__(self):
        print self.name + ": " + self.health + "hp, " + self.power + "pw, " + self.evade + "ev, " + self.armor + "ar"

    def print_status(self):
        print ("The {} has {} health and {} power.".format(self.name, self.health, self.power))
 
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def attack(self, enemy):
        miss = random.randint(1, 100)
        if 1 < miss < (enemy.evade * 5):
            pow("The enemy missed!")
        else:
            if enemy.armor > self.power:
                    pow("The attack doesnt go through your armor!")
            else:
                damage = (self.power- enemy.armor)
                enemy.health = enemy.health - damage
                print ("The {} does {} dammage to the {}. The {} has {} health left.").format(self.name, damage, enemy.name, enemy.name, enemy.health)

class Hero(Charachter):
    def __init__(self):
        self.name = "hero"
        self.max = 20
        self.health = 20
        self.power = 5
        self.evade = 1
        self.armor = 0
        self.gold = 20
        self.level = 1
    def attack(self, enemy):
        crit = random.randint(1, 10)
        miss = random.randint(1, 100)
        reflect = random.randint(1,8)
        if 1 < miss < (enemy.evade * 5):
            pow("You missed!")
        else:
            if crit < 3:
                if (enemy.armor > (self.power*2)):
                    pow("It doesnt go through the enemies armor!")
                else:
                    damage = (self.power*2 -enemy.armor)
                    pow ("Critical Strike!")
                    enemy.health = enemy.health - damage
            else:
                if enemy.armor > self.power:
                    pow("It doesnt go through the enemies armor!")
                else:
                    damage = (self.power- enemy.armor)
                    enemy.health = enemy.health - damage
                    print ("The hero does {} damage to the {}. The {} has {} health left.".format(damage, enemy.name, enemy.name, enemy.health))
            if isinstance(enemy, FireEmp):
                self.health = self.health - 1
                pow ("The hero is hurt by the flames. He takes one damage.")
            if isinstance(enemy, RockGolem) and reflect == 1:
                self.health = self.health - (self.power/2)
                pow("The rock golem's hard skin makes your sword bounce back doing half your power as damage top you!")
    def __str__(self):
        evdpct = self.evade*5
        return ("| Health: {}\n| Max-Health: {}\n| Power: {}\n| Evade: {}({}%)\n| Armor: {}\n| Gold: {}".format(self.health, self.max, self.power, self.evade, evdpct, self.armor, self.gold ))
    def pic(self):
        print'   ,   A           {|} '
        print'  / \, | ,        .--. '
        print' |    =|= >      /.--.\ '
        print'  \ /` | `       |====| '
        print'   `   |         |`::`| '
        print'       |     .-;`\..../`;-. '
        print'      /\ \/  /  |...::...|  \ '
        print'      |:\'\ |   /\'\'\'::\'\'\'\   | '
        print'       \ /\;-,/\   ::   /\--; '
        print'       |\ <` >  >._::_.<,<__> '
        print'       | `\"\"`  /   ^^   \|  | '
        print'       |       |        |\::/ '
        print'       |       |        |/||| '
        print'       |       |___/\___| \'\'\' '
        print'       |        \_ || _/ '
        print'       |        <_ >< _> '
        print'       |        |  ||  | '
        print'       |        |  ||  | '
        print'       |       _\.:||:./_ '
        print'       |      /____/\____\ '

class Medic(Charachter):
    def __init__(self, level):
        self.name = "Witch Doctor"
        self.health = 10 + (10*.1*level)
        self.max = 10 + (10*.1*level)
        self.power = 2 + (2*.1*level)
        self.evade = 2 + (2*.1*level)
        self.armor = 0 + (0*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1
    def attack(self, enemy):
        miss = random.randint(1, 100)
        recover = random.randint(1, 10)
        if recover < 3 and self.health < 9:
            self.health = self.health + 2
            pow("The witch doctor cures his Wounds! (+2 hp)")
        if 1 < miss < (enemy.evade * 5):
            pow("The Wich Doctor missed!")
        else:
            if enemy.armor > self.power:
                pow("It doesnt go throught the your armor!")
            else:
                damage = (self.power - enemy.armor)
                enemy.health = enemy.health - damage
                print ("The Medic does {} damage to the {}. The {} has {} health left.").format(damage, enemy.name, enemy.name, enemy.health)
    def descripty(self):
        print "You hear a witch doctor's cackle coming from a dark corner of the cave. Prepare for a fight."
    def pic(self):
        print'                                       __,,, '
        print'                                 _.--\'    / '
        print'                              .-\'        / '
        print'                            .\'          | '
        print'                          .\'           / '
        print'                         /_____________| '
        print'                       /`~~~~~~~~~~~~~~/ '
        print'                     /`               / '
        print'      ____,....----\'/_________________|---....,___ '
        print',--\"\"`             `~~~~~~~~~~~~~~~~~~`           `\"\"--, '
        print'`\'----------------.----,------------------------,-------\'` '
        print'               _,\'.--. \                         \ '
        print'             .\'  (o   ) \                        | '
        print'            c   , \'--\'  |                        / '
        print'           /    )\'-.    \                       / '
        print'          |  .-;        \                       | '
        print'          \_/  |___,\'    |                    .-\' '
        print'         .---.___|_      |                   / '
        print'        (          `     |               .--\' '
        print'         \'.         __,-\'\             .\' '
        print'           `\'-----\'`      \        __.\' '
        print'                           `-..--\'` '

class Shadow(Charachter):  
    def __init__(self, level):
        self.name = "shadow"
        self.health = 1 + (1*.1*level)
        self.max = 1 + (1*.1*level)
        self.power = 1 + (2*.1*level)
        self.evade = 18 
        self.armor = 0 + (1*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1
    def descripty(self):
        print "You dont hear anything, but the shadow on the wall you see moving definately isn't yours. Without warning it lunges forward."
    def pic(self):
        print"....................,,,,,,:::::~~~~~~~~~~==========+++==================~~~~~~::::::,,,,............"
        print"....................,,,,,:::::~~~~~~~~~~~=========++++==================~~~~~~~:::::,,,,............"
        print"....................,,,,::::::~~~~~~~~~~~========+++++++========++======~~~~~~~::::,,,,,............"
        print"...................,,,,,::::::~~~~~===========+++++++++++===++~:+=++=====~~~~~~:::::,,,,,..........."
        print"...................,,,,,::::::~~~~~==========++++++++++++++++=~=+:=:======~~~~~~::::,,,,,..........."
        print"...................,,,,,:::::~~:~~~========:.......~++++++++++++=~+:=,====~~~~~~:::,,,,,,..........."
        print"..................,,,,,:::::~~:~,~~======............=++++++++++++,~:,:~==~~~~~~:::,,,,,,..........."
        print"..................,,,,,:::::::~,=~======.............,++++++++++=++:::,::~~~~~~~::::,,,,,..........."
        print"..................,,,,,::::,,,~~~=======..............=++++++++=++++,:.::,:~~~~~::::,,,,,..........."
        print"..................,,,,::::,:,,:~======+=.............,:++++++++~+++=,:.....:~~~::::,,,,,,..........."
        print"..................,,,,:::,:..,:~====+++=..............=++++++++:=++~.......,~~~::::,,,,,............"
        print"..................,,,,:::.....~~~===++++,............~+++++++++=,~~........,:~~::::,,,,,............"
        print".................,,,,,::,.....~:~==++++++~..........~+??????????+=.........:~~~::::,,,,,............"
        print".................,,,,,::.......~===+++++++=.........=+???????????+:.......:~~~~::::,,,,,............"
        print".................,,,,:::.....,~===+++++++++~............,,,,::~=++~......:~~~~~::::,,,,,............"
        print".................,,,,:::,...~======~::..........................,~~~....:~=~~~~::::,,,,,............"
        print".................,,,,,:...,~==~,..................................,::,..,~=~~~~::::,,,,,............"
        print"..................,,,,....:~~,...........................................:~~~~~::::,,,,,............"
        print"..................,,,,...................................................,:~~~::::,,,,,,............"
        print"..................,,,.....................................................::~~::::,,,,,............."
        print"..................,,......................................................,:::::::,,,,,............."
        print"..................,........................................................,::::::,,,,,............."
        print"..............................................................,:::..........,::::,,,,,.............."
        print"..............................................................~===~,.........,,:,,,,,,.............."
        print"................................:==~,........................,~=+++=~,........,,,,,,,,.............."
        print"..............................,~=++=,........................,~=+?++=~:........,,,,,,,.............."
        print".............................:~=+++~,........................,~=+?+++=~:,.......,,,,,,.............."
        print"...........................,:~=++++~,........................,~=+++++=~~:,.......,,,,..............."
        print"..........................:~~==+++=~,........................,~=++++===~~::,,,..,,,,,..............."
        print"........................,::~~===++=~,.........................:~=+++===~~~:::,,,,,,,................"
        print"......................,,:::~~===++=~,.........................:~==+===~~~:::::,,,,,,................"
        print"....................,,,,:::~~~==+==~,.........................:~======~~~::::,,,,,,................."
        print"..................,,,,,,::::~~====~:..........................,:~====~~~::::,,,,,,,................."
        print"..................,,,,,,::::~~~===~:..........................,:~~==~~~:::::,,,,,,,................."
        print"...................,,,,,::::~~~==~~:..........................,::~~~~~~::::,,,,,,,.................."
        print"..................,,,,,,,,:::~~~~~:,...........................,:~~~~~::::,,,,,,,,.................."
        print"..................,,,,,,,,:::~~~~~:,...........................,::~~~:::::,,,,,,,,.................."
        print"..................,,,,,,,,::::~~~~:,...........................,,::::::::,,,,,,,,,.................."
        print"..................,,,,,,,,::::~~~::,...........................,,:::::::,,,,,,,,,..................."
        print"................,,,,,,,,,,::::~~~::,............................,,::::,,,,,,,,,,,,,,................"

class Goblin(Charachter):
    def __init__(self, level):
        self.name = 'Goblin'
        self.health = 6 + (12*.1*level)
        self.max = 6 + (12*.1*level)
        self.power = 2 + (2*.1*level)
        self.evade = 3 + (3*.1*level)
        self.armor = 0 + (3*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1
    def descripty(self):
        print "You see a simple goblin waddle forth."
    def pic(self):
        print"             (         .-,"
        print"            / )      .\' (       ___"
        print"           //(.-\"\"\"-/ /\ )   .-\"   \"-."
        print"           |.\'     _`.\// .-\'         `..--."
        print"       ..--/-.   .\'_` `\'-\'      ___    ( C\ \ "
        print"      /   /O\    / O\   |     .\'   ```--`-|_/"
        print"     /    \_/|   \__/   |    ("
        print"    |     _\-\' _   __  /      `."
        print"    \ ,--7  `.(_)_.| .\'         `."
        print"     | C._)   `.___/\' .---._      \           __"
        print"     \    |       `. /      `-.    \        ,\'  `."
        print"      `--\'          Y          \    |       )     `-._.--.__"
        print"                    |     \         |    _.\'  .--.___.-\'`--.\ "
        print"                    |      |        |\  /    /              `"
        print"               _    \      |       /  `v    |"
        print"          .\'`-\' `--._)     /::___.\'     \   /"
        print"         /    .---.       /   `-.        \ |"
        print"      _.\' _.-\' `._ `-.   /       `.       /"
        print"     /.--\'        `-. `. \         `-.__.\'"
        print"                     `.\'_/ "

class Zombie(Charachter):
    def __init__(self, level):
        self.name = 'zombie'
        self.health = 10 + (10*.1*level)
        self.max = 10 + (10*.1*level)
        self.power = 1 + (1*.1*level)
        self.evade = 2 + (2*.1*level)
        self.armor = -1 + (-1*.1*level)
        self.level = 1 + (1*.1*level)
    def alive():
        return True
    def descripty(self):
        print " "
    def pic(self):
        " "

class Slime(Charachter):
    def __init__(self, level):
        self.name = 'Slime'
        self.health = 10 + (15*.1*level)
        self.max = 10 + (15*.1*level)
        self.power = 1 + (2*.1*level)
        self.evade = 2 + (3*.1*level)
        self.armor = -1 + (1*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1 
    def descripty(self):
        print "An amorpheous blop drops from the ceiling of the cave and lands at your feet. I wouldn't step in that if I were you..."
    def pic(self):
        print"                                              7                                                     "
        print"                                                                     7       7                      "
        print"                                    7 7                      7~,:=777    7                          "
        print"                                           7              ,~:~~~~~~~~,7                             "
        print"                                                       +::~:~~::::~:::~,7                           "
        print"                                                     I:~:~:::::~~::::::~.:77                        "
        print"                                        7          7=::~:::::::::,:,,::,,.~I7                       "
        print"                   7                              7~~~:::~,:,~:::::::::,:~:.,7                      "
        print"                         7            7           ~:~~:~:~::~:::::::::::::,..,7                     "
        print"                 7                      77       ~~~~~~:~~~~,:~::~::~~::::.,..,7                    "
        print"                7                               ~~::~~:~~~~~~:,.,.,::::,,,,:~..7                    "
        print"                                               7~~~:~~:~~~=~~~,..,:::~~~:~:....:7                   "
        print"                       7                       ~~~,:~~:......:::.,,~~~~~~,:....,7   7               "
        print"                                              ~:~::~~~,.,==~:,:,.,,:.....,......7                   "
        print"               7             7               7:~.~~~~,,=??=~~,,,,.,+=~,..,......                    "
        print"                                             ~:,~~~~,,.====::,.,:,??=~:,........7                   "
        print"                                           7:~,:~~::.:.:~~~,,.,,,.,~~~~..,,.....7                   "
        print"                                          7~:,=:~~~:...,..~,,,:~,,..,,....,......7        7         "
        print"                                         7~::~:~~~.~====~:,,:~~~~~~..,...:,......7         7        "
        print"                                        :~:.~:~~~~.,,,,,.,:~~~~~:~:=,.,:::,......,7                 "
        print"                                       =~:...+~~:,.....,:~=~~,....~:::.:,,........7             7   "
        print"                                     ?=:~..==~:~:...,::~~:,.........::~...........,7                "
        print"                                     ~:~.,~~:~:~,,.::~:,,............,::...........7                "
        print"                                    ,.=:~=~:::~,,:~~::,...............,:,..........7                "
        print"                                   ,~~~~~:,~~:,:~~~~:,................,~:..........,7               "
        print"                                  ,:~~,:::~~:,~~~:,,....................~~..........7               "
        print"                   777         7.,:~:,~:,~~::~~~,,,........:=~~~~~~....,.:...........7              "
        print"                              7,::,,,~:.~~.:~~:,,.....:==~~~~~:~:~=~~~...~~...........7             "
        print"                           7,:~~~,:~~.:::..:,~:...:~~~~:,,,,,..,,,:::~~.,.:...........?7            "
        print"                          =.~~:::=~:.~::.~,.~~~~~~~:::,...........,,,:~=:.:,...........7            "
        print"                       ~,.=,,::.=:,::~=::..,:,.,,:~....,..,,,.......,..:~:::............7           "
        print"                     :..,,~~::~~,,:~~~:~,....,:~:::~,,.....,.,........,...::............7           "
        print"                   7.,..~:,,.~:.:~::~::,...:~~~~::::,...,...::,.........................+           "
        print"                  ,..~~::,.:~,..:.,~:~,,.:~~~::~::~,.......:~~:.........................,7          "
        print"    7            ..~~::..~=~:....:~::..,~~~~~~~~::,,......,:~~,,.........................7          "
        print"               7,~:,.,,.~~~,,..:~~::,.:=~=~~:~~~~,........,,:~,,.........................~7         "

class FireEmp(Charachter):
    def __init__(self, level):
        self.name = "Fire Imp"
        self.health = 6 + (10*.1*level)
        self.max = 6 + (10*.1*level)
        self.power = 3 + (6*.1*level)
        self.evade = 4 + (4*.1*level)
        self.armor = 0 + (0*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1
    def attack(self, enemy):
        miss = random.randint(1, 100)
        if 1 < miss < (enemy.evade * 5):
            pow("The Fire Imp missed!")
        else:
            if enemy.armor > self.power:
                pow("It doesnt go throught the your armor!")
            else:
                preburn = self.power - enemy.armor
                damage = self.power + 1 - enemy.armor   
                enemy.health = enemy.health - damage
    def descripty(self):
        print "An Imp leaps fromt he fire of a torch lit on the wall, it looks like it wont be letting you pass by freely."
    def pic(self):
        print"                                     ,                 "
        print"       ,  .   (          )          -.\ |"
        print"       | / .- |\        /|         _ \ \'/"
        print"       \ \'/   | \.-\"\"-./ |          \_) ;-\' "
        print"     `\'-; (_/ ;   _  _   ;           ) /"
        print"         \ (   \ (.\/.) /    .-.    / |"
        print"          \ \   \ \/\/ /-._.\'   \   | |"
        print"           \ \   \ .. /_         \  | |"
        print"            \ \   |  |__)     |\  \ | |"
        print"             \ `\"`|==|_       | \  \| |"
        print"              \,-\'|==| \      |  \    |"
        print"                   \/   \'.    /   `\ /"
        print"                          |   |     `   ,"
        print"                          |   |         )\ "
        print"                __.....__/    |        /  \ "
        print"              /`              \        `//`"
        print"              |  \`-....-\'\    `-.____.\'/"
        print"              |  |        /   /`\"-----\'`"
        print"              |  |        |  |"
        print"              | /         |  |"
        print"       .------\' \         /  /"
        print"      (((--------\'        \  |"
        print"                           | \ "
        print"                           | |"
        print"                           | |"
        print"                           | /"
        print"                          /  )"
        print"                         /   |"
        print"                        (-(-(\' "
    
class RockGolem(Charachter):
    def __init__(self, level):
        self.name = "Rock Golem"
        self.health = 15 + (20*.1*level)
        self.max = 15 + (20.1*level)
        self.power = 1 + (6*.1*level)
        self.evade = 0 
        self.armor = 2 + (6*.1*level)
        self.gold = 10 + (5*.2*level)
        self.level = 1
    def descripty(self):
        print "A place in the cave wall begins to move. Great, they have a cave troll.... wait it's just a rock golem. Prepare yourself!"
    def pic(self):
        print"                   (    )"
        print"                  ((((()))"
        print"                  |o\ /o)|"
        print"                  ( (  _\')"
        print"                   (._.  /\__"
        print"                  ,\___,/ \'  \')"
        print"    \'.,_,,       (  .- .   .    )"
        print"     \   \ \     ( \'        )(    )"
        print"      \   \ \    \.  _.__ ____( .  |"
        print"       \  /\ \   .(5   .\'  /\  \'.  )"
        print"        \(  \ \.-\' ( /    \/    \)"
        print"         \'  ()) _\'.-|/\/\/\/\/\|"
        print"             \'\ \ .( |\/\/\/\/\/|"
        print"               \'((  \    /\    /"
        print"               ((((  \'.__\/__.\')"
        print"                ((,) /   ((()   )"
        print"                 \"..-,  (()(\"   /" 
        print"                    _//.   ((() .\""
        print"          _____ //,/\" ___ ((( \', ___ "
        print"                           ((  )"
        print"                            / /"
        print"                          _/,/\'"
        print"                        /,/,\""  

class DarkWizard(Charachter):
    def __init__(self):
        self.name = "Dark Wizard"
        self.health = 250
        self.max = 250
        self.power = 15
        self.evade = 8
        self.armor = 10
        self.level = 1
    def descripty(self):
        print "The man you have been searching for, who started all of this madness. you charge forward and scream, FOR DEMACIA!!!!   .. oh wait, is that you gandalf?"
    def pic(self):
        print"................................................................:......................:...................................................."
        print"...............................................................~~......................=...................................................."
        print".......................................,......................,~~~.....................??..................................................."
        print".......................................::.....................~~~~,....................?+I.................................................."
        print"......................................:::.....................~~~~~....................:?+?................................................."
        print"....................................:::::,....................~~~~~:....................?+I,................................................"
        print"..................................:::::,,:....................~~~~~~:...................??:?................................................"
        print".................................:::::.,::...................,~~~~~~~~..................I???+..............................................."
        print"................................,::,,,,:::...................~~~~~~~~~~,................???=I..............................................."
        print"................................:,,,::::~....................~~~~~~~~~~~:................???II.............................................."
        print"................................:,::::::,...................~~~~~~~~~~~~~~...............I??=?+............................................."
        print"................................:::::::..,.................~~~~~~~~~~~~~~~~..............:?????............................................."
        print"...............................:::::::,,:,................~~~~~~~~~~~~~~~~~~..............???~I?............................................"
        print"...............................:::::.,,,:................~~~~~~~~~~~~~~~~~~~~..............??I??............................................"
        print"..............................::::.,,,:::...............~~~~~~~~~~~~~~~~~~~~~,.............+??:??..........................................."
        print"..............................:::.,,.::::..............~~~~~~~~~~~~~~~~~~~~~~~..............???I?,.........................................."
        print"..............................::,,.:::::..............~~~~~~~~~~~~~~~~~~~~~~~~~.............~??:??.........................................."
        print"..............................,:,:::::::.............~~~~~~~~~~~~~~~~~~~~~~~~~~..............?????:........................................."
        print"................................:::::::..............~~~.,:~~~~~~~~~~~~~~~~:.:~,..............??=??........................................."
        print"................................::::::..............:~~~~~~~~~~~~::,,........,:~:.............+??~I:........................................"
        print"...............................::::::...........:~,.,:::::::::::::,,,,,,,,,,::::::::,..........????I........................................"
        print"...............................:::::,........,::::::,.,++,+++++++++++++++,+++++,,.::::::,......,??~?~......................................."
        print"..............................,:::::......:::,.::::::++++,+++++++++++++++++=++++~::::,,::::,....I?II?......................................."
        print"..............................:::::.....::.:::::::::,++++,+++++=+=+++++++++~+++++,:::::::::::,...??~II......................................"
        print"..............................:::::....:::::::::::::=+++,++++++~+~+++++++++~++++++::::::::::::,..+?I??......................................"
        print"..............................::::,....:::::::::::::~++++.=I777?=++=77777:+,++++++~:::::::::::,...??:??....................................."
        print".............................:::::.....:::::::::::::,++++I7I~777++=777.777?~+++++++.:::::::::.....=??I?....................................."
        print".............................:::::.......::::::::::::=+++~?777?=+++=?777?~+.++++++++:::::::........??+??...................................."
        print".............................::::..........::::::::::++++?=+?+=+++++,?+?=+++~+++++++,:.............,????,..................................."
        print".............................::::..............,::::,++++?++++?++++++++++++++~++++++,...............II+??..................................."
        print".............................::::...................+++++~+++:++++++~++++++,+=++++++~................??+?..................................."
        print"............................,:::,..................:++++++,=++?+?=+++++++,++++++++++=................=?+?I.................................."
        print"............................::::...................++++++=+++++++++++++++++~+++++++++.................??:?.................................."
        print"............................::::...................~++++++++++++..~==+++++++,+++++++,=~~~~............,?II?................................."
        print"............................::::.................:~:+++++++++::+..:==~=?=++++=+++++++~~~~~~~~..........I?:?................................."
        print"............................::::...............~~~~,++++++++~?+:+++++++++=+++~.++++++,~~~~~~~~~.........II??................................"
        print"...........................,:::...............~~~~~+++++=++++,++:=++++~~+~+++++=++++++~~~~~~~~~~~.......=?:?=..............................."
        print"...........................::::..............~~~~~.++++,,++~++++~+++=+++++++++==++++++~~~~~~~~~~~~,......I?I?..........:...................."
        print"...........................::::.............~~~~~~+++++++=+,++++++=+~+++++=+++:+:+++++:~~~~~~~~~~~~:.....~?,?=........,:,..................."
        print"...........................::::............:~~~~~,++++~++++:++++++++++++++:=++,++~++++~~~~~~~~~~~~~~~,....I?=?.......,::...................."
        print"...........................:::.............~~~~~::+++,+++=+++++++++++++++++~++:+++++++~~~~~~~~~~~~~~~~~...:??I?......::....................."
        print"..........................,:::............,~~~~~:+=~~,+++:+++++++++++++++++++=,+++,+++~~~~~~~~~~~~~~~~~~~:.??:??....::......................"
        print"..........................::::............~~~~~:=,====+++,:+++++++++++++++++=,+++++~++:~~~~~~~~~~~~~~~~~~~~+??I?I..,:......................."
        print"..........................::::............~~~~~:~====++++~~+++++++++++++++++:~+++++===~~~~~~~~~~~~~~~~~~~~~.?????,:,........................"
        print"..........................::::............~~~~~~=====++++=++++++++++++++++++~++++++==~~~~~~~~~~~~~~~~~~~~~~.I?=:,:.~~~......................"
        print"..........................:::,...........,~~~~,====~~=+++++++++++++++++++++++++++++=~=~~~~~~~~~~~~~~~~~~~~++=?,,,,===~~~...................."
        print"..........................:::............:~~~~=======.+++++++++++++++++++++++++++++~==~~~~~~~~~~~~~~~~~~~,+++::,:===~==.:,.................."
        print".........................,:::............~~~~:~======,+,++++++++++++++++++++++++++=~==~~~~~~~~~~~~~~~~~~~:=,,:.+++:~~~~~::.................."
        print".........................::::............~~~~:=======.:~++++++++++++++++++++++++.+,=~=~~~~~~~~~~~~~~~~~~~::::+++++:+.==::,~................."
        print".........................::::...........:~~~,~====~==.~~++++++++++++++++++++++++:+====:~~~~~~~~~~~~~~~~~,,:,~++++++++=~,:,,:................"
        print".........................::::...........~~~~=~=======,~~+++++++++++++++++++++++=~~====,~~~~~~~~~~~~~~:,,:,~~~~,==++??==:::,~................"
        print".........................:::,...........~~~,=========:~~+++++++++++++++++++++++~~=====,~~~~,~~~~~~~~~.,.:~~~~:~,.,..=~,,:::.:..............."
        print".........................:::...........:~~~==========~~~++++++++++++++++++++++,=~====~:~~~~,~~~~~~~~~~~~~~~~~:~~.:::::,:::::~..............."
        print"........................::::...........~~~,~======~=~~~~=++++++++++++++++++++:===~====~~~~~,~~~~~~~~~~~~~~~~~,~~,::::::::::,~..............."
        print"........................::::..........~~~~=========~:~~~:+++++++++++++++++++,==========~~~~:~~~~~~~~~~~~~~~~:~~~::::::::::::::.............."
        print"........................::::.........~~~~~==========:~~~~:+,++++++++++++++?=~==========:~~~~~~~~~~~~~~~~~~~:~~~~~,::::::::::,~.............."
        print"........................::::........~~~~:===~~=====:~~~~~~+~++++++++++++++~==========~=,~~~~:~~~~~~~~~~~~~~~~~~~~:::::::::::.~.............."
        print".......................,:::,......,~~~~,~~~========:~~~~~~~=+++++++++++++,.============:~~~~:~~~~~~~~~~~~~~~~~~~~,::::::::::,~.............."
        print".......................::::......~~~~~:===========,~~~~~~~~:~++++++++++++~.======~=====:~~~~~.~~~~~~~~~~~~~~~~~~~.::::::::::,~.............."
        print".......................::::....:~~~~~:============~~~~~~~~~~:+++++++++++~~:=========~==~~~~~~~.,~~~~~~~~~~~~~~~~~::::::::::::~.............."
        print".......................::::..,~~~~~~~=~==========,~~~~~~~~~~~+++++++++++,~:===========~~~~~~~~.....:~~~~~~~~~~~~~~,,:::::::::~.............."
        print".......................::::.~~~~~~~~~===========~~~~~~~~~~~~:+++++++++++,~:===========~~~~~~~~,......,~~~~~~~~~~~~,:::::::::::.............."
        print".......................:::,~~~~~~~~:~==========~:~~~~~~~~~~~:+++++++++++,~,===========:~~~~~~~.........:~~~~~~~~~~~,::::::::,,.............."
        print"......................,:::.~~~~~~~,============:~~~~:~~~~~~~~:++++++++++,~.===========,~~~~~~~...........~~~~~~~~~~::::::::::..............."
        print".....................,::::,~~~~~~~~===========:~~:~~,~~~~~~~~~~+++++++++~~.==~=~~=====,~~~~~~~.............~~~~~~~~~,:::::::::,............."
        print"....................~~:::::~~~~~~============:~~~.~~:~~~~~~~~~~:+++++++=~~,~~~~~~~==~=:~~~~~~~..............,~~~~~~~~:::::::::~............."
        print"...................~:,::::~~~~~~========~~==:~~~~~~~~~~~~~~~~~~~,++++++,~=======~~====~~~~:~~:.................~~~~~~,,:::::::.............."
        print".................,==~,::::=,~:=============:~~~~~~.~~~~~~~~~~~~~:++++++~========~~===~~~~~:~~....................,~~~~.:::::::,:............"
        print"................:==,++:,::++.~============:~~~~~~~~~~,~~~~~~~~~~~+++++.~:,======~~===,::::::........................~~~,:::::::~............"
        print"................===?+++++++++~==========~,~~~~~~~~~~:~~~~~~~~,,,::,+++:~~=======~~===.:::::::.........................~~:::::::,............"
        print"...............:==~,=+++++?++~==========,~~~~~~~~~~~~,:::::~~~~:+~::+~~~:=======~~===::::::::..........................:~,:::::............."
        print"...............~==.+++++:+++===========,~~~~~~~~~~~~,:::::,~~~~~?~~~:~~~=======~~~==~:~~~:~~~~...........................~,:::::............"
        print"...............===.++++++++?========~=.~~~~~~~~~~~~~::::::,~~~~:?=:====:======~~==~,:,~~~~,~~~~............................:,,,:............"
        print"...............===~++=.=++?+========~,~~~~~~~~~~~~~,~~,~~~:~~~====:===~,=:~,=.:,.::.:,~~~~~~~~~............................................."
        print"...............,===++++++++========~,~~~~~~~~~~~~~,~~:~~~~:~~:====:====:~=,~~.:,.::,,,~~~~~,~~~~............................................"
        print"................~=~~.:~~~~:========.~~~~~~~~~~~~~,~~~,~~~~:~~:====:==~:=::~:,::,.:~:,,~~~~~~~~~~~..........................................."
        print"................,==~.:::.==~=====~.~~~~~~~~~~~~~.~~~~~~~~::::,~~~=~==~~:~==..~,,,:~,,,~~~~~~~~~~~:.........................................."
        print"..................==.:::,~======~.~~~~~~~~~~~~~,~~~~~~~~~~::::~~==~=~~:~~~.::,.:,~~,:,~~~~~~:~~~~~.........................................."
        print"..................:~::::~===~===.~~~~~~~~~~~~~:~~~~~,~~~~~::::~~====~==~::=~::~~:~~.:,~~~~~~:~~~~~~........................................."
        print"..................~~::::======~.~~~~~~~~~~~~~~~~~~~~,~~~~~:::::=====::::==:~:~==~~:.,,~~~~~~:~~~~~~........................................."
        print".................==,::::=====~,~~~~~~~~~~~~~~~~~~~~~~~~~~~.:::,====:~==::,~~==+=~~,,,,~~~~~~,~~~~~~~........................................"
        print"................~==.:::,~~===.~~~~~~~~~~~~~~~~~~~~~:~~~~~~.::~:=====:::==~=:~~=~::.~:~~~~~~~,~~~~~~~........................................"
        print"...............:==~::::,~=~=.:~~~~~~~~~~~~~,~~~~~~~.~~~~~~~:~~~====:==:~:~::::::,,.~~~~~~~~~:~~~~~~~~......................................."
        print"..............:===~:::::~=~.::~~~~~~~~~~~~,~~~~~~~~~~~~~~~~~~~~====~=~~~~~~~~~~~~.,~~~~~~~~~~~~~~~~~~:......................................"
        print".............~~====::::~~~.:::,~~~~~~~~~~:~~~~~~~~~~~~~~~~~:~~~=====:~~~~~~~~~~~~~~~~~~~~~~~~,~~~~~~~~......................................"
        print"............=~====~::::~=.::::,,~~~~~~~~~~~~~~~~~~:~~~~~~~~:~~~====~.~~~~~~~~~~~~~~~~~~~~~~~~~:~~~~~~~~....................................."
        print"...........~====~=.::::~.:::::::.~~~~~~~~~~~~~~~~~,~~~~~~~~,~~~===~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~...................................."
        print".........~========,::::...,:::::::~~~~~,~~~~~~~~~~,~~~~~~~~:~~~~=~~~~,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~..................................."
        print"........:=========::::.....:,::::,:~~~,~~~~~~~~~~~.~~~~~~~~:::,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:.................................."
        print".......~.===~~===~::::.......,::::.~~.~~~~~~~~~~~~,~~~~~~~::~~:~~~~~~~:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:................................."
        print"......=.~.=..,~==~::::..........::~..,~~~~~~~~~~~~,~~~~~~~:::~~~~~=~=~~:====~~~~~:~~=~~~~~~~~~~~~~~~~~~~~~~,................................"
        print".....~.~.~....~...::::...............~~~~~~~~~~~~~:~~~~~~~~~~~~~~~~~~~:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~................................"
        print"....~.=.~.:.,..~,,::::...............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,~,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~..............................."
        print"...:.~.:.~.=.:..~::::...............:~~~~~~~~~~~~:~~~~~~~~~~~~~~~~~~~~.~~,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:.............................."
        print"..~.=.,.:.:.~.:,.::::...............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,~~~.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.............................."
        print".~.~.:.......:.~.::::...............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.~~~~:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:............................."
        print":.~....~.:.:..:.:::::..............:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.,~~~~,:.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~............................."
        print".,..~.~.,.:.:.~.::::,..............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~::~~~~~.::,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~............................"
        print"...:.,..,.,..:.~::::...............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.:~~~~~~~,::::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,..........................."
        print".......:.=.~.~..::::..............:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~::~~~~~~~~::::::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~..........................."
        print"...............,::::..............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.:,~~~~~~~~:::::::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.........................."
        print"...............::::,..............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~::,~~~~~~~~~,::::::::~~~~~~~~~~~~~~~~~~~~~~~~~~,........................."
        print"...............::::..............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.::~~~~~~~~~~~.::::::::,~~~~~~~~~~~~~~~~~~~~~~~~~........................."
        print"...............::::..............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,::,~~~~~~~~~~~~.:::::::::.~~~~~~~~~~~~~~~~~~~~~~~~........................"
        print"..............,::::..............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~::::~~~~~~~~~~~~~,::::::::::,:~~~~~~~~~~~~~~~~~~~~~:......................."
        print"..............::::,.............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,:::~~~~~~~~~~:~~~~.::::::::::::::~~~~~~~~~~~~~~~~~~~......................."
        print"..............::::..............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,:::.~~~~~~~~~~~~~~~~.:::::::::::::.~~~~~~~~~~~~~~~~~~:......................"
        print"..............::::..............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~:::::~~~~~~~~~~~:~~~~~:::::::::::::::.~~~~~~~~~~~~~~~~~......................"
        print".............,::::.............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,::::~~~~~~~~~~~~~,~~~~~~,::::::::::::::.~~~~~~~~~~~~~~~,....................."
        print".............::::,.............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.~:::,~~~~~~~~~~~~~~,~~~~~~~:::::::::::::::.~~~~~~~~~~~~~~....................."
        print".............::::.............:~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,:::::~~~~~~~~~~~~~~~~,~~~~~~~~,::::::::::::::.~~~~~~~~~~~~....................."
        print"............,::::.............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~::::::,~~~~~~~~~~~~~~~~~,~~~~~~~~~,::::::::::::::,~~~~~~~~~~~...................."
        print"............:::::.............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~::::::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,::::::::::::::~~~~~~~~~...................."
        print"............::::.............~~~~~~~~~~~~~~~~~~~~~~~~~~~~~::::::.~~~~~~~~~~~~~~~~~~~~~,~~~~~~~~~~~~~.:::::::::::~~~~~~~~~..................."
        print"............::::.............~~~~~~~~~~~~~~~~~~~~~~~~~~~~,::::::~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.::::::::.~~~~~~~,.................."
        print"...........,::::............:~~~~~~~~~~~~~~~~~~~~~~~~~~~.::::::.~~~~~~~~~~~~~~~~~~~~~~~~~,~~~~~~~~~~~~~~~~~,:::::::.~~~~~~.................."
        print"...........:::::............~~~~~~~~~~~~~~~~~~~~~~~~~~~,:::::::~~~~~~~~~~~~~~~~~~~~~~~~~~~~:~~~~~~~~~~~~~~~~~,:::::::~~~~~~................."

###################################
###################################
###################################

def fight_sequence(flenemy, hero, backpack):
    print" "
    flenemy.pic()
    flenemy.descripty()
    cleanup()

    while flenemy.alive() and hero.alive():
        print"___________________________________________________________________________________"
        hero.print_status()
        flenemy.print_status()
        print"___________________________________________________________________________________"
        print" "
        print("__________________________")
        print("| What do you want to do? |")
        print("| 1. Fight {}             ").format(flenemy.name)
        print("| 2. Use item             |")
        print("| 3. Get status of hero   |")
        print("|_________________________|")
        try:
            # raw_input = int(input(" >>"))
            raw_input_s = (input(" >>"))

            if raw_input_s == '':
                print("try again")
                # banner("Please only use integers")
                # fight_sequence(flenemy, hero, backpack)
            else:
                raw_input = int(raw_input_s)
        except ValueError:
            banner("Please only use integers")
            # fight_sequence(flenemy, hero, backpack)
        print()
        if raw_input == 1:
            os.system("clear")
            hero.attack(flenemy)
            if flenemy.alive() == False:
                print" /$$    /$$ /$$$$$$  /$$$$$$  /$$$$$$$$ /$$$$$$  /$$$$$$$  /$$     /$$ "
                print"| $$   | $$|_  $$_/ /$$__  $$|__  $$__//$$__  $$| $$__  $$|  $$   /$$/"
                print"| $$   | $$  | $$  | $$  \__/   | $$  | $$  \ $$| $$  \ $$ \  $$ /$$/ "
                print"|  $$ / $$/  | $$  | $$         | $$  | $$  | $$| $$$$$$$/  \  $$$$/  "
                print" \  $$ $$/   | $$  | $$         | $$  | $$  | $$| $$__  $$   \  $$/   "
                print"  \  $$$/    | $$  | $$    $$   | $$  | $$  | $$| $$  \ $$    | $$    "
                print"   \  $/    /$$$$$$|  $$$$$$/   | $$  |  $$$$$$/| $$  | $$    | $$    "
                print"    \_/    |______/ \______/    |__/   \______/ |__/  |__/    |__/ "
                print"                  ............................"
                print"                  \' The {} is dead.".format(flenemy.name)
                print"                  \'"
                hero.gold += flenemy.gold
                print"                  \' You found {} gold!   ".format(flenemy.gold)
                print"                  ............................"
        elif raw_input == 2:
            os.system("clear")
            print" ______________________________"
            print"| Choose an item number to use |"
            print" ______________________________"
            backpack.sort()
            for i in range(len(backpack)):
                print str(i) + ". " + backpack[i].name
            used = int(input(">>"))
            backpack[used].use(hero, flenemy)
            del backpack[used]
        elif raw_input == 3:
            os.system("clear")
            print(hero)
            print" If your health goes to 0, you die.\nYour max health is the most you can have right now at full streangth.\nYour power is how much damage you deal before armor is involved.\nYour evade is the percentage chance that an attacking enemy will miss you completely.\nEach point of armor will protect you from one point of damage when an enemy attacks you.\noYur fold will be used to buy items in the store."
        elif raw_input == "":
            banner("Invalid input {}, try again: ".format(raw_input))
        else:
            banner("Invalid input {}".format(raw_input))

        if flenemy.alive():
            # Enemy attacks hero
            flenemy.attack(hero)
            if hero.alive() == False:
                print"                   /\ "
                print"                   ||"
                print"                <======>"
                print"                   ||"
                print"                   ||"
                print"                 __||__"
                print"           _____/      \ \_____"
                print"          |  _     ___   _   ||"
                print"          | | \     |   | \  ||"
                print"          | |  |    |   |  | ||"
                print"          | |_/     |   |_/  ||"
                print"          | | \     |   |    ||"
                print"          | |  \    |   |    ||"
                print"          | |   \. _|_. | .  ||"
                print"          |                  ||"
                print"          |    Died a Hero   ||"
                print"  *       | *   **    * **   |**      **"
                print"   \))//\ \/\/.,(//\/\ \./\/\/\||(\ \,\ \,.((//"
                print""
                print"__   __  _____  _     _      _______  ______ _______      ______  _______ _______ ______   "
                print" \_/   |     | |     |      |_____| |_____/ |______      |     \ |______ |_____| |     \  "
                print"  |    |_____| |_____|      |     | |    \_ |______      |_____/ |______ |     | |_____/ ."
                cleanup()                                                                           
                sys.exit()


def store(a, b, c, d, e, f, g, h, i, j, hero, backpack):

    def sure():
        os.system("clear")
        print " __________________________________________"
        print "| Are you sure you want to leave? (Y or N) |"
        print " __________________________________________"
        leave = raw_input(" >>")
        if leave.upper() == "Y":
            return
        elif leave.upper() == "N":
            store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
        elif raw_input == "":
            banner("Invalid input {}, try again: ".format(raw_input))
        else:
            banner("Please enter yes or no. ")
            sure()
        
    def want_to_buy(item, backpack):
        os.system("clear")
        item.pic()
        print item.description
        print " ============================================================================="
        print " _____________________________________ "
        print "| Type \'1\' To buy this item.        |"
        print "| Type \'2\' To go back to the store. |"
        print "| Type \'3\' To exit the store.       |"
        print " _____________________________________ "
        try:
            choice = int(input(">>"))
        except ValueError:
            banner("\nPlease only use integers")
            store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
        if choice == 1:
            os.system("clear")
            if item.count == 0:
                banner("This item is out of stock.")
                store (a, b, c, d, e, f, g, h, i, j, hero, backpack)
            elif hero.gold < item.price:
                banner("You dont have enough gold.")
                store (a, b, c, d, e, f, g, h, i, j, hero, backpack)
            else: 
                item.pack(hero, backpack)
                print"*******************************************************************************"
                print"          |                   |                  |                     |       "
                print" _________|________________.=\"\"_;=.______________|_____________________|_______"
                print"|                   |  ,-\"_,=\"\"     `\"=.|                  |                   "
                print"|___________________|__\"=._o`\"-._        `\"=.______________|___________________"
                print"          |                `\"=._o`\"=._      _`\"=._                     |       "
                print" _________|_____________________:=._o \"=._.\"_.-=\"\'\"=.__________________|_______"
                print"|                   |    __.--\" , ; `\"=._o.\" ,-\"\"\"-._ \".   |                   "
                print"|___________________|_._\"  ,. .` ` `` ,  `\"-._\"-._   \". '__|___________________"
                print"          |           |o`\"=._` , \"` `; .\". ,  \"-._\"-._; ;              |       "
                print" _________|___________| ;`-.o`\"=._; .\" ` '`.\"\` . \"-._ /_______________|_______"
                print"|                   | |o;    `\"-.o`\"=._``  '` \" ,__.--o;   |                   "
                print"|___________________|_| ;     (#) `-.o `\"=.`_.--\"_o.-; ;___|___________________"
                print"____/______/______/___|o;._    \"      `\".o|o_.--\"    ;o;____/______/______/____"
                print"/______/______/______/_\"=._o--._        ; | ;        ; ;/______/______/______/_"
                print"____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____"
                print"/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/_"
                print"____/______/______/______/______/_____\"=.o|o_.--\"\"___/______/______/______/____"
                print"/______/______/______/______/______/______/______/______/______/______/______/_"
                print"*******************************************************************************"
                print "  "
                print("                          You bought " + item.name)
                print "                      \______________________________________/"
                item.count = item.count - 1
                hero.gold -= item.price
                store (a, b, c, d, e, f, g, h, i, j, hero, backpack)
        elif choice == 2:
            os.system("clear")
            store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
        elif choice == 3:
            os.system("clear")
            sure()
        elif raw_input == "":
            banner("Invalid input {}, try again: ".format(raw_input))
        else:
            os.system("clear")
            banner("Invalid input, please try again: ")
            store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
    
    cleanup()
    print"___       __    ______                                 _____            ___________            _____________               ______"
    print"__ |     / /_______  /__________________ ________      __  /______      __  /___  /______      __  ___/__  /__________________  /"
    print"__ | /| / /_  _ \_  /_  ___/  __ \_  __ `__ \  _ \     _  __/  __ \     _  __/_  __ \  _ \     _____ \__  __ \  __ \__  __ \_  / "
    print"__ |/ |/ / /  __/  / / /__ / /_/ /  / / / / /  __/     / /_ / /_/ /     / /_ _  / / /  __/     ____/ /_  / / / /_/ /_  /_/ //_/  "
    print"____/|__/  \___//_/  \___/ \____//_/ /_/ /_/\___/      \__/ \____/      \__/ /_/ /_/\___/      /____/ /_/ /_/\____/_  .___/(_)   "
    print"                ________________________________________________________________________________________           /_/  "
    print"              ( Select a number for an item in the shop to see what it does or to purchase it. Of course )"
    print"              ( this is a buisness so the items arent free. If you dont have enough cash, go kill a     )"
    print"              ( monster or two. I'll have a portal open between each floor.                              )"
    print"                ________________________________________________________________________________________"
    print" "
    print"      $$$$$$$$$$$$$$$"
    print"      $  Gold: {}  $".format(hero.gold)
    print"      $$$$$$$$$$$$$$$"
    print ""
    print ("1. " + str(a) + "\n2. " + str(b) + "\n3. " + str(c) + "\n4. " + str(d) + "\n5. " + str(e) + "\n6. " + str(f) + "\n7. " + str(g) + "\n8. " + str(h) + "\n9. " + str(i) + "\n10. " + str(j) + "\n11. Get Hero Status\n12.  Exit")
    print" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    print " "
    try:
        choice = int(input(">>"))
    except ValueError:
        banner("Please only use integers")
        store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
    if choice == 1:
        want_to_buy(a, backpack)
    elif choice == 2:
        want_to_buy(b, backpack)
    elif choice == 3:
        want_to_buy(c, backpack)
    elif choice == 4:
        want_to_buy(d, backpack)
    elif choice == 5:
        want_to_buy(e, backpack)
    elif choice == 6:
        want_to_buy(f, backpack)
    elif choice == 7:
        want_to_buy(g, backpack)
    elif choice == 8:
        want_to_buy(h, backpack)
    elif choice == 9:
        want_to_buy(i, backpack)
    elif choice == 10:
        want_to_buy(j, backpack)
    elif choice == 11:
        os.system("clear")
        print" _________________"
        print"|                  \ "
        print(hero)
        print"|_________________/"

        store(a, b, c, d, e, f, g, h, i, j, hero, backpack)
    elif choice == 12:
        sure()
    elif raw_input == "":
        banner("Invalid input {}, try again: ".format(raw_input))
    else:
        os.system("clear")
        banner("Invalid input, please try again: ")
        store(a, b, c, d, e, f, g, h, i, j, hero, backpack)


def main():
    print"_        ____  _     __    ___   _   _  ____     _____  ___  "
    print"\ \    /| |_  | |   / /`  / / \ | |\/| | |_       | |  / / \ "
    print" \_\/\/ |_|__ |_|__ \_\_, \_\_/ |_|  | |_|__      |_|  \_\_/  o o o"
    print" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  "
    print"/  ______      _   _                  ______                                      _____                    _            /"
    print"\  | ___ \    | | | |                 |  _  \                                    /  __ \                  | |           \ "
    print"/  | |_/ /   _| |_| |__   ___  _ __   | | | |_   _ _ __   __ _  ___  ___  _ __   | /  \/_ __ __ ___      _| | ___ _ __  /"
    print"\  |  __/ | | | __| '_ \ / _ \| '_ \  | | | | | | | '_ \ / _` |/ _ \/ _ \| '_ \  | |   | '__/ _` \ \ /\ / / |/ _ \ '__| \ "
    print"/  | |  | |_| | |_| | | | (_) | | | | | |/ /| |_| | | | | (_| |  __/ (_) | | | | | \__/\ | | (_| |\ V  V /| |  __/ |    /"
    print"\  \_|   \__, |\__|_| |_|\___/|_| |_| |___/  \__,_|_| |_|\__, |\___|\___/|_| |_|  \____/_|  \__,_| \_/\_/ |_|\___|_|    \ "
    print"/         __/ |                                           __/ |                                                         /"
    print"\        |___/                                           |___/                                                          \ "
    print"/                                                                                                                       / "
    print" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    raw_input("press any key to continue...")
    print"          ____ ____ ____ ____ _  _    ___ _  _ ____    ___  ____ ____ _  _    _ _ _ _ ___  ____ ____ ___      "
    print"          |__/ |___ |__| |    |__|     |  |__| |___    |  \ |__| |__/ |_/     | | | |   /  |__| |__/ |  \     "
    print"          |  \ |___ |  | |___ |  |     |  |  | |___    |__/ |  | |  \ | \_    |_|_| |  /__ |  | |  \ |__/     "
    print"                                                                                                         "
    print"          _ _  _    ___ _  _ ____    ___  ____ ____ ___  ____ ____ ___    ____ _    ____ ____ ____    ____ ____    "
    print"          | |\ |     |  |__| |___    |  \ |___ |___ |__] |___ [__   |     |___ |    |  | |  | |__/    |  | |___    "
    print"          | | \|     |  |  | |___    |__/ |___ |___ |    |___ ___]  |     |    |___ |__| |__| |  \    |__| |      " 
    print"                                                                                                       " 
    print"                                         ___ _  _ ____    _  _ ____ ___  ____    /       "                                                          
    print"                                          |  |__| |___    |\/| |__|   /  |___   /       "                                                           
    print"                                          |  |  | |___    |  | |  |  /__ |___  .       "                                                            
    raw_input("press any key to continue...")  
    print" You are a Hero of DEMACIA, and a DARK Wizard has threatened your homeland. It has been sending hoards of monsters"
    print"  from its layer at the bottom of the dungeon. Reach him and save your kingdom... FOR DEMACIA!"     
    print("Each floor will have a new, stronger combatant. Between each floor a small fairy store will have a portal open to")
    print("sell you items you might need. Can you make it all of the way to the bottom?")
    print "*********************************************************************************************************************************** "
    start = raw_input("Type \'start\' to start the game and take your first steps into the dungeons first floor!:  ")
    if start.upper() == "START": 
        print"\nYou step into the dungeon and see your first monster!"
        os.system("clear")
    else:
        print("I dont care that you didnt stype start. This is a monster game. *The game maker pushes your hero into the dungeon and a monster appears!")
        os.system("clear")
    backpack = []
    floor_count = 1
    thishero = Hero()
    #items
    super_tonic = SuperTonic()
    armor_plate = ArmorPlate()
    holy_hand_grande = HolyHandGrenade()
    nurse = Nurse()
    protien_shake = ProtienShake()
    axe = Axe()
    winchester = Winchester()
    magic_missile_launcher = MagicMissilelauncher()
    lightsaber = LightSaber()
    hire_deadpool = Hire_DeadPool()
    #enemies
    medic = Medic(floor_count)
    shadow = Shadow(floor_count)
    goblin = Goblin(floor_count)
    slime = Slime(floor_count)
    fire_emp = FireEmp(floor_count)
    rock_golem = RockGolem(floor_count)
    dark_wizard = DarkWizard()
    enemy_rotation = [medic, shadow, goblin, slime, fire_emp, rock_golem]


    while floor_count < 25:
        #enemies1   
        medic = Medic(floor_count)
        shadow = Shadow(floor_count)
        goblin = Goblin(floor_count)
        slime = Slime(floor_count)
        fire_emp = FireEmp(floor_count)
        rock_golem = RockGolem(floor_count)
        dark_wizard = DarkWizard()
        #
        enemy_rotation = [medic, shadow, goblin, slime, fire_emp, rock_golem]
        next_enemy = random.randint(0, 5)
        flenemy = enemy_rotation[next_enemy]
        cleanup()
        print"                          +++++++++++++"
        print"                          + Floor #{} +".format(floor_count)
        print"                          +++++++++++++"
        print" "
        fight_sequence(flenemy, thishero, backpack)
        store(super_tonic, holy_hand_grande, armor_plate, nurse, protien_shake, axe, winchester, magic_missile_launcher, lightsaber, hire_deadpool, thishero, backpack)
        floor_count += 1

    cleanup()
    print"                   _______                                          _              _                         "
    print"                  /  _____)                               _        | |         _  (_)                        "
    print"                  | |      ___  ____   ____  ____ _____ _| |_ _   _| | _____ _| |_ _  ___  ____   ___        "
    print"                  | |     / _ \|  _ \ / _  |/ ___|____ (_   _) | | | |(____ (_   _) |/ _ \|  _ \ /___)       "
    print"                  | |____| |_| | | | ( (_| | |   / ___ | | |_| |_| | |/ ___ | | |_| | |_| | | | |___ |       "
    print"                   \______)___/|_| |_|\___ |_|   \_____|  \__)____/ \_)_____|  \__)_|\___/|_| |_(___( )      "
    print"                                     (_____|                                                        |/       "
    print"                                     _                                                  _               _ "
    print"                                    | |                                                | |             | |"
    print"                _   _  ___  _   _   | |__  _____ _   _ _____     ____ _____ _____  ____| |__  _____  __| |"
    print"               | | | |/ _ \| | | |  |  _ \(____ | | | | ___ |   / ___) ___ (____ |/ ___)  _ \| ___ |/ _  |"
    print"               | |_| | |_| | |_| |  | | | / ___ |\ V /| ____|  | |   | ____/ ___ ( (___| | | | ____( (_| |"
    print"                \__  |\___/|____/   |_| |_\_____| \_/ |_____)  |_|   |_____)_____|\____)_| |_|_____)\____|"
    print"               (____/                                                                                     "
    print"                            _                 ___ _             _     _                    _    _                 "
    print"                        _  | |               / __|_)           | |   | |                  | |  | |                "
    print"                      _| |_| |__  _____    _| |__ _ ____  _____| |   | | _____ _   _ _____| |  | |                "
    print"                     (_   _)  _ \| ___ |  (_   __) |  _ \(____ | |   | || ___ | | | | ___ | |  |_|                "
    print"                       | |_| | | | ____|    | |  | | | | / ___ | |   | || ____|\ V /| ____| |   _                 "
    print"                        \__)_| |_|_____)    |_|  |_|_| |_\_____|\_)   \_)_____) \_/ |_____)\_) |_|        "     
    raw_input("press any key to continue...")
    print" "
    print" ______  _     _ _______                                                                                                              "
    print" |_____] |     |    |                                                                                                                 "
    print" |_____] |_____|    |   o o o                                                                                                            "
    print"                                                                                                                                   "
    print" ______  _______ __   _      __   __  _____  _     _      ______  _______ _______ _______ _______ _______      _______ _     _ _______"
    print" |       |_____| | \  |        \_/   |     | |     |      |     \ |______ |______ |______ |_____|    |            |    |_____| |______"
    print" |_____  |     | |  \_|         |    |_____| |_____|      |_____/ |______ |       |______ |     |    |            |    |     | |______  o o o"
    print " "
    print"       ______   _______  _______  _                      _________ _______  _______  _______  _______  ______  "
    print"      (  __  \ (  ___  )(  ____ )| \    /\      |\     /|\__   __// ___   )/ ___   )(  ___  )(  ____ )(  __  \ "
    print"      | (  \  )| (   ) || (    )||  \  / /      | )   ( |   ) (   \/   )  |\/   )  || (   ) || (    )|| (  \  )"
    print"      | |   ) || (___) || (____)||  (_/ /       | | _ | |   | |       /   )    /   )| (___) || (____)|| |   ) |"
    print"      | |   | ||  ___  ||     __)|   _ (        | |( )| |   | |      /   /    /   / |  ___  ||     __)| |   | |"
    print"      | |   ) || (   ) || (\ (   |  ( \ \       | || || |   | |     /   /    /   /  | (   ) || (\ (   | |   ) |"
    print"      | (__/  )| )   ( || ) \ \__|  /  \ \      | () () |___) (___ /   (_/\ /   (_/\| )   ( || ) \ \__| (__/  )"
    print"      (______/ |/     \||/   \__/|_/    \/      (_______)\_______/(_______/(_______/|/     \||/   \__/(______/"
    fight_sequence(dark_wizard, thishero, backpack)
    
    print"YYYYYYY       YYYYYYY          OOOOOOOOO          UUUUUUUU     UUUUUUUU               WWWWWWWW                           WWWWWWWW     IIIIIIIIII     NNNNNNNN        NNNNNNNN      !!!       !!!       !!!  "    
    print"Y:::::Y       Y:::::Y        OO:::::::::OO        U::::::U     U::::::U               W::::::W                           W::::::W     I::::::::I     N:::::::N       N::::::N     !!:!!     !!:!!     !!:!!  "   
    print"Y:::::Y       Y:::::Y      OO:::::::::::::OO      U::::::U     U::::::U               W::::::W                           W::::::W     I::::::::I     N::::::::N      N::::::N     !:::!     !:::!     !:::!   "  
    print"Y::::::Y     Y::::::Y     O:::::::OOO:::::::O     UU:::::U     U:::::UU               W::::::W                           W::::::W     II::::::II     N:::::::::N     N::::::N     !:::!     !:::!     !:::!    " 
    print"YYY:::::Y   Y:::::YYY     O::::::O   O::::::O      U:::::U     U:::::U                 W:::::W           WWWWW           W:::::W        I::::I       N::::::::::N    N::::::N     !:::!     !:::!     !:::!     "
    print"   Y:::::Y Y:::::Y        O:::::O     O:::::O      U:::::D     D:::::U                  W:::::W         W:::::W         W:::::W         I::::I       N:::::::::::N   N::::::N     !:::!     !:::!     !:::!     "
    print"    Y:::::Y:::::Y         O:::::O     O:::::O      U:::::D     D:::::U                   W:::::W       W:::::::W       W:::::W          I::::I       N:::::::N::::N  N::::::N     !:::!     !:::!     !:::!     "
    print"     Y:::::::::Y          O:::::O     O:::::O      U:::::D     D:::::U                    W:::::W     W:::::::::W     W:::::W           I::::I       N::::::N N::::N N::::::N     !:::!     !:::!     !:::!     "
    print"      Y:::::::Y           O:::::O     O:::::O      U:::::D     D:::::U                     W:::::W   W:::::W:::::W   W:::::W            I::::I       N::::::N  N::::N:::::::N     !:::!     !:::!     !:::!     "
    print"       Y:::::Y            O:::::O     O:::::O      U:::::D     D:::::U                      W:::::W W:::::W W:::::W W:::::W             I::::I       N::::::N   N:::::::::::N     !:::!     !:::!     !:::!     "
    print"       Y:::::Y            O:::::O     O:::::O      U:::::D     D:::::U                       W:::::W:::::W   W:::::W:::::W              I::::I       N::::::N    N::::::::::N     !!:!!     !!:!!     !!:!!     "
    print"       Y:::::Y            O::::::O   O::::::O      U::::::U   U::::::U                        W:::::::::W     W:::::::::W               I::::I       N::::::N     N:::::::::N      !!!       !!!       !!!      "
    print"       Y:::::Y            O:::::::OOO:::::::O      U:::::::UUU:::::::U                         W:::::::W       W:::::::W              II::::::II     N::::::N      N::::::::N                                   "
    print"    YYYY:::::YYYY          OO:::::::::::::OO        UU:::::::::::::UU                           W:::::W         W:::::W               I::::::::I     N::::::N       N:::::::N      !!!       !!!       !!!      "
    print"    Y:::::::::::Y            OO:::::::::OO            UU:::::::::UU                              W:::W           W:::W                I::::::::I     N::::::N        N::::::N     !!:!!     !!:!!     !!:!!     "
    print"    YYYYYYYYYYYYY              OOOOOOOOO                UUUUUUUUU                                 WWW             WWW                 IIIIIIIIII     NNNNNNNN         NNNNNNN      !!!       !!!       !!!      "
    cleanup()
    


main()
