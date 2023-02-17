import pygame
import random

class Warrior():
    def __init__(self, x, y, data, sprite_sheet, animation_steps):
      self.size = data[0]
      self.flip = False
      self.animation_list = self.load_images(sprite_sheet, animation_steps)
      self.rect = pygame.Rect((x, y, 80, 180))
      self.attacking = False
      self.atk_type = 0
      self.health = 100


    #load images (warrior, tanker)
    def load_images(self, sprite_sheet, animation_steps):
      
      #extract images from spritesheet
      animation_list = []
      for y, animation in enumerate(animation_steps):
        temp_img_list = []
        for x in range(animation):
          temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
          temp_img_list.append(temp_img)
        animation_list.append(temp_img_list)
      return animation_list


      
    
      

    def move(self, screen_width, scree_height, surface, target):
      SPEED = 10
      dx = 0
      dy = 0

      #get keypresses
      key = pygame.key.get_pressed()
      
      #can only perform other actions if not currently attacking
      if self.attacking == False:
        
        

      #movement
        if key[pygame.K_a]:
          dx = -SPEED
        if key[pygame.K_d]:
          dx = SPEED
      #attack
        if key[pygame.K_w]:
          self.attack(surface, target)

        #determine which attack type was used
          if key[pygame.K_w]:
            self.attack_type = random.randint(1, 10)
            #self.defense_type = random.randint(5, 15)### need make defense
    

  

      #ensure player stays on screen
      if self.rect.left + dx < 0:
        dx = -self.rect.left
      if self.rect.right + dx > screen_width:
        dx = screen_width - self.rect.right
     
      #ensure players face each other
      if target.rect.centerx > self.rect.centerx:
        self.flip = False
      else:
        self.flip = True

      #update player position
      self.rect.x += dx
      self.rect.y += dy


    def attack(self, surface, target):
      self.attacking = True
      attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
      if attacking_rect.colliderect(target.rect):
        target.health -= 10

    

      pygame.draw.rect(surface, (0, 255,0), attacking_rect)


    
    def draw(self, surface):
      pygame.draw.rect(surface, (255, 0, 0), self.rect)
    
  