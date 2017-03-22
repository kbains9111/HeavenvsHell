
from gamelib import *

#sys
game =Game(1280,820,"Project")

#objects
title_bg =Image("images\\heaven_hell_5.jpg",game)
title_bg.resizeTo(game.width,game.height)
bg =Image("images\\heaven_3.png",game)
bg.resizeTo(game.width,game.height)
bg_h =Image("images\\heaven_2.jpg",game)
bg_h.resizeTo(game.width,game.height)
bg_d =Image("images\\hell_3.jpg",game)
bg_d.resizeTo(game.width,game.height)
end_1_bg =Image("images\\hell_2.jpg",game)
end_1_bg.resizeTo(game.width,game.height)
end_2_bg =Image("images\\heaven_4.jpg",game)
end_2_bg.resizeTo(game.width,game.height)

obj_player =Image("images\\angel_2.png",game)

obj_player.rotateBy(90)

obj_rings =[]

obj_points =[]
obj_points3 =[]
obj_points8 =[]
obj_points15 =[]

obj_devils =[]
obj_devils_2 =[]
obj_devils_3 =[]
obj_devils_4 =[]


obj_satan =[]

for d in obj_devils:
    x = randint(10,game.width-10)
    s = randint(1,4)
    d.moveTo(x,-100)
    d.setSpeed(s,180)

#sounds
bgm =Sound("sound\\Desire_Drive_2.wav",1)
sd_dead_sound =Sound("sound\\monster_dead.wav",1)
sd_shooting_sound =Sound("sound\\shooting_star.wav",1)

#set
game_start =0
game.setBackground(bg)

level =1

player_max_hp =50000
player_hp =50000
player_healthRegen =0
player_speed =2
damage =1

attack_delay_full =60
attack_delay =0
shot_speed =10
penetrate =0

healthRegen_D =0
player_max_hp_D =0
damage_D =0
attack_delay_D =0
speed_D =0
shot_speed_D =0
penetrate_D =0
penetrate_price =50
percent_dmg =0

summon_delay =0
level_delay =0
upgrade_delay =0
point =randint(0,20)
remove_delay =0
boss_stage =0
difficulty =1

move_on =0
attack_on =0
upgrade_on =0

obj_dark_missiles =[]
dark_missile_cd =0
satan_attack_cd =0
boss_on =0


ending =1
s_health =666666


