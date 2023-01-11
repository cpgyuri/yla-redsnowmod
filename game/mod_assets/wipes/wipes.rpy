init:
    python:
        def eyewarp(x):
            return x**1.33

    define badendpoem = MultipleTransition([
        False, Dissolve(0.15),
        "mod_assets/wipes/badend1.png", Pause(0.15),
        "mod_assets/wipes/badend2.png", Pause(0.15),
        "mod_assets/wipes/badend3.png", Pause(0.15),
        "mod_assets/wipes/badend4.png", Pause(0.15),
        "mod_assets/wipes/badend5.png", Pause(0.15),
        "mod_assets/wipes/badend6.png", Pause(0.15),
        "mod_assets/wipes/badend7.png", Pause(0.15),
        "mod_assets/wipes/badend8.png", Pause(0.15),
        "mod_assets/wipes/badend7.png", Pause(0.15),
        "mod_assets/wipes/badend8.png", Pause(0.15),
        "mod_assets/wipes/badend7.png", Pause(0.15),
        "mod_assets/wipes/badend8.png", dissolve,
        True])

    $ circlewipe = ImageDissolve("mod_assets/wipes/circlewipe-cw.png", 1.0, 8)
    $ ccirclewipe = ImageDissolve("mod_assets/wipes/circlewipe-ccw.png", 1.0, 8)
    $ bites = ImageDissolve("mod_assets/wipes/bites.png", 1.0, 8)
    $ bowtie = ImageDissolve("mod_assets/wipes/bowtie.png", 1.0, 8)
    $ cmet = ImageDissolve("mod_assets/wipes/cmet.png", 1.0, 8)
    $ cwside = ImageDissolve("mod_assets/wipes/cw-side.png", 1.0, 8)
    $ cwtop = ImageDissolve("mod_assets/wipes/cw-top.png", 1.0, 8)
    $ dots = ImageDissolve("mod_assets/wipes/dots.png", 1.0, 8)
    $ edges = ImageDissolve("mod_assets/wipes/edges.png", 1.0, 8)
    $ flips = ImageDissolve("mod_assets/wipes/flips.png", 1.0, 8)
    $ fur = ImageDissolve("mod_assets/wipes/fur.png", 1.0, 8)
    $ goslow = ImageDissolve("mod_assets/wipes/goslow.png", 5.0, 8)
    $ letter = ImageDissolve("mod_assets/wipes/letter.png", 1.0, 8)
    $ maze = ImageDissolve("mod_assets/wipes/maze.png", 1.0, 8)
    $ radio = ImageDissolve("mod_assets/wipes/radio.png", 1.0, 8)
    $ snake = ImageDissolve("mod_assets/wipes/snake.png", 1.0, 8)
    $ snake2 = ImageDissolve("mod_assets/wipes/snake2.png", 1.0, 8)
    $ snakes = ImageDissolve("mod_assets/wipes/snakes.png", 1.0, 8)
    $ sunshine = ImageDissolve("mod_assets/wipes/sunshine.png", 1.0, 8)
    $ glasswool = ImageDissolve("mod_assets/wipes/glasswool.png", 1.0, 8)
    $ wet = ImageDissolve("mod_assets/wipes/wet.png", 1.0, 8)
    
    $ curtains = ImageDissolve("mod_assets/wipes/curtains.png", 1.0, 8)

    $ snow1 = ImageDissolve("mod_assets/wipes/snow1.png", 1.0, 8)
    $ rain1 = ImageDissolve("mod_assets/wipes/rain1.png", 1.0, 8)
    $ rain2 = ImageDissolve("mod_assets/wipes/rain2.png", 1.0, 8)

    $ puzz = ImageDissolve("mod_assets/wipes/puzz.png", 1.0, 8)
    
    $ shatter = ImageDissolve("mod_assets/wipes/shatter.png", 1.0, 8)
    $ shot = ImageDissolve("mod_assets/wipes/shot.png", 1.0, 8)

    $ roundin = ImageDissolve("mod_assets/wipes/round-in.png", 1.0, 0)
    $ roundout = ImageDissolve("mod_assets/wipes/round-out.png", 1.0, 0)
    $ ringsin = ImageDissolve("mod_assets/wipes/rings-in.png", 1.0, 0)
    $ ringsout = ImageDissolve("mod_assets/wipes/rings-out.png", 1.0, 0)
