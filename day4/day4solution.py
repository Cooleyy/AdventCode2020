#!/usr/bin/env python3
import sys
import re


if __name__ == "__main__":
    
    puzzleInputFile = open(sys.argv[1], 'r')
    passports = puzzleInputFile.read().split("\n\n")
    
    
    for i, passport in enumerate(passports):
        passport = re.split('[\s\n]\s*', passport)
        passports[i] = {}
        for keyValuePair in passport:
            key, value = keyValuePair.split(":")
            passports[i][key] = value

    validPassports = 0
    for  passport in passports:
        if len(passport) == 8 or (len(passport) == 7 and passport.get('cid') == None):
            if int(passport.get("byr")) < 1920 or int(passport.get("byr")) > 2002:
                continue
            if int(passport.get("iyr")) < 2010 or int(passport.get("iyr")) > 2020:
                continue
            if int(passport.get("eyr")) < 2020 or int(passport.get("eyr")) > 2030:
                continue
            if not (passport.get("hgt")[-2:] == "cm" or passport.get("hgt")[-2:] == "in"):
                continue
            if passport.get("hgt")[-2:] == "cm":
                if int(passport.get("hgt")[:-2]) < 150 or int(passport.get("hgt")[:-2]) > 193:
                    continue
            elif passport.get("hgt")[-2:] == "in":
                if int(passport.get("hgt")[:-2]) < 59 or int(passport.get("hgt")[:-2]) > 76:
                    continue
            else:
                continue
            if not re.fullmatch(r"#[0-9A-Fa-f]{6}", passport.get("hcl")):
                continue
            if not passport.get("ecl") in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                continue
            if not re.fullmatch(r"[0-9]{9}", passport.get("pid")):
                continue
            validPassports += 1
            

    print(validPassports)