#run
while not game.over: 
    game.processInput()
    bgm.play()
    if game_start ==0:
        title_bg.draw()
        game.drawText("Defeat the Satan in level 20.",game.width/2+240,game.height/2-340,Font(black,30,black))
        game.drawText("Upgrade youself with number (1~8).",game.width/2+240,game.height/2-300,Font(black,30,black))
        game.drawText("Challenge higher level......",game.width/2+240,game.height/2-380,Font(black,30,black))
        game.drawText("Press [A] -Easy mode.",game.width/2+180,game.height/2+100,Font(cyan,38,blue))
        game.drawText("Press [S] -Hard mode. ",game.width/2-400,game.height/2+100,Font(red,38,yellow))
        game.drawText("Press [D] -Ultimate God mode. ",game.width/2-200,game.height/2-350,Font(magenta,38,cyan))
        if keys.Pressed[K_a]:
            difficulty =1
            game_start =1
        if keys.Pressed[K_s]:
            difficulty =2
            game_start =1
        if keys.Pressed[K_d]:
            difficulty =3
            game_start =1
    if keys.Pressed[K_SPACE]:
        game_start =1
    if game_start ==1:
        if difficulty ==1:
            game.drawBackground()
        if difficulty ==2:
            bg_h.draw()
        if difficulty ==3:
            bg_d.draw()
            
        obj_player.move()
        if mouse.RightButton:
            move_on =1
            obj_player.moveTowards(mouse,player_speed)
        obj_player.rotateTowards(mouse)
        for d_m in obj_dark_missiles:
            if obj_player.collidedWith(d_m):
                player_hp -=500
        if obj_player.x >=game.width:
            obj_player.x =game.width
        if obj_player.x <=0:
            obj_player.x =0
        if obj_player.y >=game.height:
            obj_player.y =game.height
        if obj_player.y <=0:
            obj_player.y =0

        if attack_delay >=attack_delay_full:
            if mouse.LeftButton:
                attack_on =1
                sd_shooting_sound.play()
                obj_rings.append(   Animation("images\\energyBall_blue.png",30,game,236/5,330/7,2))
                obj_rings[len(obj_rings)-1].moveTo(obj_player.x,obj_player.y)
                obj_rings[len(obj_rings)-1].move()
                obj_rings[len(obj_rings)-1].setSpeed(0,0)
                obj_rings[len(obj_rings)-1].moveTowards(mouse,shot_speed)
                if obj_rings[len(obj_rings)-1].x >=game.width:
                    obj_rings[len(obj_rings)-1].visible =False
                if obj_rings[len(obj_rings)-1].x <=0:
                    obj_rings[len(obj_rings)-1].visible =False
                if obj_rings[len(obj_rings)-1].y >=game.height:
                    obj_rings[len(obj_rings)-1].visible =False
                if obj_rings[len(obj_rings)-1].y <=0:
                    obj_rings[len(obj_rings)-1].visible =False
                attack_delay=0
        for r in obj_rings:
            r.move()                          
        for r in obj_rings:
            if r.x >=game.width:
                r.visible =False
            if r.x <=0:
                r.visible =False
            if r.y >=game.height:
                r.visible =False
            if r.y <=0:
                r.visible =False

        for p in obj_points:
            p.draw()
            if obj_player.collidedWith(p):
                p.visible =False
                point +=1
        for p in obj_points3:
            p.draw()
            if obj_player.collidedWith(p):
                p.visible =False
                point +=3
        for p in obj_points8:
            p.draw()
            if obj_player.collidedWith(p):
                p.visible =False
                point +=8
        for p in obj_points15:
            p.draw()
            if obj_player.collidedWith(p):
                p.visible =False
                point +=15
        if summon_delay >=70:
            obj_devils.append(   Image("images\\devil_1.png",game))
            obj_devils[len(obj_devils)-1].moveTo(randint(10,game.width-10),-20)
            if level <5:
                summon_delay =0
        if level >=5:
            if boss_on ==0 :
                if summon_delay >=70.1:
                    obj_devils_2.append(   Image("images\\devil_2.png",game))
                    obj_devils_2[len(obj_devils_2)-1].moveTo(randint(10,game.width-10),-20)
                    if level <10:
                        summon_delay =0
        if level >=10:
            if boss_on ==0 :
                if summon_delay >=70.2:
                    obj_devils_3.append(   Image("images\\devil_3.png",game))
                    obj_devils_3[len(obj_devils_3)-1].moveTo(randint(10,game.width-10),-20)
                    if level <15:
                        summon_delay =0
        if level >=15:
            if boss_on ==0 :
                if summon_delay >=70.3:
                        obj_devils_4.append(   Image("images\\devil_4.png",game))
                        obj_devils_4[len(obj_devils_4)-1].moveTo(randint(10,game.width-10),-20)
                        summon_delay =0
        if level ==20:
            if boss_stage ==0:
                obj_satan.append(   Image("images\\satan.png",game))
                obj_satan[len(obj_satan)-1].moveTo(game.width/2,game.height/2)
                obj_satan[len(obj_satan)-1].resizeBy(-50)
                boss_stage =1
                boss_on =1
        if boss_on ==1:
            obj_devils =[]
            obj_devils_2 =[]
            obj_devils_3 =[]
            obj_devils_4 =[]
            
        for d in obj_devils:
            for r in obj_rings:
                if r.collidedWith(d):
                    d.damage +=damage
                    if not penetrate >=1:
                        r.visible =False
                    if difficulty ==1:
                        if d.damage >= 1:                       
                            if len(obj_devils) >0:
                                sd_dead_sound.play()
                                obj_devils.remove(d)
                                obj_points.append(  Image("images\\angel_ring.png",game))
                                obj_points[len(obj_points)-1].moveTo(d.x,d.y)
                    if difficulty ==2:
                        if d.damage >= 2:                       
                            if len(obj_devils) >0:
                                sd_dead_sound.play()
                                obj_devils.remove(d)
                                obj_points.append(  Image("images\\angel_ring.png",game))
                                obj_points[len(obj_points)-1].moveTo(d.x,d.y)
                    if difficulty ==3:
                        if d.damage >= 3:                       
                            if len(obj_devils) >0:
                                sd_dead_sound.play()
                                obj_devils.remove(d)
                                obj_points.append(  Image("images\\angel_ring.png",game))
                                obj_points[len(obj_points)-1].moveTo(d.x,d.y)
                

                
                
        for d in obj_devils_2:
            for r in obj_rings:
                if r.collidedWith(d):
                    d.damage +=damage
                    if not penetrate >=2:
                        r.visible =False
                    if difficulty ==1:
                        if d.damage >= 4:
                            if len(obj_devils_2) >0:
                                sd_dead_sound.play()
                                obj_devils_2.remove(d)
                                obj_points3.append(  Image("images\\angel_ring2.png",game))
                                obj_points3[len(obj_points3)-1].moveTo(d.x,d.y)
                    if difficulty ==2:
                        if d.damage >= 6:
                            if len(obj_devils_2) >0:
                                sd_dead_sound.play()
                                obj_devils_2.remove(d)
                                obj_points3.append(  Image("images\\angel_ring2.png",game))
                                obj_points3[len(obj_points3)-1].moveTo(d.x,d.y)
                    if difficulty ==3:
                        if d.damage >= 8:
                            if len(obj_devils_2) >0:
                                sd_dead_sound.play()
                                obj_devils_2.remove(d)
                                obj_points3.append(  Image("images\\angel_ring2.png",game))
                                obj_points3[len(obj_points3)-1].moveTo(d.x,d.y)

        for d in obj_devils_3:
            for r in obj_rings:
                if r.collidedWith(d):
                    d.damage +=damage
                    if not penetrate >=3:
                        r.visible =False
                    if difficulty ==1:
                        if d.damage >= 8:
                            if len(obj_devils_3):
                                sd_dead_sound.play()
                                obj_devils_3.remove(d)
                                obj_points8.append(  Image("images\\angel_ring3.png",game))
                                obj_points8[len(obj_points8)-1].moveTo(d.x,d.y)
                    if difficulty ==2:
                        if d.damage >= 12:
                            if len(obj_devils_3):
                                sd_dead_sound.play()
                                obj_devils_3.remove(d)
                                obj_points8.append(  Image("images\\angel_ring3.png",game))
                                obj_points8[len(obj_points8)-1].moveTo(d.x,d.y)
                    if difficulty ==3:
                        if d.damage >= 16:
                            if len(obj_devils_3):
                                sd_dead_sound.play()
                                obj_devils_3.remove(d)
                                obj_points8.append(  Image("images\\angel_ring3.png",game))
                                obj_points8[len(obj_points8)-1].moveTo(d.x,d.y)
        for d in obj_devils_4:
            for r in obj_rings:
                if r.collidedWith(d):
                    d.damage +=damage
                    if not penetrate >=4:
                        r.visible =False
                    if difficulty ==1:
                        if d.damage >= 14:
                            if len(obj_devils_4):
                                sd_dead_sound.play()
                                obj_devils_4.remove(d)
                                obj_points15.append(  Image("images\\angel_ring4.png",game))
                                obj_points15[len(obj_points15)-1].moveTo(d.x,d.y)
                    if difficulty ==2:
                        if d.damage >= 19:
                            if len(obj_devils_4):
                                sd_dead_sound.play()
                                obj_devils_4.remove(d)
                                obj_points15.append(  Image("images\\angel_ring4.png",game))
                                obj_points15[len(obj_points15)-1].moveTo(d.x,d.y)
                    if difficulty ==3:
                        if d.damage >= 24:
                            if len(obj_devils_4):
                                sd_dead_sound.play()
                                obj_devils_4.remove(d)
                                obj_points15.append(  Image("images\\angel_ring4.png",game))
                                obj_points15[len(obj_points15)-1].moveTo(d.x,d.y)

                
        for s in obj_satan:
            for r in obj_rings:
                if r.collidedWith(s):
                    if percent_dmg ==1:
                        s_health -=s_health/100
                    s_health -=damage
                    r.visible =False
            if s_health <=0:
                s.visible = False

        for d in obj_devils:
            if difficulty ==1:
                d.moveTowards(obj_player,2.5)
            if difficulty ==2:
                d.moveTowards(obj_player,2.7)
            if difficulty ==3:
                d.moveTowards(obj_player,3)
            d.rotateTowards(obj_player)
            if obj_player.collidedWith(d):
                if difficulty ==1:
                    player_hp -=5
                if difficulty ==2:
                    player_hp -=10
                if difficulty ==3:
                    player_hp -=30

        for d in obj_devils_2:
            if difficulty ==1:
                d.moveTowards(obj_player,2.7)
            if difficulty ==2:
                d.moveTowards(obj_player,3)
            if difficulty ==3:
                d.moveTowards(obj_player,3.3)
            d.rotateTowards(obj_player)
            if obj_player.collidedWith(d):
                if difficulty ==1:
                    player_hp -=25
                if difficulty ==2:
                    player_hp -=60
                if difficulty ==3:
                    player_hp -=120

        for d in obj_devils_3:
            if difficulty ==1:
                d.moveTowards(obj_player,3.8)
            if difficulty ==2:
                d.moveTowards(obj_player,4.2)
            if difficulty ==3:
                d.moveTowards(obj_player,4.5)
            d.rotateTowards(obj_player)
            if obj_player.collidedWith(d):
                if difficulty ==1:
                    player_hp -=50
                if difficulty ==2:
                    player_hp -=150
                if difficulty ==3:
                    player_hp -=400
                    
        for d in obj_devils_4:
            if difficulty ==1:
                d.moveTowards(obj_player,5)
            if difficulty ==2:
                d.moveTowards(obj_player,6)
            if difficulty ==3:
                d.moveTowards(obj_player,7)
            d.rotateTowards(obj_player)
            if obj_player.collidedWith(d):
                if difficulty ==1:
                    player_hp -=110
                if difficulty ==2:
                    player_hp -=500
                if difficulty ==3:
                    player_hp -=1200
                
        for s in obj_satan:
            s.moveTowards(obj_player,2)
            if obj_player.collidedWith(s):
                if difficulty ==1:
                    player_hp -=666
                if difficulty ==2:
                    player_hp -=666*2
                if difficulty ==1:
                    player_hp -=6666

                
        if difficulty ==3:
            for i in range(1000):
                i +=1
                if dark_missile_cd ==120 *i:
                        if obj_devils:
                            obj_dark_missiles.append(    Image("images\\dark_missile.png",game))
                            for d in obj_devils:
                                obj_dark_missiles[len(obj_dark_missiles)-1].moveTo(d.x,d.y)
                            obj_dark_missiles[len(obj_dark_missiles)-1].moveTowards(obj_player,4)
                            obj_dark_missiles[len(obj_dark_missiles)-1].rotateTowards(obj_player)
            for d_m in obj_dark_missiles:
                d_m.move()

        if difficulty ==3:
            for i in range(1000):
                i +=1
                if dark_missile_cd ==100 *i:
                        if obj_devils_2:
                            obj_dark_missiles.append(    Image("images\\dark_missile.png",game))
                            for d in obj_devils_2:
                                obj_dark_missiles[len(obj_dark_missiles)-1].moveTo(d.x,d.y)
                            obj_dark_missiles[len(obj_dark_missiles)-1].moveTowards(obj_player,5)
                            obj_dark_missiles[len(obj_dark_missiles)-1].rotateTowards(obj_player)
            for d_m in obj_dark_missiles:
                d_m.move()

        if difficulty ==3:
            for i in range(1000):
                i +=1
                if dark_missile_cd ==80 *i:
                        if obj_devils_3:
                            obj_dark_missiles.append(    Image("images\\dark_missile.png",game))
                            for d in obj_devils_3:
                                obj_dark_missiles[len(obj_dark_missiles)-1].moveTo(d.x,d.y)
                            obj_dark_missiles[len(obj_dark_missiles)-1].moveTowards(obj_player,6)                                                   
                            obj_dark_missiles[len(obj_dark_missiles)-1].rotateTowards(obj_player)
            for d_m in obj_dark_missiles:
                d_m.move()

        if difficulty ==3:
            for i in range(1000):
                i +=1
                if dark_missile_cd ==60 *i:
                        if obj_devils_4:
                            obj_dark_missiles.append(    Image("images\\dark_missile.png",game))
                            for d in obj_devils_4:
                                obj_dark_missiles[len(obj_dark_missiles)-1].moveTo(d.x,d.y)
                            obj_dark_missiles[len(obj_dark_missiles)-1].moveTowards(obj_player,7)
                            obj_dark_missiles[len(obj_dark_missiles)-1].rotateTowards(obj_player)
            for d_m in obj_dark_missiles:
                d_m.move()

        if difficulty ==1:
            for i in range(1000):
                i +=1
                if dark_missile_cd ==60 *i:
                    for n in range(6):
                        if obj_satan:
                            obj_dark_missiles.append(    Image("images\\dark_missile.png",game))
                            for s in obj_satan:
                                obj_dark_missiles[len(obj_dark_missiles)-1].moveTo(s.x,s.y)
                                obj_dark_missiles_angle = n * 60
                                obj_dark_missiles[len(obj_dark_missiles)-1].setSpeed(7,obj_dark_missiles_angle)
                                obj_dark_missiles[len(obj_dark_missiles)-1].rotateTo(obj_dark_missiles_angle-30)
                if dark_missile_cd ==120 *i:
                    for s in obj_satan:
                        for n in range(i):
                            obj_devils_4.append(   Image("images\\devil_4.png",game))
                            obj_devils_4[len(obj_devils_4)-1].moveTo(s.x,s.y)
            for d_m in obj_dark_missiles:
                d_m.move()

        if difficulty ==2:
            for i in range(1000):
                i +=1
                if dark_missile_cd ==60 *i:
                    for n in range(12):
                        if obj_satan:
                            obj_dark_missiles.append(    Image("images\\dark_missile.png",game))
                            for s in obj_satan:
                                obj_dark_missiles[len(obj_dark_missiles)-1].moveTo(s.x,s.y)
                                obj_dark_missiles_angle = n * 30
                                obj_dark_missiles[len(obj_dark_missiles)-1].setSpeed(9,obj_dark_missiles_angle)
                                obj_dark_missiles[len(obj_dark_missiles)-1].rotateTo(obj_dark_missiles_angle-30)
            for d_m in obj_dark_missiles:
                d_m.move()

        if difficulty ==3:
            for i in range(1000):
                i +=1
                if dark_missile_cd ==60*i:
                    for n in range(18):
                        if obj_satan:
                            obj_dark_missiles.append(    Image("images\\dark_missile.png",game))
                            for s in obj_satan:
                                obj_dark_missiles[len(obj_dark_missiles)-1].moveTo(s.x,s.y)
                                obj_dark_missiles_angle = n * 20
                                obj_dark_missiles[len(obj_dark_missiles)-1].setSpeed(14,obj_dark_missiles_angle)
                                obj_dark_missiles[len(obj_dark_missiles)-1].rotateTo(obj_dark_missiles_angle-30)
            for d_m in obj_dark_missiles:
                d_m.move()

        
        if difficulty ==3:
            if len(obj_dark_missiles):
                if d_m in obj_dark_missiles:
                    if d_m.x <=0:
                        d_m.visible =False
                    if d_m.x >=game.width:
                        d_m.visible =False
                    if d_m.y <=0:
                        d_m.visible =False
                    if d_m.y >=game.height:
                        d_m.visible =False
                    
        
        if upgrade_delay >=10:
            if keys.Pressed[K_1]:
                if point >=4:
                    point -=4
                    player_max_hp +=5000
                    player_max_hp_D +=1
                    upgrade_delay =0
                    upgrade_on =1

        if upgrade_delay >=10:
            if keys.Pressed[K_2]:
                if point >=10:
                    point -=10
                    player_healthRegen +=1
                    healthRegen_D+=1
                    upgrade_delay =0
                    upgrade_on =1

        if upgrade_delay >=10:
            if keys.Pressed[K_3]:
                if point >=20:
                    point -=20
                    damage +=1
                    damage_D +=1
                    upgrade_delay =0
                    upgrade_on =1

        if upgrade_delay >=10:
            if keys.Pressed[K_4]:
                if attack_delay_D <10:
                    if point >=5:
                        point -=5
                        attack_delay_full -=5
                        attack_delay_D +=1
                        upgrade_delay =0
                        upgrade_on =1

        if upgrade_delay >=10:
            if keys.Pressed[K_5]:
                if point >=3:
                    point -=3
                    shot_speed +=1
                    shot_speed_D +=1
                    upgrade_delay =0
                    upgrade_on =1

        if upgrade_delay >=10:
            if keys.Pressed[K_6]:
                if player_speed <5:
                    if point >=10:
                        point -=10
                        player_speed +=1
                        speed_D +=1
                        upgrade_delay =0
                        upgrade_on =1

        if upgrade_delay >=10:
            if keys.Pressed[K_7]:
                if penetrate <4:
                    if point >=penetrate_price:
                        point -=penetrate_price
                        penetrate +=1
                        penetrate_D +=1
                        upgrade_delay =0
                        upgrade_on =1

        if upgrade_delay >=10:
            if keys.Pressed[K_8]:
                if percent_dmg <1:
                    if point >=500:
                        point -=500
                        percent_dmg =1
                        upgrade_delay =0
                        upgrade_on =1

        if keys.Pressed[K_p]:
            if level_delay >=15:
                level_delay =0
                level +=1
        #if keys.Pressed[K_0]:
            #point +=1000
            
        attack_delay +=1
        if difficulty ==1:
            summon_delay +=level/5
        else:
            summon_delay +=level/6
            
            
        level_delay +=1
        upgrade_delay +=1
        remove_delay +=1
        player_hp +=player_healthRegen

        if keys.Pressed[K_r]:
            game_start =0
            power =0
            level =1
            player_max_hp =50000
            player_hp =50000
            player_healthRegen =0
            damage =1
            shot_speed =10
            player_speed =2
            penetrate =0

            player_max_hp_D =0
            healthRegen_D =0
            damage_D =0
            attack_delay_D =0
            shot_speed_D =0
            speed_D =0
            penetrate_D =0
            penetrate_price =50
            percent_dmg =0
            
            attack_delay_full =60
            attack_delay =0
            summon_delay =0

            level_delay =0
            point =randint(0,20)
            
            obj_devils =[]
            obj_devils_2 =[]
            obj_devils_3 =[]
            obj_devils_4 =[]
            obj_satan =[]
            obj_dark_missiles =[]
            
            move_on =0
            attack_on =0
            upgrade_on =0

        if player_hp >player_max_hp:
            player_hp =player_max_hp
        if player_hp <=0:
            game.over =True
            ending =1
        if s_health <=1:
            game.over =True
            ending =2
        dark_missile_cd +=1
        satan_attack_cd +=1
        penetrate_price = (penetrate+1) *50
        game.drawText("HP : " +str(player_hp),obj_player.x-50,obj_player.y-60,Font(red,40,yellow))
        game.drawText("Power : "+str(point),20,45,Font(green,40,black))
        if difficulty ==1:
            game.drawText("Level : "+str(level),20,20,Font(blue,40,black))
        if difficulty ==2 or 3:
            game.drawText("Level : "+str(level),20,20,Font(red,40,green))
        if difficulty ==1 or 2:
            game.drawText("Max Health[1](4) : "+str(player_max_hp_D),game.width-260,20,Font(black,28,red))
            game.drawText("Health Regen[2](10) : "+str(healthRegen_D),game.width-260,40,Font(black,28,red))
            game.drawText("Damage[3](20) : "+str(damage_D),game.width-260,60,Font(black,28,red))
            game.drawText("Shooting Speed[4](5) : "+str(attack_delay_D),game.width-260,80,Font(black,28,red))
            game.drawText("Shot Speed[5](3) : "+str(shot_speed_D),game.width-260,100,Font(black,28,red))
            game.drawText("Speed[6](10) : "+str(speed_D),game.width-260,120,Font(black,28,red))
            game.drawText("Penetrate[7](%s) : "%(penetrate_price)+str(penetrate_D),game.width-260,140,Font(black,28,red))
            game.drawText("Percent Damage[8](500) : "+str(percent_dmg),game.width-260,160,Font(black,28,red))
            #game.drawText("create(60): " +str(summon_delay),700,400)
            #game.drawText("Difficulty: " +str(difficulty),800,700,Font(black,50,red))
        if difficulty ==3:
            game.drawText("Max Health[1](4) : "+str(player_max_hp_D),game.width-260,20,Font(cyan
                                                                                            ,28,red))
            game.drawText("Health Regen[2](10) : "+str(healthRegen_D),game.width-260,40,Font(cyan,28,red))
            game.drawText("Damage[3](20) : "+str(damage_D),game.width-260,60,Font(cyan,28,red))
            game.drawText("Shooting Speed[4](5) : "+str(attack_delay_D),game.width-260,80,Font(cyan,28,red))
            game.drawText("Shot Speed[5](3) : "+str(shot_speed_D),game.width-260,100,Font(cyan,28,red))
            game.drawText("Speed[6](10) : "+str(speed_D),game.width-260,120,Font(cyan,28,red))
            game.drawText("Penetrate[7](%s) : "%(penetrate_price)+str(penetrate_D),game.width-260,140,Font(cyan,28,red))
            game.drawText("Percent Damage[8](500) : "+str(percent_dmg),game.width-260,160,Font(cyan,28,red))
            #game.drawText("create(60): " +str(summon_delay),700,400)
            #game.drawText("Difficulty: " +str(difficulty),800,700,Font(black,50,red))
        if level  ==1:
            game.drawText("Press [P] to level up" ,20,80,Font(red,50,blue))
            game.drawText("Upgrade[NUMBER](COST)",20,120,Font(red,50,blue))
        if move_on ==0:
            game.drawText("Move : Mouse Right Button",game.width/2-100,game.height/2-150,Font(black,36,black))
        if attack_on ==0:
            game.drawText("Attack : Mouse Left Button",game.width/2-100,game.height/2,Font(black,36,black))
        if upgrade_on ==0:
            game.drawText("Upgrade : 1 ~ 9 Number",game.width/2-100,game.height/2+150,Font(black,36,black))
        for s in obj_satan:
            if boss_stage ==1:
                game.drawText("Satan : " +str(s_health),s.x-80,s.y-100,Font(yellow,32,red))
    if difficulty ==1 or 2:
        game.update(60)
    if difficulty ==3:
        game.update(1800)
    
#ending
if ending ==1:
    end_1_bg.draw()
    game.drawText("Heaven has Fallen...",game.width/2 -220,game.height/2-150,Font(magenta,60,black))
if ending ==2:
    end_2_bg.draw()
    if difficulty ==1:
        game.drawText("You protected Heaven from devils. !!",game.width/2 -250,game.height/2-150,Font(cyan,60,magenta))
    if difficulty ==2:
        game.drawText("You protected Heaven from satan. !",game.width/2 -250,game.height/2-150,Font(black,70,magenta))
    if difficulty ==3:
        game.drawText("You protected Heaven from Ultimate Great King Satan.!!!",game.width/2 -250,game.height/2-150,Font(red,80,magenta))
        
game.drawText("Press [SPACE] To end Game.",game.width/2-250,game.height/2+200,Font(blue,60,red))
game.update(1)
game.wait(K_SPACE)
game.quit()

