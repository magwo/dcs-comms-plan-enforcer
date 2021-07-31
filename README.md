# DCS Comms Plan Enforcer by Mags

Enforces radio presets and intraflight frequency according to a standardized comms plan, per coalition. Flight names are used to determine intraflight frequencies, see [comms_plan_example.json](comms_plan_example.json). Also checks and sets frequencies of AI flights such as tankers or AWACS.

Typical use cases are to check existing missions for correctness, or to modify generated mission files, for example when playing [Liberation](https://github.com/dcs-liberation/dcs_liberation).

<img src="https://github.com/magwo/dcs-comms-plan-enforcer/blob/main/screenshot.png?raw=true" width="500"/>

## Requirements

* Windows
* DCS

## Installation

* Download comms-plan-enforcer.zip from the [latest release](https://github.com/magwo/dcs-comms-plan-enforcer/releases).
* Extract the zip file.
* Find and run comms-plan-enforcer.exe in the extracted folder.

## Usage

* Find and run comms-plan-enforcer.exe in extracted folder.
* Enter filenames when prompted.

An example comms plan JSON is included in the application directory: `comms_plan_example.json`. Feel free to edit this file, or copy it to another location and edit your own comms plan. I recommend putting your comms plan file in your Missions folder in "Saved Games DCS", for easy access.

### Advanced usage

The exe file also supports command-line arguments on the format:

`comms-plan-enforcer.exe myMission.miz comms_plan_example.json myEnforcedMission.miz`

Any missing command-line arguments will result in a dialog.

You can specify comms plan for `red` and `neutrals` coalitions in the comms plan JSON file, by adding them on the same level as "blue" in the JSON file.

## Example run

```
FA-18C_hornet Player_01 has correct primary channels!
FA-18C_hornet Player_02 has correct primary channels!
FA-18C_hornet Player_03 has correct primary channels!
FA-18C_hornet Player_04 has correct primary channels!
FA-18C_hornet Player_08 has correct primary channels!
FA-18C_hornet Player_06 has correct primary channels!
FA-18C_hornet Player_07 has correct primary channels!
FA-18C_hornet Player_05 has correct primary channels!
FA-18C_hornet Player_11 has correct primary channels!
FA-18C_hornet Player_09 has correct primary channels!
FA-18C_hornet Player_10 has correct primary channels!
FA-18C_hornet Player_12 has correct primary channels!
AI group SHELL3 103X (USN) has correct frequency 253
Unit type KC135MPRS not supported, skipping
FA-18C_hornet Player_16 has correct primary channels!
FA-18C_hornet Player_14 has correct primary channels!
FA-18C_hornet Player_15 has correct primary channels!
FA-18C_hornet Player_13 has correct primary channels!
FA-18C_hornet Player_17 has correct primary channels!
FA-18C_hornet Player_18 has correct primary channels!
FA-18C_hornet Player_19 has correct primary channels!
FA-18C_hornet Player_20 has correct primary channels!
F-14B Player_21 has correct primary channels!
F-14B Player_22 has correct primary channels!
F-14B Player_23 has correct primary channels!
F-14B Player_24 has correct primary channels!
F-14B Player_25 has correct primary channels!
F-14B Player_26 has correct primary channels!
F-14B Player_27 has correct primary channels!
F-14B Player_28 has correct primary channels!
F-14B Player_29 has correct primary channels!
F-14B Player_30 has correct primary channels!
F-14B Player_31 has correct primary channels!
F-14B Player_32 has correct primary channels!
AJS37 Pilot #005 incorrect channel 5: 262 should be 259.0
AJS37 Pilot #005 incorrect channel 6: 259 should be 268.0
2 incorrect channels for unit Pilot #005
Enforcing channels of AJS37 Pilot #005
AJS37 Pilot #010 incorrect channel 5: 262 should be 259.0
AJS37 Pilot #010 incorrect channel 6: 259 should be 268.0
2 incorrect channels for unit Pilot #010
Enforcing channels of AJS37 Pilot #010
AJS37 Pilot #011 incorrect channel 5: 262 should be 259.0
AJS37 Pilot #011 incorrect channel 6: 259 should be 268.0
2 incorrect channels for unit Pilot #011
Enforcing channels of AJS37 Pilot #011
AJS37 Pilot #012 incorrect channel 5: 262 should be 259.0
AJS37 Pilot #012 incorrect channel 6: 259 should be 268.0
2 incorrect channels for unit Pilot #012
Enforcing channels of AJS37 Pilot #012
AI group ARCO1 101X (USN) has correct frequency 260
Unit type KC135MPRS not supported, skipping
AI group TEXACO2 102X (USAF) has correct frequency 266
Unit type KC-135 not supported, skipping
AI group STINGRAY1 has correct frequency 251
Unit type E-3A not supported, skipping
AJS37 Gandalf51 incorrect channel 5: 262 should be 259.0
AJS37 Gandalf51 incorrect channel 6: 259 should be 268.0
2 incorrect channels for unit Gandalf51
Enforcing channels of AJS37 Gandalf51
AJS37 Gandalf52 incorrect channel 5: 262 should be 259.0
AJS37 Gandalf52 incorrect channel 6: 259 should be 268.0
2 incorrect channels for unit Gandalf52
Enforcing channels of AJS37 Gandalf52
AJS37 Gandalf53 incorrect channel 5: 262 should be 259.0
AJS37 Gandalf53 incorrect channel 6: 259 should be 268.0
2 incorrect channels for unit Gandalf53
Enforcing channels of AJS37 Gandalf53
AJS37 Gandalf54 incorrect channel 5: 262 should be 259.0
AJS37 Gandalf54 incorrect channel 6: 259 should be 268.0
2 incorrect channels for unit Gandalf54
Enforcing channels of AJS37 Gandalf54
FA-18C_hornet Devil11 has correct primary channels!
FA-18C_hornet Devil11 has incorrect intra 305, expected 331.3
Enforcing channels of FA-18C_hornet Devil11
FA-18C_hornet Devil12 has correct primary channels!
FA-18C_hornet Devil12 has incorrect intra 305, expected 331.3
Enforcing channels of FA-18C_hornet Devil12
FA-18C_hornet Devil13 has correct primary channels!
FA-18C_hornet Devil13 has incorrect intra 305, expected 331.3
Enforcing channels of FA-18C_hornet Devil13
FA-18C_hornet Devil14 has correct primary channels!
FA-18C_hornet Devil14 has incorrect intra 305, expected 331.3
Enforcing channels of FA-18C_hornet Devil14
Unit type A-10C_2 not supported, skipping
F-14B Gypsy61 has correct primary channels!
F-14B Gypsy61 has incorrect intra 305, expected 331.9
Enforcing channels of F-14B Gypsy61
F-14B Gypsy62 has correct primary channels!
F-14B Gypsy62 has incorrect intra 305, expected 331.9
Enforcing channels of F-14B Gypsy62
F-14B Gypsy63 has correct primary channels!
F-14B Gypsy63 has incorrect intra 305, expected 331.9
Enforcing channels of F-14B Gypsy63
F-14B Gypsy64 has correct primary channels!
F-14B Gypsy64 has incorrect intra 305, expected 331.9
Enforcing channels of F-14B Gypsy64
F-16C_50 Echo21 has correct primary channels!
F-16C_50 Echo21 has incorrect intra 127, expected 131.4
Enforcing channels of F-16C_50 Echo21
F-16C_50 Echo22 has correct primary channels!
F-16C_50 Echo22 has incorrect intra 127, expected 131.4
Enforcing channels of F-16C_50 Echo22
F-16C_50 Echo23 has correct primary channels!
F-16C_50 Echo23 has incorrect intra 127, expected 131.4
Enforcing channels of F-16C_50 Echo23
F-16C_50 Echo24 has correct primary channels!
F-16C_50 Echo24 has incorrect intra 127, expected 131.4
Enforcing channels of F-16C_50 Echo24
F-16C_50 Empress31 has correct primary channels!
F-16C_50 Empress31 has incorrect intra 127, expected 131.5
Enforcing channels of F-16C_50 Empress31
F-16C_50 Empress32 has correct primary channels!
F-16C_50 Empress32 has incorrect intra 127, expected 131.5
Enforcing channels of F-16C_50 Empress32
F-16C_50 Empress33 has correct primary channels!
F-16C_50 Empress33 has incorrect intra 127, expected 131.5
Enforcing channels of F-16C_50 Empress33
F-16C_50 Empress34 has correct primary channels!
F-16C_50 Empress34 has incorrect intra 127, expected 131.5
Enforcing channels of F-16C_50 Empress34
Unit type A-10C_2 not supported, skipping
F-5E-3 Nemo31 has correct primary channels!
F-5E-3 Nemo32 has correct primary channels!
F-5E-3 Nemo33 has correct primary channels!
F-5E-3 Nemo34 has correct primary channels!
AV8BNA Quarterback11 has correct primary channels!
AV8BNA Quarterback11 has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback11
AV8BNA Quarterback12 has correct primary channels!
AV8BNA Quarterback12 has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback12
AV8BNA Quarterback13 has correct primary channels!
AV8BNA Quarterback13 has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback13
AV8BNA Quarterback14 has correct primary channels!
AV8BNA Quarterback14 has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback14
Unit type F-15C not supported, skipping
FA-18C_hornet ._MissionControl_A has correct primary channels!
JF-17 XRay81 has correct primary channels!
JF-17 XRay82 has correct primary channels!
JF-17 XRay83 has correct primary channels!
JF-17 XRay84 has correct primary channels!
FA-18C_hornet Adder11 has correct primary channels!
FA-18C_hornet Adder11 has incorrect intra 305, expected 330.6
Enforcing channels of FA-18C_hornet Adder11
FA-18C_hornet Adder12 has correct primary channels!
FA-18C_hornet Adder12 has incorrect intra 305, expected 330.6
Enforcing channels of FA-18C_hornet Adder12
FA-18C_hornet Adder13 has correct primary channels!
FA-18C_hornet Adder13 has incorrect intra 305, expected 330.6
Enforcing channels of FA-18C_hornet Adder13
FA-18C_hornet Adder14 has correct primary channels!
FA-18C_hornet Adder14 has incorrect intra 305, expected 330.6
Enforcing channels of FA-18C_hornet Adder14
FA-18C_hornet Beaver21 has correct primary channels!
FA-18C_hornet Beaver21 has incorrect intra 305, expected 330.7
Enforcing channels of FA-18C_hornet Beaver21
FA-18C_hornet Beaver22 has correct primary channels!
FA-18C_hornet Beaver22 has incorrect intra 305, expected 330.7
Enforcing channels of FA-18C_hornet Beaver22
FA-18C_hornet Beaver23 has correct primary channels!
FA-18C_hornet Beaver23 has incorrect intra 305, expected 330.7
Enforcing channels of FA-18C_hornet Beaver23
FA-18C_hornet Beaver24 has correct primary channels!
FA-18C_hornet Beaver24 has incorrect intra 305, expected 330.7
Enforcing channels of FA-18C_hornet Beaver24
FA-18C_hornet Camel31 has correct primary channels!
FA-18C_hornet Camel31 has incorrect intra 305, expected 330.8
Enforcing channels of FA-18C_hornet Camel31
FA-18C_hornet Camel32 has correct primary channels!
FA-18C_hornet Camel32 has incorrect intra 305, expected 330.8
Enforcing channels of FA-18C_hornet Camel32
FA-18C_hornet Camel33 has correct primary channels!
FA-18C_hornet Camel33 has incorrect intra 305, expected 330.8
Enforcing channels of FA-18C_hornet Camel33
FA-18C_hornet Camel34 has correct primary channels!
FA-18C_hornet Camel34 has incorrect intra 305, expected 330.8
Enforcing channels of FA-18C_hornet Camel34
F-14B Cheetah41 has correct primary channels!
F-14B Cheetah41 has incorrect intra 305, expected 330.9
Enforcing channels of F-14B Cheetah41
F-14B Cheetah42 has correct primary channels!
F-14B Cheetah42 has incorrect intra 305, expected 330.9
Enforcing channels of F-14B Cheetah42
F-14B Cheetah43 has correct primary channels!
F-14B Cheetah43 has incorrect intra 305, expected 330.9
Enforcing channels of F-14B Cheetah43
F-14B Cheetah44 has correct primary channels!
F-14B Cheetah44 has incorrect intra 305, expected 330.9
Enforcing channels of F-14B Cheetah44
Unit type A-10C not supported, skipping
Unit type F-15E not supported, skipping
Unit Formup Drone F-16C of type F-16C_50 with radio None not checkable, probably because A-10 or AI controlled
FA-18C_hornet Zodiac51 has correct primary channels!
FA-18C_hornet Zodiac51 has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac51
FA-18C_hornet Zodiac52 has correct primary channels!
FA-18C_hornet Zodiac52 has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac52
FA-18C_hornet Zodiac53 has correct primary channels!
FA-18C_hornet Zodiac53 has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac53
FA-18C_hornet Zodiac54 has correct primary channels!
FA-18C_hornet Zodiac54 has incorrect intra 305, expected 334.2
Enforcing channels of FA-18C_hornet Zodiac54
FA-18C_hornet Dogfight F/A-18C BLUE 1 has correct primary channels!
FA-18C_hornet Dogfight F/A-18C BLUE 2 has correct primary channels!
F-16C_50 Dogfight F-16C BLUE 1 has correct primary channels!
F-16C_50 Dogfight F-16C BLUE 2 has correct primary channels!
F-14B Dogfight F-14B BLUE 1 has correct primary channels!
F-14B Dogfight F-14B BLUE 2 has correct primary channels!
Unit type P-51D not supported, skipping
Unit type MiG-15bis not supported, skipping
Unit type F-86F Sabre not supported, skipping
Unit type P-47D-40 not supported, skipping
Unit type F-15C not supported, skipping
F-5E-3 ZZ Dogfight F-5E-3 BLUE 1 has correct primary channels!
F-5E-3 ZZ Dogfight F-5E-3 BLUE 2 has correct primary channels!
Unit type F-86F Sabre not supported, skipping
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 1: 108 should be 305.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 2: 108.5 should be 264.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 3: 109 should be 265.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 4: 109.5 should be 256.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 5: 110 should be 254.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 6: 110.5 should be 250.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 7: 111 should be 270.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 8: 111.5 should be 257.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 9: 112 should be 255.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 10: 112.5 should be 262.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 11: 113 should be 259.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 12: 113.5 should be 268.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 13: 114 should be 269.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 14: 114.5 should be 260.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 15: 115 should be 263.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 16: 115.5 should be 261.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 17: 116 should be 267.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 18: 116.5 should be 251.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 19: 117 should be 253.0
JF-17 ZZ Dogfight JF-17 BLUE 1 incorrect channel 20: 117.5 should be 266.0
20 incorrect channels for unit ZZ Dogfight JF-17 BLUE 1
Enforcing channels of JF-17 ZZ Dogfight JF-17 BLUE 1
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 1: 108 should be 305.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 2: 108.5 should be 264.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 3: 109 should be 265.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 4: 109.5 should be 256.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 5: 110 should be 254.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 6: 110.5 should be 250.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 7: 111 should be 270.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 8: 111.5 should be 257.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 9: 112 should be 255.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 10: 112.5 should be 262.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 11: 113 should be 259.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 12: 113.5 should be 268.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 13: 114 should be 269.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 14: 114.5 should be 260.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 15: 115 should be 263.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 16: 115.5 should be 261.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 17: 116 should be 267.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 18: 116.5 should be 251.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 19: 117 should be 253.0
JF-17 ZZ Dogfight JF-17 BLUE 2 incorrect channel 20: 117.5 should be 266.0
20 incorrect channels for unit ZZ Dogfight JF-17 BLUE 2
Enforcing channels of JF-17 ZZ Dogfight JF-17 BLUE 2
M-2000C ZZ Dogfight M-2000C BLUE 1 incorrect channel 1: 251 should be 305.0
1 incorrect channels for unit ZZ Dogfight M-2000C BLUE 1
Enforcing channels of M-2000C ZZ Dogfight M-2000C BLUE 1
M-2000C ZZ Dogfight M-2000C BLUE 2 incorrect channel 1: 251 should be 305.0
1 incorrect channels for unit ZZ Dogfight M-2000C BLUE 2
Enforcing channels of M-2000C ZZ Dogfight M-2000C BLUE 2
Unit type P-47D-30 not supported, skipping
Unit type SpitfireLFMkIX not supported, skipping
Unit type Su-27 not supported, skipping
Unit Blue Singleton Easy of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
Unit Blue Two-ship Easy of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
Unit Pilot #013 of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
Unit Blue Singleton Hard of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
Unit Blue Two-ship Hard of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
Unit Pilot #004 of type FA-18C_hornet with radio None not checkable, probably because A-10 or AI controlled
FA-18C_hornet Intro - Hornet - Nugget11 has correct primary channels!
FA-18C_hornet Intro - Hornet - Nugget12 has correct primary channels!
F-16C_50 Intro - Viper - Nugget11 has correct primary channels!
F-16C_50 Intro - Viper - Nugget12 has correct primary channels!
Unit type A-10C_2 not supported, skipping
AJS37 Intro - Viggen - Nugget11 incorrect channel 5: 262 should be 259.0
AJS37 Intro - Viggen - Nugget11 incorrect channel 6: 259 should be 268.0
2 incorrect channels for unit Intro - Viggen - Nugget11
Enforcing channels of AJS37 Intro - Viggen - Nugget11
AJS37 Intro - Viggen - Nugget12 incorrect channel 5: 262 should be 259.0
AJS37 Intro - Viggen - Nugget12 incorrect channel 6: 259 should be 268.0
2 incorrect channels for unit Intro - Viggen - Nugget12
Enforcing channels of AJS37 Intro - Viggen - Nugget12
F-14B Intro - Tomcat - Nugget11 has correct primary channels!
F-14B Intro - Tomcat - Nugget12 has correct primary channels!
Unit type F-14A-135-GR not supported, skipping
Unit type F-14A-135-GR not supported, skipping
AI group STINGRAY2 has correct frequency 251
Unit type E-3A not supported, skipping
AI group TEXACO4 104X (USAF) has correct frequency 255
Unit type KC-135 not supported, skipping
AV8BNA Quarterback11_Tarawa has correct primary channels!
AV8BNA Quarterback11_Tarawa has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback11_Tarawa
AV8BNA Quarterback12_Tarawa has correct primary channels!
AV8BNA Quarterback12_Tarawa has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback12_Tarawa
AV8BNA Quarterback13_Tarawa has correct primary channels!
AV8BNA Quarterback13_Tarawa has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback13_Tarawa
AV8BNA Quarterback14_Tarawa has correct primary channels!
AV8BNA Quarterback14_Tarawa has incorrect intra 133, expected 332.9
Enforcing channels of AV8BNA Quarterback14_Tarawa
F-16C_50 ZZ BVR F-16C BLUE 1 has correct primary channels!
F-16C_50 ZZ BVR F-16C BLUE 2 has correct primary channels!
F-16C_50 ZZ BVR F-16C BLUE 3 has correct primary channels!
F-16C_50 ZZ BVR F-16C BLUE 4 has correct primary channels!
FA-18C_hornet ZZ BVR F/A-18C 1 has correct primary channels!
FA-18C_hornet ZZ BVR F/A-18C 2 has correct primary channels!
FA-18C_hornet ZZ BVR F/A-18C 3 has correct primary channels!
FA-18C_hornet ZZ BVR F/A-18C 4 has correct primary channels!
F-14B ZZ BVR F-14B BLUE 1 has correct primary channels!
F-14B ZZ BVR F-14B BLUE 2 has correct primary channels!
F-14B ZZ BVR F-14B BLUE 3 has correct primary channels!
F-14B ZZ BVR F-14B BLUE 4 has correct primary channels!
FA-18C_hornet ZZ Intro - Hornet - Nugget21 has correct primary channels!
FA-18C_hornet ZZ Intro - Hornet - Nugget22 has correct primary channels!
F-16C_50 Epic41 has correct primary channels!
F-16C_50 Epic41 has incorrect intra 127, expected 131.6
Enforcing channels of F-16C_50 Epic41
F-16C_50 Epic42 has correct primary channels!
F-16C_50 Epic42 has incorrect intra 127, expected 131.6
Enforcing channels of F-16C_50 Epic42
F-16C_50 Epic43 has correct primary channels!
F-16C_50 Epic43 has incorrect intra 127, expected 131.6
Enforcing channels of F-16C_50 Epic43
F-16C_50 Epic44 has correct primary channels!
F-16C_50 Epic44 has incorrect intra 127, expected 131.6
Enforcing channels of F-16C_50 Epic44
Unit type F-15C not supported, skipping
Unit type SH-60B not supported, skipping
UH-1H Rattler21 has correct primary channels!
UH-1H Rattler22 has correct primary channels!
UH-1H Rattler23 has correct primary channels!
UH-1H Rattler24 has correct primary channels!
Unit type Ka-50 not supported, skipping
Mi-8MT Turtle41 has correct primary channels!
Mi-8MT Turtle42 has correct primary channels!
Mi-8MT Turtle43 has correct primary channels!
Mi-8MT Turtle44 has correct primary channels!
Unit type Ka-50 not supported, skipping
UH-1H Rocky21 has correct primary channels!
UH-1H Rocky22 has correct primary channels!
UH-1H Rocky23 has correct primary channels!
UH-1H Rocky24 has correct primary channels!
UH-1H Rocky21_Tarawa has correct primary channels!
UH-1H Rocky22_Tarawa has correct primary channels!
UH-1H Rocky23_Tarawa has correct primary channels!
UH-1H Rocky24_Tarawa has correct primary channels!
Unit type MiG-29A not supported, skipping
M-2000C Zeppelin21 has correct primary channels!
M-2000C Zeppelin21 has incorrect intra 129, expected 134.1
Enforcing channels of M-2000C Zeppelin21
M-2000C Zeppelin22 has correct primary channels!
M-2000C Zeppelin22 has incorrect intra 129, expected 134.1
Enforcing channels of M-2000C Zeppelin22
M-2000C Zeppelin23 has correct primary channels!
M-2000C Zeppelin23 has incorrect intra 129, expected 134.1
Enforcing channels of M-2000C Zeppelin23
M-2000C Zeppelin24 has correct primary channels!
M-2000C Zeppelin24 has incorrect intra 129, expected 134.1
Enforcing channels of M-2000C Zeppelin24
Unit type SA342M not supported, skipping
Unit type SpitfireLFMkIX not supported, skipping
Unit type Su-27 not supported, skipping
Mi-24P Scorpion31 has correct primary channels!
Mi-24P Scorpion32 has correct primary channels!
Mi-24P Scorpion33 has correct primary channels!
Mi-24P Scorpion34 has correct primary channels!
Mi-24P Scorpion41 has correct primary channels!
Mi-24P Scorpion42 has correct primary channels!
Mi-24P Scorpion43 has correct primary channels!
Mi-24P Scorpion44 has correct primary channels!
Unit type Su-25T not supported, skipping
Unit type Su-25T not supported, skipping
No comms plan found for red
No comms plan found for neutrals
66 units were updated/enforced
There were 114 incorrects
Select file to save enforced mission as
```
