import sys
import pygame as pg

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    img = pg.image.load("ex01/fig/3.png")
    img = pg.transform.flip(img,True,False)
    imgs = [img, pg.transform.rotozoom(img,10,1.0)]
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img_r = pg.transform.flip(bg_img,True,False)
    tmr = 0
    bg_imgs=[bg_img,bg_img_r,bg_img,bg_img_r]

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        for i in range(4):
            screen.blit(bg_imgs[0],[-tmr,0])
            screen.blit(bg_imgs[1],[1600-tmr,0])
            screen.blit(bg_imgs[2],[3200-tmr,0])
            screen.blit(bg_imgs[3],[4800-tmr,0])
        screen.blit(imgs[(tmr//50)%2], [300,200])
        
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()