# unnamed
    $ w1 = ImageDissolve("mod_assets/wipes/1.png", 1.0, 8)
    $ w2 = ImageDissolve("mod_assets/wipes/2.png", 1.0, 8)
    $ w3 = ImageDissolve("mod_assets/wipes/3.png", 1.0, 8)
    $ w4 = ImageDissolve("mod_assets/wipes/4.png", 1.0, 8)
    $ w5 = ImageDissolve("mod_assets/wipes/5.png", 1.0, 8)
    $ w5b = ImageDissolve("mod_assets/wipes/5b.png", 1.0, 8)
    $ w6 = ImageDissolve("mod_assets/wipes/6.png", 1.0, 8)
    $ w7 = ImageDissolve("mod_assets/wipes/7.png", 1.0, 8)
    $ w8 = ImageDissolve("mod_assets/wipes/8.png", 1.0, 8)
    $ w9 = ImageDissolve("mod_assets/wipes/9.png", 1.0, 8)
    $ w10 = ImageDissolve("mod_assets/wipes/10.png", 1.0, 8)
    $ w11 = ImageDissolve("mod_assets/wipes/11.png", 1.0, 8)
    $ w12 = ImageDissolve("mod_assets/wipes/12.png", 1.0, 8)
    $ w13 = ImageDissolve("mod_assets/wipes/13.png", 1.0, 8)
    $ w14 = ImageDissolve("mod_assets/wipes/14.png", 1.0, 8)
    $ w15 = ImageDissolve("mod_assets/wipes/15.png", 1.0, 8)
    $ w16 = ImageDissolve("mod_assets/wipes/16.png", 1.0, 8)
    $ w17 = ImageDissolve("mod_assets/wipes/17.png", 1.0, 8)
    $ w18 = ImageDissolve("mod_assets/wipes/18.png", 1.0, 8)
    $ w19 = ImageDissolve("mod_assets/wipes/19.png", 1.0, 8)
    $ w20 = ImageDissolve("mod_assets/wipes/20.png", 1.0, 8)
    $ w21 = ImageDissolve("mod_assets/wipes/21.png", 1.0, 8)
    $ w22 = ImageDissolve("mod_assets/wipes/22.png", 1.0, 8)
    $ w23 = ImageDissolve("mod_assets/wipes/23.png", 1.0, 8)
    $ w24 = ImageDissolve("mod_assets/wipes/24.png", 1.0, 8)
    $ w25 = ImageDissolve("mod_assets/wipes/25.png", 1.0, 8)
    $ w26 = ImageDissolve("mod_assets/wipes/26.png", 1.0, 8)
    $ w27 = ImageDissolve("mod_assets/wipes/27.png", 1.0, 8)
    $ w28 = ImageDissolve("mod_assets/wipes/28.png", 1.0, 8)

    $ w29 = ImageDissolve("mod_assets/wipes/29.png", 1.0, 8)
    $ w30 = ImageDissolve("mod_assets/wipes/30.png", 1.0, 8)
    $ w31 = ImageDissolve("mod_assets/wipes/31.png", 1.0, 8)
    $ w32 = ImageDissolve("mod_assets/wipes/32.png", 1.0, 8)
    $ w33 = ImageDissolve("mod_assets/wipes/33.png", 1.0, 8)

    $ w34 = ImageDissolve("mod_assets/wipes/34.png", 1.0, 8)
    $ w35 = ImageDissolve("mod_assets/wipes/35.png", 1.0, 8)
    $ w36 = ImageDissolve("mod_assets/wipes/36.png", 1.0, 8)
    $ w37 = ImageDissolve("mod_assets/wipes/37.png", 1.0, 8)

    $ eye = ImageDissolve("mod_assets/wipes/eye.png", 2, ramplen=128, reverse=False, time_warp=eyewarp)
    $ eye2 = ImageDissolve("mod_assets/wipes/eye.png", 2, ramplen=128, reverse=True, time_warp=eyewarp)
    $ eye3 = ImageDissolve("mod_assets/wipes/eye.png", 5, 5)
    $ eye4 = ImageDissolve("mod_assets/wipes/eye.png", 5, 5, ramplen=128, reverse=True, time_warp=eyewarp)
    $ eye_open = ImageDissolve("mod_assets/wipes/eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
    $ eye_shut = ImageDissolve("mod_assets/wipes/eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)
