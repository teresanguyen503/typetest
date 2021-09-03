import pygame
from pygame.locals import *
from typetest.constants import *
import sys
import time
import random
 
    
class main:
   
    def __init__(self):
        self._width = width
        self._height = height
        self._reset = True
        self._active = False
        self._input_text = ""
        self._word = ""
        self._time_start = 0
        self._total_time = 0
        self._accuracy = "0%"
        self._results = "Time: 0 Accuracy: 0 % WPM: 0"
        self._wpm = 0
        self._end = False
        self._header = aquamarine
        self._text = white
        self._result = bisque
        
       
        pygame.init()
        self._open_img = pygame.image.load('openImg.png')
        self._open_img = pygame.transform.scale(self._open_img, (self._width, self._height))

        self._background = pygame.image.load('charcoal.jpeg')
        self._background = pygame.transform.scale(self._background, (width, height))

        self._window = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption('Testing Words Per Minute')
       
        
    def _draw_text(self, screen, msg, y ,fsize, color):
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
            # Time 
            self._total_time = time.time() - self._time_start
               
            # Accuracy
            count = 0
            for i,c in enumerate(self._word):
                try:
                    if self._input_text[i] == c:
                        count += 1
                except:
                    pass
            self._accuracy = count/len(self._word)*100
           
            # WPM
            self._wpm = len(self._input_text) * 60 / (5 * self._total_time)
            self._end = True
            print(self._total_time)
                
            self._results = "Time: " + str(round(self._total_time)) + " seconds   Accuracy: " + str(round(self._accuracy)) + "%" + "   WPM: " + str(round(self._wpm))

            # reset
            self._reset_image = pygame.image.load('reset.png')
            self._reset_image = pygame.transform.scale(self._reset_image, (75, 75))
            screen.blit(self._reset_image, (self._width / 2 - 35, self._height - 100))
            self._draw_text(screen, "Reset", self._height - 35, 25, black)
            
            print(self._results)
            pygame.display.update()

    def run(self):
        self._reset_game()
    
        self._running = True
        while(self._running):
            clock = pygame.time.Clock()
            self._window.fill(black, text_input_rect)
            pygame.draw.rect(self._window,self._header, text_input_rect, 2)
            # update user input 
            self._draw_text(self._window, self._input_text, 274, 26, white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self._running = False
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x,y = pygame.mouse.get_pos()
                    # input 
                    if(x >= 50 and x <= 800 and y >= 250 and y <= 300):
                        self._active = True
                        self._input_text = ""
                        self._time_start = time.time() 
                     # reset 
                    if(x >= 310 and x <= 510 and y >= 390 and self._end):
                        self._reset_game()
                        x,y = pygame.mouse.get_pos()
         
                        
                elif event.type == pygame.KEYDOWN:
                    if self._active and not self._end:
                        if event.key == pygame.K_RETURN:
                            print(self._input_text)
                            self.show_results(self._window)
                            print(self._results)
                            self._draw_text(self._window, self._results, 350, 28, self._result)  
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

    def _reset_game(self):
        self._window.blit(self._open_img, (0,0))

        pygame.display.update()
        time.sleep(1)
        
        self._reset = False
        self._end = False

        self._input_text = ""
        self._word = ""
        self._time_start = 0
        self._total_time = 0
        self._wpm = 0

        # Get random sentence 
        self._word = self.get_sentence()
        if (not self._word): self._reset_game()
        # heading 
        self._window.fill(black)
        self._window.blit(self._background, (0,0))
        message = "Type Fast and Accurately!!!"
        self._draw_text(self._window, message, 80, 80, self._header)  
        # input box 
        pygame.draw.rect(self._window, aquamarine, text_input_rect, 2)

        # sentence
        self._draw_text(self._window, self._word, 200, 28, self._text)
        
        pygame.display.update()

main().run()


