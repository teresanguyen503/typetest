import pygame
from pygame.locals import *
from typetest.constants import *
import sys
import time
import random


# 750 x 500    
    
class main:
   
    def __init__(self):
        self._width = width
        self._height = height
        self._reset=True
        self._active = False
        self._input_text=''
        self._word = ''
        self._time_start = 0
        self._total_time = 0
        self._accuracy = '0%'
        self._results = 'Time:0 Accuracy:0 % Wpm:0 '
        self._wpm = 0
        self._end = False
        self._HEAD_C = dandelion
        self._TEXT_C = light_grey
        self._RESULT_C = red
        
       
        pygame.init()
        self.open_img = pygame.image.load('openImg.png')
        self.open_img = pygame.transform.scale(self.open_img, (self._width,self._height))

        self.bg = pygame.image.load('charcoal.jpeg')
        self.bg = pygame.transform.scale(self.bg, (width, height))

        self.window = pygame.display.set_mode((self._width,self._height))
        pygame.display.set_caption('Testing Words Per Minute')
       
        
    def draw_text(self, screen, msg, y ,fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1,color)
        text_rect = text.get_rect(center=(self._width/2, y))
        screen.blit(text, text_rect)
        pygame.display.update()   
        
    def get_sentence(self):
        f = open('sentences.txt').read()
        sentences = f.split('\n')
        sentence = random.choice(sentences)
        return sentence

    def show_results(self, screen):
        if(not self._end):
            #Calculate time
            self._total_time = time.time() - self._time_start
               
            #Calculate accuracy
            count = 0
            for i,c in enumerate(self._word):
                try:
                    if self._input_text[i] == c:
                        count += 1
                except:
                    pass
            self._accuracy = count/len(self._word)*100
           
            #Calculate words per minute
            self._wpm = len(self._input_text)*60/(5*self._total_time)
            self._end = True
            print(self._total_time)
                
            self._results = 'Time:'+str(round(self._total_time)) +" secs   Accuracy:"+ str(round(self._accuracy)) + "%" + '   Wpm: ' + str(round(self._wpm))

            # draw icon image
            self.time_img = pygame.image.load('reset.png')
            self.time_img = pygame.transform.scale(self.time_img, (150,150))
            screen.blit(self.time_img, (self._width/2-75,self._height-140))
            self.draw_text(screen,"Reset", self._height - 20, 26, (100,100,100))
            
            print(self._results)
            pygame.display.update()

    def run(self):
        self.reset_game()
    
       
        self.running=True
        while(self.running):
            clock = pygame.time.Clock()
            self.window.fill(black, text_input_rect)
            pygame.draw.rect(self.window,self._HEAD_C, text_input_rect, 2)
            # update the text of user input
            self.draw_text(self.window, self._input_text, 274, 26, white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    # position of input box
                    if(x>=50 and x<=650 and y>=250 and y<=300):
                        self._active = True
                        self._input_text = ''
                        self._time_start = time.time() 
                     # position of reset box
                    if(x>=310 and x<=510 and y>=390 and self._end):
                        self.reset_game()
                        x,y = pygame.mouse.get_pos()
         
                        
                elif event.type == pygame.KEYDOWN:
                    if self._active and not self._end:
                        if event.key == pygame.K_RETURN:
                            print(self._input_text)
                            self.show_results(self.window)
                            print(self._results)
                            self.draw_text(self.window, self._results,350, 28, self._RESULT_C)  
                            self._end = True
                            
                        elif event.key == pygame.K_BACKSPACE:
                            self._input_text = self._input_text[:-1]
                        else:
                            try:
                                self._input_text += event.unicode
                            except:
                                pass
            
            pygame.display.update()
             
                
        clock.tick(frame_per_second)

    def reset_game(self):
        self.window.blit(self.open_img, (0,0))

        pygame.display.update()
        time.sleep(1)
        
        self._reset=False
        self._end = False

        self._input_text=''
        self._word = ''
        self._time_start = 0
        self._total_time = 0
        self._wpm = 0

        # Get random sentence 
        self._word = self.get_sentence()
        if (not self._word): self.reset_game()
        #drawing heading
        self.window.fill(black)
        self.window.blit(self.bg,(0,0))
        msg = "Typing Speed Test"
        self.draw_text(self.window, msg,80, 80,self._HEAD_C)  
        # draw the rectangle for input box
        pygame.draw.rect(self.window, light_yellow, text_input_rect, 2)

        # draw the sentence string
        self.draw_text(self.window, self._word,200, 28,self._TEXT_C)
        
        pygame.display.update()

main().run()

