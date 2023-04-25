'''
handle global settings stuff

TO DO:
Add more settings as stuff is added

'''

# app information
width = None
height = None
fps = 60

# game information
player = None
map = None
minimap = None
statusBars = None
gameOver = False

# player information
fov = 65
speed = 1.5
sensitivity = 0.75
maxHealth = 100
maxStamina = 100
maxSpecial = 100
damage = 60
knockback = 0.3
attackRange = 1.2
attackCooldown = 2.5

# map information
spriteList = []

# enemy information
enemyList = []
enemyHealth = 65
enemySpeed = 1
aggroDistance = 5
enemyAttackRange = 1
enemyDamage = 3.7
enemyStaminaCost = 6
enemyAttackCooldown = 3
enemyKnockback = 0.5