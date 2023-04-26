'''
handle global settings stuff

TO DO:
Add more settings as stuff is added

'''

# app information
window = None
width = None
height = None
fps = 60

# object information
player = None
map = None
minimap = None
statusBars = None
texFiles = []
spriteFiles = []

# game information
state = None
gameOver = False

# player information
fov = 65
speed = 1.25
sensitivity = 0.75
maxHealth = 100
maxStamina = 100
maxSpecial = 100
damage = 40
knockback = 0.2
attackRange = 1.2
attackAngularRange = 20
attackCooldown = 2.5
maxSpriteDist = 1

# map information
spriteList = []

# enemy information
enemyList = []
enemyHealth = 65
enemySpeed = 0.5
aggroDistance = 5
enemyAttackRange = 1
enemyDamage = 10
enemyStaminaCost = 6
enemyAttackCooldown = 3
enemyKnockback = 0.65