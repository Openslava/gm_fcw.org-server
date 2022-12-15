
[spec]

; Format and options of this spec file: 
options = "+Freeciv-spec-Devel-2019-Jul-03"

[info]

artists = "
    Tatu Rissanen <tatu.rissanen@hut.fi>
    Jeff Mallatt <jjm@codewell.com> (miscellaneous)
"

[file]
gfx = "amplio2/tiles"

[grid_main]

x_top_left = 1
y_top_left = 1
dx = 96
dy = 48
pixel_border = 1

tiles = { "row", "column", "tag"
; Unit hit-point bars: approx percent of hp remaining

  0,  0, "unit.hp_100"
  0,  1, "unit.hp_90"
  0,  2, "unit.hp_80"
  0,  3, "unit.hp_70"
  0,  4, "unit.hp_60"
  0,  5, "unit.hp_50"
  0,  6, "unit.hp_40"
  0,  7, "unit.hp_30"
  0,  8, "unit.hp_20"
  0,  9, "unit.hp_10"
  0, 10, "unit.hp_0"

  8,  0, "unit.hp_95"
  8,  1, "unit.hp_85"
  8,  2, "unit.hp_75"
  8,  3, "unit.hp_65"
  8,  4, "unit.hp_55"
  8,  5, "unit.hp_45"
  8,  6, "unit.hp_35"
  8,  7, "unit.hp_25"
  8,  8, "unit.hp_15"
  8,  9, "unit.hp_5"

; Numbers: city size: (also used for goto)

  1,  0, "city.size_000"
  1,  1, "city.size_100"
  1,  2, "city.size_200"
  1,  3, "city.size_300"
  1,  4, "city.size_400"
  1,  5, "city.size_500"
  1,  6, "city.size_600"
  1,  7, "city.size_700"
  1,  8, "city.size_800"
  1,  9, "city.size_900"

  2, 0, "city.size_00"
  2, 1, "city.size_10"
  2, 2, "city.size_20"
  2, 3, "city.size_30"
  2, 4, "city.size_40"
  2, 5, "city.size_50"
  2, 6, "city.size_60"
  2, 7, "city.size_70"
  2, 8, "city.size_80"
  2, 9, "city.size_90"

  3,  0, "city.size_0"
  3,  1, "city.size_1"
  3,  2, "city.size_2"
  3,  3, "city.size_3"
  3,  4, "city.size_4"
  3,  5, "city.size_5"
  3,  6, "city.size_6"
  3,  7, "city.size_7"
  3,  8, "city.size_8"
  3,  9, "city.size_9"

; Numbers: city tile food/shields/trade y/g/b

  4,  0, "city.t_food_0"
  4,  1, "city.t_food_1"
  4,  2, "city.t_food_2"
  4,  3, "city.t_food_3"
  4,  4, "city.t_food_4"
  4,  5, "city.t_food_5"
  4,  6, "city.t_food_6"
  4,  7, "city.t_food_7"
  4,  8, "city.t_food_8"
  4,  9, "city.t_food_9"

  5,  0, "city.t_shields_0"
  5,  1, "city.t_shields_1"
  5,  2, "city.t_shields_2"
  5,  3, "city.t_shields_3"
  5,  4, "city.t_shields_4"
  5,  5, "city.t_shields_5"
  5,  6, "city.t_shields_6"
  5,  7, "city.t_shields_7"
  5,  8, "city.t_shields_8"
  5,  9, "city.t_shields_9"

  6, 0, "city.t_trade_0"
  6, 1, "city.t_trade_1"
  6, 2, "city.t_trade_2"
  6, 3, "city.t_trade_3"
  6, 4, "city.t_trade_4"
  6, 5, "city.t_trade_5"
  6, 6, "city.t_trade_6"
  6, 7, "city.t_trade_7"
  6, 8, "city.t_trade_8"
  6, 9, "city.t_trade_9"

; Server sends back a single numeral/char for tile output, previously limiting us to 0-9, 
; which fails in cases like gold+river+colossus+democracy+superhighway (6+3)*1.5 = 13
  7, 0, "city.t_trade_A"  ; 10
  7, 1, "city.t_trade_B"  ; 11
  7, 2, "city.t_trade_C"  ; 12
  7, 3, "city.t_trade_D"  ; 13
  7, 4, "city.t_trade_E"  ; 14
  7, 5, "city.t_trade_F"  ; 15
  7, 6, "city.t_trade_G"  ; 16
  7, 7, "city.t_trade_H"  ; 17
  7, 8, "city.t_trade_I"  ; 18
  7, 9, "city.t_trade_J"  ; 19
  7, 10, "city.t_trade_K"  ; 20
  7, 11, "city.t_trade_L"  ; 21+

; Unit Extras(not activities)

  3, 10, "unit.connect"
  4, 10, "unit.auto_attack",
         "unit.auto_settler"
  5, 10, "unit.stack"
  6, 10, "unit.loaded"
; Alternate display modes for stacked units 
  3, 11, "unit.stack1"
  4, 11, "unit.stk_shld_r"
  5, 11, "unit.stk_shld_l"
; Stacked unit count for display mode 2
  9, 0,  "unit.stack2"
  9, 1,  "unit.stack3"
  9, 2,  "unit.stack4"
  9, 3,  "unit.stack5"
  9, 4,  "unit.stack6"
  9, 5,  "unit.stack7"
  9, 6,  "unit.stack8"
  9, 7,  "unit.stack9"  ; NB: 9 or more

; Server sends back a single numeral/char for tile output, previously limiting us to 0-9, 
 10, 0, "city.t_food_A"  ; 10
 10, 1, "city.t_food_B"  ; 11
 10, 2, "city.t_food_C"  ; 12
 10, 3, "city.t_food_D"  ; 13
 10, 4, "city.t_food_E"  ; 14
 10, 5, "city.t_food_F"  ; 15
 10, 6, "city.t_food_G"  ; 16
 10, 7, "city.t_food_H"  ; 17
 10, 8, "city.t_food_I"  ; 18
 10, 9, "city.t_food_J"  ; 19
; 10, 10, "city.t_food_K"  ; 20
; 10, 11, "city.t_food_L"  ; 21+

; Server sends back a single numeral/char for tile output, previously limiting us to 0-9, 
 11, 0, "city.t_shields_A"  ; 10
 11, 1, "city.t_shields_B"  ; 11
 11, 2, "city.t_shields_C"  ; 12
 11, 3, "city.t_shields_D"  ; 13
 11, 4, "city.t_shields_E"  ; 14
 11, 5, "city.t_shields_F"  ; 15
 11, 6, "city.t_shields_G"  ; 16
 11, 7, "city.t_shields_H"  ; 17
 11, 8, "city.t_shields_I"  ; 18
 11, 9, "city.t_shields_J"  ; 19
; 11, 10, "city.t_shields_K"  ; 20
; 11, 11, "city.t_shields_L"  ; 21+
}
