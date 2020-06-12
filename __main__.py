from typing import List
import time
import os

sprites: List[str] = [
    '''
                               _.-~ -       
                    _..--~~~~,'   ,-|     _ 
                 .-'. . . .'   ,-','    ,' |
               ,'. . . _   ,--~,-'__..-'  ,'
             ,'. . .  (@)' ---~~~~      ,'  
            .. . . . '~~             ,-'    
           .. . . . .             ,-'       
          ; . . . .  - .        ,'          
         : . . . .       _     .            
        . . . . .          `-.:             
       . . . .  - .          |              
      .  . . |  _____..---..__|             
.   . ~.                       .--.    . `  
    ''',
    '''
                                            
                               _.-~ -       
                    _..--~~~~,'   ,-|    _  
                 .-'. . . .'   ,-','   ,' | 
               ,'. . . _   ,--~,-'__.-' ,'  
             ,'. . .  (-)' ---~~~~     ,'   
            .. . . . '~~             ,'     
           .. . . . .             ,-'       
          ; . . . .  - .        ,'          
        . . . . .        _    .             
       . . . .  - .        `-.              
      .  . . |  _____.......__|            .
`   . ~.                       .--.      `  
    ''',
    '''
                                            
                                            
                               _.-~ -       
                    _..--~~~~,'   ,-|   _   
                 .-'. . . .'   ,-','  ,' |  
               ,'. . . _   ,--~,-'__..  ,'  
             ,'. . .  >< ' ---~~~~    ,'    
            .. . . . '~~            .       
           .. . . . .             ,-        
          ; . . . .  - .        ,'          
  `      . . . .  - .      _    .           
 .  ` .  . . |  _____....__`-.      `.      
    . ~.                       .-`.      .  
    ''',
    '''
                                            
                                            
                               _.-~ -       
                    _..--~~~~,'   ,-|  _    
                 .-'. . . .'   ,-',' ,' |   
               ,'. . . _   ,--~,-'_..  ,    
             ,'. . .  >< ' ---~~~~   ,'     
            .. . . . '~~            .       
           .. . . . .             ,         
   `.     ; . . . .  - .        ,'        .`
        . . . .  - .      _    .       .    
.     .  . . |  _____....__`-.              
    . ~.                       .-`.   .  .  
    ''',
    '''
                                            
                                            
                               _.-~ -       
                    _..--~~~~,'   ,-|   _   
                 .-'. . . .'   ,-','  ,' |  
               ,'. . . _   ,--~,-'__..  ,'  
             ,'. . .  >< ' ---~~~~    ,'    
            .. . . . '~~            .       
           .. . . . .             ,-        
          ; . . . .  - .        ,'          
  `      . . . .  - .      _    .           
 .  ` .  . . |  _____....__`-.      `.      
    . ~.                       .-`.      .  
    ''',
    '''
                                            
                               _.-~ -       
                    _..--~~~~,'   ,-|    _  
                 .-'. . . .'   ,-','   ,' | 
               ,'. . . _   ,--~,-'__.-' ,'  
             ,'. . .  (-)' ---~~~~     ,'   
            .. . . . '~~             ,'     
           .. . . . .             ,-'       
          ; . . . .  - .        ,'          
        . . . . .        _    .             
       . . . .  - .        `-.              
      .  . . |  _____.......__|            .
`   . ~.                       .--.      `  
    ''',
]

bg: str = '''
𝓙𝓸𝓬𝓮𝓵𝓪𝓲𝓷𝓰
'''


def invert(sprite: str) -> str:
    return (
        '\n'.join([line[::-1] for line in sprite.split('\n')])
        .replace(')@(', '(@)')
        .replace(')-(', '(-)')
        .replace('<>', '><')
    )


def translate(sprite: str, sp: int) -> str:
    return '\n'.join(
        [' '.join(['' for __ in range(sp)]) + _ for _ in sprite.split('\n')]
    )


def draw(sprite: str, bg: str, v: float) -> None:
    print(sprite + bg)
    time.sleep(v)
    os.system('clear')


def animate(*, sprites: List[str], background: str, speed: float) -> None:
    i: int = 0
    j: int = 0
    k: int = 0
    d: int = 30
    sprite: str = None
    inv: bool = False

    while True:
        i = i % len(sprites)
        j = j % d
        inv = not inv if not j else inv
        sprite = sprites[i] if inv else invert(sprites[i])
        sprite = translate(sprite, k)

        draw(sprite, background, speed)

        j += 1
        i += 1
        k += 1 if inv else -1


animate(sprites=sprites, background=bg, speed=0.1)
