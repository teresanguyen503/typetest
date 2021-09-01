import pygame
from pygame.locals import *
from typetest.constants import *
import sys
import time
import random


# 750 x 500    
    
class main:
   
    def __init__(self):
        self.width = width
        self.height = height
        self.reset=True
        self.active = False
        self.input_text=''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time:0 Accuracy:0 % Wpm:0 '
        self.wpm = 0
        self.end = False
        self.HEAD_C = dandelion
        self.TEXT_C = light_grey
        self.RESULT_C = red
        
       
        pygame.init()
        self.open_img = pygame.image.load('openImg.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.width,self.height))

        self.bg = pygame.image.load('charcoal.jpeg')
        self.bg = pygame.transform.scale(self.bg, (750, 500))

        self.window = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption('Testing Words Per Minute')
       
        
    def draw_text(self, screen, msg, y ,fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1,color)
        text_rect = text.get_rect(center=(self.width/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()   
        
    def get_sentence(self):
        f = open('sentences.txt').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence

    def show_results(self, screen):
        if(not self.end):
            #Calculate time
            self.total_time = time.time() - self.time_start
               
            #Calculate accuracy
            count = 0
            for i,c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except:
                    pass
            self.accuracy = count/len(self.word)*100
           
            #Calculate words per minute
            self.wpm = len(self.input_text)*60/(5*self.total_time)
            self.end = True
            print(self.total_time)
                
            self.results = 'Time:'+str(round(self.total_time)) +" secs   Accuracy:"+ str(round(self.accuracy)) + "%" + '   Wpm: ' + str(round(self.wpm))

            # draw icon image
            self.time_img = pygame.image.load('reset.png')
            self.time_img = pygame.transform.scale(self.time_img, (150,150))
            screen.blit(self.time_img, (self.width/2-75,self.height-140))
            self.draw_text(screen,"Reset", self.height - 20, 26, (100,100,100))
            
            print(self.results)
            pygame.display.update()

    def run(self):
        self.reset_game()
    
       
        self.running=True
        while(self.running):
            clock = pygame.time.Clock()
            self.window.fill((0,0,0), (50,250,650,50))
            pygame.draw.rect(self.window,self.HEAD_C, (50,250,650,50), 2)
            # update the text of user input
            self.draw_text(self.window, self.input_text, 274, 26,(250,250,250))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    # position of input box
                    if(x>=50 and x<=650 and y>=250 and y<=300):
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time() 
                     # position of reset box
                    if(x>=310 and x<=510 and y>=390 and self.end):
                        self.reset_game()
                        x,y = pygame.mouse.get_pos()
         
                        
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            print(self.input_text)
                            self.show_results(self.window)
                            print(self.results)
                            self.draw_text(self.window, self.results,350, 28, self.RESULT_C)  
                            self.end = True
                            
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except:
                                pass
            
            pygame.display.update()
             
                
        clock.tick(frame_per_second)

    def reset_game(self):
        self.window.blit(self.open_img, (0,0))

        pygame.display.update()
        time.sleep(1)
        
        self.reset=False
        self.end = False

        self.input_text=''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0

        # Get random sentence 
        self.word = self.get_sentence()
        if (not self.word): self.reset_game()
        #drawing heading
        self.window.fill((0,0,0))
        self.window.blit(self.bg,(0,0))
        msg = "Typing Speed Test"
        self.draw_text(self.window, msg,80, 80,self.HEAD_C)  
        # draw the rectangle for input box
        pygame.draw.rect(self.window,(255,192,25), (50,250,650,50), 2)

        # draw the sentence string
        self.draw_text(self.window, self.word,200, 28,self.TEXT_C)
        
        pygame.display.update()

main().run()

