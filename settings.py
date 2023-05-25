'''
handle global settings
'''

# app information
window = None
width = None
height = None
uiScale = None
fps = 60

# object information
player = None
map = None
minimap = None
statusBars = None
texFiles = []
spriteFiles = []
sfxFiles = []
musicFiles = []
musicPlayer = None

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
attackRange = 1.5
attackAngularRange = 20
attackCooldown = 1.5
maxSpriteDist = 1

# map information
spriteList = []

# enemy information
enemyList = []
enemyHealth = 65
enemySpeed = 0.5
aggroDistance = 4
enemyAttackRange = 1
enemyDamage = 5
enemyStaminaCost = 6
enemyAttackCooldown = 3
enemyKnockback = 0.65

# sound information
footstepInterval = 0.4
enemySnarlFrequency = 5.5