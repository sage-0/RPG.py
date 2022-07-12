import random



print("="*20)
print("Welcome to the world of RPG!")
print("="*20)



#味方パラメータ
pl_name = ["勇者", "弟子"]
pl_lv = [random.randint(0, 500), random.randint(0, 500)]
pl_hp = [random.randint(0, 100), random.randint(0, 100)]
#敵パラメータ
en_name = ["ドラゴン", "魔王"]
en_lv = [random.randint(0, 500), random.randint(0, 500)]
en_hp = [random.randint(0, 100), random.randint(0, 100)]


#ゲーム情報
def info(p_name,e_name,p_lv,e_lv,p_hp,e_hp):
    print("*"*20)
    print("プレイヤー情報")
    print("*"*20)
    print(f"味方: {p_name[0],p_name[1]}")
    print(f"レベル: {p_lv[0],p_lv[1]}")
    print(f"HP: {p_hp[0],p_hp[1]}")
    print("")
    print("敵情報: ")
    print("*"*20)
    print(f"敵: {e_name[0],e_name[1]}")
    print(f"レベル: {e_lv[0],e_lv[1]}")
    print(f"HP: {e_hp[0],e_hp[1]}")
    print("*"*20)
    print("="*20)
    print("")

print(info(pl_name,en_name,pl_lv,en_lv,pl_hp,en_hp))



#攻撃倍率計算
def level_difference(p_lv, e_lv):
     if p_lv > e_lv:
         print("勇者のレベルが高いため、攻撃力が上がりました")
         hitmag = 0.2*(p_lv - e_lv)
         kaisin = random.randint(0, int(hitmag))
         if kaisin > 5:
             print(f"会心の一撃！: {kaisin}")
             hitmag = 10
         return hitmag
     elif (p_lv - e_lv) < 20:
        hitmag = 0.2
        return hitmag
def en_level_difference(p_lv, e_lv):
     if p_lv < e_lv:
         print("敵のレベルが高いため、敵の攻撃力上がりました")
         e_hitmag = 0.2*(e_lv - p_lv)
         return e_hitmag
     elif (p_lv[0] - en_lv[0]) < 20 and (p_lv[1] - e_lv[1]) < 20:
        e_hitmag = 0.2
        return e_hitmag

#攻撃
def attak(attak_com):
    en_aut_attak = random.randint(0, 1)
    en_tyois = random.randint(0, 1)
    level = level_difference(pl_lv[attak_com], en_lv[en_aut_attak])
    if attak_com == 0:
        print("ドラゴンに攻撃した")
        en_hp[attak_com] -= level
    if en_aut_attak == 0:
        if en_tyois == 0:
            print("勇者はドラゴンから攻撃を受けた")
            pl_hp[en_aut_attak] -= level
        else:
            print("勇者は魔王から攻撃を受けた")
            pl_hp[en_aut_attak] -= level
    else:
        print("魔王に攻撃した")
        en_hp[attak_com] -= level
        if en_tyois == 0:
            print("弟子はドラゴンから攻撃を受けた")
            pl_hp[en_aut_attak] -= level
        else:
            print("弟子は魔王から攻撃を受けた")
            pl_hp[en_aut_attak] -= level
    # else:
    #     print("魔王に攻撃した")
    #     attak_p = level_difference(pl_lv[aut_attak], en_lv[aut_attak])
    #     en_hp[aut_attak] -= attak_p
    #     en_attak_p = level_difference(pl_lv[aut_attak], en_lv[aut_attak])
    #     pl_hp[aut_attak] -= en_attak_p
    #     print(f"魔王から攻撃された {level_difference(pl_lv[aut_attak], en_lv[aut_attak])}")
    #     return attak_p, en_attak_p

while True:
    human = int(input("0: ドラゴン, 1: 魔王"))
    attak(human)
    if en_hp[0] <= 0:
            print("勇者はドラゴンを倒した:")
            info(pl_name,en_name,pl_lv,en_lv,pl_hp,en_hp)
            break
    if pl_hp[0] <= 0:
            print("勇者は死んでしまった")
            info(pl_name,en_name,pl_lv,en_lv,pl_hp,en_hp)
            break
    if pl_hp[1] <= 0:
            print("弟子は死んでしまった")
            info(pl_name,en_name,pl_lv,en_lv,pl_hp,en_hp)
            break
    info(pl_name,en_name,pl_lv,en_lv,pl_hp,en_hp)
