# dcs-comms-plan-enforcer

Enforces radio presets and intraflight frequency according to a standardized comms plan. Flight names are used to determine intraflight frequencies, see `comms_plan.py`. Also checks and sets frequencies of AI flights such as tankers or AWACS.

## Requirements

* Python 3.9
* pydcs (see requirements.txt)

## Usage

`python main.py myMissionFile.miz enforcedMissionFile.miz`

(Future updates will include exe file releases)

## Example run

```
python main.py test_mission.miz output.miz

Loaded mission file test_mission_syria.miz
Found comms plan for blue
Unit Monster91 has correct primary channels!
Unit Monster92 has correct primary channels!
Unit Monster93 has correct primary channels!
Unit Monster94 has correct primary channels!
Unit Vodka61 has correct primary channels!
Unit Vodka62 has correct primary channels!
Unit Vodka63 has correct primary channels!
Unit Vodka64 has correct primary channels!
Unit type FW-190D9 not supported, skipping
Unit Unicorn51 has correct primary channels!
Unit Unicorn52 has correct primary channels!
Unit Unicorn53 has correct primary channels!
Unit Unicorn514 has correct primary channels!
Unit Zoom71 has correct primary channels!
Unit Zoom72 has correct primary channels!
Unit Zoom73 has correct primary channels!
Unit Zoom74 has correct primary channels!
Unit Player_01 has correct primary channels!
Unit Player_02 has correct primary channels!
Unit Player_03 has correct primary channels!
Unit Player_04 has correct primary channels!
Unit Player_08 has correct primary channels!
Unit Player_06 has correct primary channels!
Unit Player_07 has correct primary channels!
Unit Player_05 has correct primary channels!
Unit Player_11 has correct primary channels!
Unit Player_09 has correct primary channels!
Unit Player_10 has correct primary channels!
Unit Player_12 has correct primary channels!
AI group SHELL3 103X (USN) has correct frequency 253
Unit type KC135MPRS not supported, skipping
Unit Player_16 has correct primary channels!
Unit Player_14 has correct primary channels!
Unit Player_15 has correct primary channels!
Unit Player_13 has correct primary channels!
Unit Player_17 has correct primary channels!
Unit Player_18 has correct primary channels!
Unit Player_19 has correct primary channels!
Unit Player_20 has correct primary channels!
Unit Player_21 has correct primary channels!
Unit Player_22 has correct primary channels!
Unit Player_23 has correct primary channels!
Unit Player_24 has correct primary channels!
Unit Player_25 has correct primary channels!
Unit Player_26 has correct primary channels!
Unit Player_27 has correct primary channels!
Unit Player_28 has correct primary channels!
Unit Player_29 has correct primary channels!
Unit Player_30 has correct primary channels!
Unit Player_31 has correct primary channels!
Unit Player_32 has correct primary channels!
Unit Pilot #005 has correct primary channels!
Unit Pilot #010 has correct primary channels!
Unit Pilot #011 has correct primary channels!
Unit Pilot #012 has correct primary channels!
AI group ARCO1 101X (USN) has correct frequency 260
Unit type KC135MPRS not supported, skipping
AI group TEXACO2 102X (USAF) has correct frequency 266
Unit type KC-135 not supported, skipping
AI group STINGRAY1 has correct frequency 251
Unit type E-3A not supported, skipping
Unit Gandalf51 has correct primary channels!
Unit Gandalf52 has correct primary channels!
Unit Gandalf53 has correct primary channels!
Unit Gandalf54 has correct primary channels!
Unit Devil11 has correct primary channels!
Unit Devil11 has incorrect intra 305, expected 331.3
Enforcing channels of FA-18C_hornet Devil11
Unit Devil12 has correct primary channels!
Unit Devil12 has incorrect intra 305, expected 331.3
Enforcing channels of FA-18C_hornet Devil12
Unit Devil13 has correct primary channels!
Unit Devil13 has incorrect intra 305, expected 331.3
Enforcing channels of FA-18C_hornet Devil13
Unit Devil14 has correct primary channels!
Unit Devil14 has incorrect intra 305, expected 331.3
Enforcing channels of FA-18C_hornet Devil14
Unit type A-10C_2 not supported, skipping
Unit Gypsy61 has correct primary channels!
Unit Gypsy61 has incorrect intra 305, expected 331.9
Enforcing channels of F-14B Gypsy61
Unit Gypsy62 has correct primary channels!
Unit Gypsy62 has incorrect intra 305, expected 331.9
Enforcing channels of F-14B Gypsy62
Unit Gypsy63 has correct primary channels!
Unit Gypsy63 has incorrect intra 305, expected 331.9
Enforcing channels of F-14B Gypsy63
Unit Gypsy64 has correct primary channels!
Unit Gypsy64 has incorrect intra 305, expected 331.9
Enforcing channels of F-14B Gypsy64
Unit type A-10C_2 not supported, skipping
Unit Nemo31 has correct primary channels!
Unit Nemo32 has correct primary channels!
Unit Nemo33 has correct primary channels!
Unit Nemo34 has correct primary channels!
Unit Quarterback11 has correct primary channels!
Unit Quarterback11 has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback11
Unit Quarterback12 has correct primary channels!
Unit Quarterback12 has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback12
Unit Quarterback13 has correct primary channels!
Unit Quarterback13 has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback13
Unit Quarterback14 has correct primary channels!
Unit Quarterback14 has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback14
Unit type F-15C not supported, skipping
Unit ._MissionControl_A has correct primary channels!
Unit XRay81 has correct primary channels!
Unit XRay82 has correct primary channels!
Unit XRay83 has correct primary channels!
Unit XRay84 has correct primary channels!
Unit Adder11 has correct primary channels!
Unit Adder11 has incorrect intra 305, expected 330.6
Enforcing channels of FA-18C_hornet Adder11
Unit Adder12 has correct primary channels!
Unit Adder12 has incorrect intra 305, expected 330.6
Enforcing channels of FA-18C_hornet Adder12
Unit Adder13 has correct primary channels!
Unit Adder13 has incorrect intra 305, expected 330.6
Enforcing channels of FA-18C_hornet Adder13
Unit Adder14 has correct primary channels!
Unit Adder14 has incorrect intra 305, expected 330.6
Enforcing channels of FA-18C_hornet Adder14
Unit Beaver21 has correct primary channels!
Unit Beaver21 has incorrect intra 305, expected 330.7
Enforcing channels of FA-18C_hornet Beaver21
Unit Beaver22 has correct primary channels!
Unit Beaver22 has incorrect intra 305, expected 330.7
Enforcing channels of FA-18C_hornet Beaver22
Unit Beaver23 has correct primary channels!
Unit Beaver23 has incorrect intra 305, expected 330.7
Enforcing channels of FA-18C_hornet Beaver23
Unit Beaver24 has correct primary channels!
Unit Beaver24 has incorrect intra 305, expected 330.7
Enforcing channels of FA-18C_hornet Beaver24
Unit Camel31 has correct primary channels!
Unit Camel31 has incorrect intra 305, expected 330.8
Enforcing channels of FA-18C_hornet Camel31
Unit Camel32 has correct primary channels!
Unit Camel32 has incorrect intra 305, expected 330.8
Enforcing channels of FA-18C_hornet Camel32
Unit Camel33 has correct primary channels!
Unit Camel33 has incorrect intra 305, expected 330.8
Enforcing channels of FA-18C_hornet Camel33
Unit Camel34 has correct primary channels!
Unit Camel34 has incorrect intra 305, expected 330.8
Enforcing channels of FA-18C_hornet Camel34
Unit Cheetah41 has correct primary channels!
Unit Cheetah41 has incorrect intra 305, expected 330.9
Enforcing channels of F-14B Cheetah41
Unit Cheetah42 has correct primary channels!
Unit Cheetah42 has incorrect intra 305, expected 330.9
Enforcing channels of F-14B Cheetah42
Unit Cheetah43 has correct primary channels!
Unit Cheetah43 has incorrect intra 305, expected 330.9
Enforcing channels of F-14B Cheetah43
Unit Cheetah44 has correct primary channels!
Unit Cheetah44 has incorrect intra 305, expected 330.9
Enforcing channels of F-14B Cheetah44
Unit type A-10C not supported, skipping
Unit type F-15E not supported, skipping
Unit Zodiac51 has correct primary channels!
Unit Zodiac51 has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac51
Unit Zodiac52 has correct primary channels!
Unit Zodiac52 has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac52
Unit Zodiac53 has correct primary channels!
Unit Zodiac53 has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac53
Unit Zodiac54 has correct primary channels!
Unit Zodiac54 has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac54
Unit Dogfight F/A-18C BLUE 1 has correct primary channels!
Unit Dogfight F/A-18C BLUE 2 has correct primary channels!
Unit Dogfight F-16C BLUE 1 has correct primary channels!
Unit Dogfight F-16C BLUE 2 has correct primary channels!
Unit Dogfight F-14B BLUE 1 has correct primary channels!
Unit Dogfight F-14B BLUE 2 has correct primary channels!
Unit type P-51D not supported, skipping
Unit type MiG-15bis not supported, skipping
Unit type F-86F Sabre not supported, skipping
Unit type P-47D-40 not supported, skipping
Unit type F-15C not supported, skipping
Unit ZZ Dogfight F-5E-3 BLUE 1 has correct primary channels!
Unit ZZ Dogfight F-5E-3 BLUE 2 has correct primary channels!
Unit type F-86F Sabre not supported, skipping
Unit ZZ Dogfight JF-17 BLUE 1 has correct primary channels!
Unit ZZ Dogfight JF-17 BLUE 2 has correct primary channels!
Unit ZZ Dogfight M-2000C BLUE 1 has correct primary channels!
Unit ZZ Dogfight M-2000C BLUE 2 has correct primary channels!
Unit type P-47D-30 not supported, skipping
Unit type SpitfireLFMkIX not supported, skipping
Unit type Su-27 not supported, skipping
Unit Blue Singleton Easy of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
Unit Blue Two-ship Easy of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
Unit Pilot #013 of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
Unit Blue Singleton Hard of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
Unit Blue Two-ship Hard of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
Unit Pilot #004 of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
AI group STINGRAY2 has correct frequency 251
Unit type E-3A not supported, skipping
Unit Fenris41_Roadside has correct primary channels!
Unit Fenris42_Roadside has correct primary channels!
Unit Fenris43_Roadside has correct primary channels!
Unit Fenris44_Roadside has correct primary channels!
Unit Quarterback11_Roadside has correct primary channels!
Unit Quarterback11_Roadside has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback11_Roadside
Unit Quarterback12_Roadside has correct primary channels!
Unit Quarterback12_Roadside has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback12_Roadside
Unit Quarterback13_Roadside has correct primary channels!
Unit Quarterback13_Roadside has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback13_Roadside
Unit Quarterback14_Roadside has correct primary channels!
Unit Quarterback14_Roadside has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback14_Roadside
Unit Zodiac51_Roadside has correct primary channels!
Unit Zodiac51_Roadside has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac51_Roadside
Unit Zodiac52_Roadside has correct primary channels!
Unit Zodiac52_Roadside has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac52_Roadside
Unit Zodiac53_Roadside has correct primary channels!
Unit Zodiac53_Roadside has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac53_Roadside
Unit Zodiac54_Roadside has correct primary channels!
Unit Zodiac54_Roadside has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac54_Roadside
Unit Gandalf51_Roadside has correct primary channels!
Unit Gandalf52_Roadside has correct primary channels!
Unit Gandalf53_Roadside has correct primary channels!
Unit Gandalf54_Roadside has correct primary channels!
Unit type F-14A-135-GR not supported, skipping
Unit type F-14A-135-GR not supported, skipping
AI group TEXACO4 104X (USAF) has correct frequency 255
Unit type KC-135 not supported, skipping
Unit Aerial-1-1 has correct primary channels!
Unit Quarterback11_Tarawa has correct primary channels!
Unit Quarterback11_Tarawa has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback11_Tarawa
Unit Quarterback12_Tarawa has correct primary channels!
Unit Quarterback12_Tarawa has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback12_Tarawa
Unit Quarterback13_Tarawa has correct primary channels!
Unit Quarterback13_Tarawa has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback13_Tarawa
Unit Quarterback14_Tarawa has correct primary channels!
Unit Quarterback14_Tarawa has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback14_Tarawa
Unit ZZ BVR F-16C BLUE-1 has correct primary channels!
Unit ZZ BVR F-16C BLUE-2 has correct primary channels!
Unit ZZ BVR F-16C BLUE-3 has correct primary channels!
Unit ZZ BVR F-16C BLUE-4 has correct primary channels!
Unit ZZ BVR F/A-18C BLUE-1 has correct primary channels!
Unit ZZ BVR F/A-18C BLUE-2 has correct primary channels!
Unit ZZ BVR F/A-18C BLUE-3 has correct primary channels!
Unit ZZ BVR F/A-18C BLUE-4 has correct primary channels!
Unit ZZ BVR F-14B BLUE 1 has correct primary channels!
Unit ZZ BVR F-14B BLUE 2 has correct primary channels!
Unit ZZ BVR F-14B BLUE 3 has correct primary channels!
Unit ZZ BVR F-14B BLUE 4 has correct primary channels!
Unit type F-15C not supported, skipping
Unit type SH-60B not supported, skipping
Unit Rattler21 has correct primary channels!
Unit Rattler22 has correct primary channels!
Unit Rattler23 has correct primary channels!
Unit Rattler24 has correct primary channels!
Unit type Ka-50 not supported, skipping
Unit Turtle41 has correct primary channels!
Unit Turtle42 has correct primary channels!
Unit Turtle43 has correct primary channels!
Unit Turtle44 has correct primary channels!
Unit type Ka-50 not supported, skipping
Unit Rocky21 has correct primary channels!
Unit Rocky22 has correct primary channels!
Unit Rocky23 has correct primary channels!
Unit Rocky24 has correct primary channels!
Unit Rocky21_Tarawa has correct primary channels!
Unit Rocky22_Tarawa has correct primary channels!
Unit Rocky23_Tarawa has correct primary channels!
Unit Rocky24_Tarawa has correct primary channels!
Unit type MiG-29A not supported, skipping
Unit Zeppelin21 has correct primary channels!
Unit Zeppelin21 has incorrect intra 305, expected 134.1
Enforcing channels of M-2000C Zeppelin21
Unit Zeppelin22 has correct primary channels!
Unit Zeppelin22 has incorrect intra 305, expected 134.1
Enforcing channels of M-2000C Zeppelin22
Unit Zeppelin23 has correct primary channels!
Unit Zeppelin23 has incorrect intra 305, expected 134.1
Enforcing channels of M-2000C Zeppelin23
Unit Zeppelin24 has correct primary channels!
Unit Zeppelin24 has incorrect intra 305, expected 134.1
Enforcing channels of M-2000C Zeppelin24
Unit type SA342M not supported, skipping
Unit type SpitfireLFMkIX not supported, skipping
Unit Empress31 has correct primary channels!
Unit Empress31 has incorrect intra 127, expected 131.5
Enforcing channels of F-16C_50 Empress31
Unit Empress32 has correct primary channels!
Unit Empress32 has incorrect intra 127, expected 131.5
Enforcing channels of F-16C_50 Empress32
Unit Empress33 has correct primary channels!
Unit Empress33 has incorrect intra 127, expected 131.5
Enforcing channels of F-16C_50 Empress33
Unit Empress34 has correct primary channels!
Unit Empress34 has incorrect intra 127, expected 131.5
Enforcing channels of F-16C_50 Empress34
Unit Echo21 has correct primary channels!
Unit Echo21 has incorrect intra 127, expected 131.4
Enforcing channels of F-16C_50 Echo21
Unit Pilot #009 has correct primary channels!
Unit Pilot #009 has incorrect intra 127, expected 131.4
Enforcing channels of F-16C_50 Pilot #009
Unit Pilot #021 has correct primary channels!
Unit Pilot #021 has incorrect intra 127, expected 131.4
Enforcing channels of F-16C_50 Pilot #021
Unit Pilot #022 has correct primary channels!
Unit Pilot #022 has incorrect intra 127, expected 131.4
Enforcing channels of F-16C_50 Pilot #022
Unit Formup Drone F-16C of type F-16C_50 with radio None not checkable, probably because A-10 or AI controlled
Unit Epic41 has correct primary channels!
Unit Epic41 has incorrect intra 127, expected 131.6
Enforcing channels of F-16C_50 Epic41
Unit Epic42 has correct primary channels!
Unit Epic42 has incorrect intra 127, expected 131.6
Enforcing channels of F-16C_50 Epic42
Unit Epic43 has correct primary channels!
Unit Epic43 has incorrect intra 127, expected 131.6
Enforcing channels of F-16C_50 Epic43
Unit Epic44 has correct primary channels!
Unit Epic44 has incorrect intra 127, expected 131.6
Enforcing channels of F-16C_50 Epic44
Unit type Su-27 not supported, skipping
Unit Scorpion31 has correct primary channels!
Unit Scorpion32 has correct primary channels!
Unit Scorpion33 has correct primary channels!
Unit Scorpion34 has correct primary channels!
Unit Scorpion41 has correct primary channels!
Unit Scorpion42 has correct primary channels!
Unit Scorpion43 has correct primary channels!
Unit Scorpion44 has correct primary channels!
Unit Scorpion31_Cyprus has correct primary channels!
Unit Scorpion32_Cyprus has correct primary channels!
Unit Scorpion33_Cyprus has correct primary channels!
Unit Scorpion34_Cyprus has correct primary channels!
Unit Scorpion41_Cyprus has correct primary channels!
Unit Scorpion42_Cyprus has correct primary channels!
Unit Scorpion43_Cyprus has correct primary channels!
Unit Scorpion44_Cyprus has correct primary channels!
Unit type Su-25T not supported, skipping
Unit type Su-25T not supported, skipping
No comms plan found for red
No comms plan found for neutrals
60 units were updated/enforced
There were 60 incorrects
Dry run was completed
```
