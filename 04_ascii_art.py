import os, time
import regex as re
from colorama import Fore, Back, Style 
import platform

if platform.system() == 'Linux':
    clear = 'clear'
else: 
    clear = 'cls'

os.system('clear')

INPUT = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''.split('\n\n')


def print_result(valid, passport, count):
    '''print a formatted string with the fields of the passport and the validation result'''
    fields = passport.split()
    fields = {
        field.split(':')[0].strip(): ''.join(field.split(':')[1:])
        for field in fields
    }
    # print(fields)
    form = '''
    /------------------------------------------\\
    |\t       \t|   Birth Year: {byr}\t\t|
    |\t       \t|   Issue Year: {iyr}\t\t|
    |\tRESULT\t|   Expiration Year: {eyr}\t|
    |\t       \t|   Height: {hgt}\t\t|
    |\t{valid}\t|   Hair Color: {hcl}\t\t|
    |\t       \t|   Eye Color: {ecl}\t\t|
    |\t       \t|   Passport ID: {pid}\t|
    |\t       \t|   Country ID: {cid}\t\t|
    \------------------------------------------/
    valid: {count}
    '''.format(
        byr = fields['byr'] if 'byr' in fields else '', 
        iyr = fields['iyr'] if 'iyr' in fields else '\t', 
        eyr = fields['eyr'] if 'eyr' in fields else '\t', 
        hgt = fields['hgt'] if 'hgt' in fields else '\t', 
        hcl = fields['hcl'] if 'hcl' in fields else '\t', 
        ecl = fields['ecl'] if 'ecl' in fields else '\t', 
        pid = fields['pid'] if 'pid' in fields else '\t', 
        cid = fields['cid'] if 'cid' in fields else '', 
        valid = Fore.GREEN + 'valid  ' + Style.RESET_ALL if valid else Fore.RED + 'invalid' + Style.RESET_ALL,
        count = count
    )
    print(form)


def check_field(field):
    field_validation = {
        # if it is not an int, will return false, must be > 999 to be 4 digits
        'byr': lambda year: 1920 <= int(year) <= 2002,
        'iyr': lambda year: int(year) > 999 and 2010 <= int(year) <= 2020,
        'eyr': lambda year: int(year) > 999 and 2020 <= int(year) <= 2030,
        'hgt': lambda height: (height[-2:] == 'cm' and 150 <= int(height[:-2]) <= 193) or (height[-2:] == 'in' and 59 <= int(height[:-2]) <= 76),
        'hcl': lambda hcl: hcl[0] == '#' and bool(re.search('^#[0-9a-f]{6}$', hcl)),
        'ecl': lambda ecl: bool(re.search('^amb|blu|brn|gry|grn|hzl|oth$', ecl)),
        'pid': lambda pid: bool(re.search('^[0-9]{9}$', pid))
    }
    key, value = field.split(':')
    # cid does not have to be checked
    if key == 'cid':
        return True
    try:
        return field_validation[key](value)
    except KeyError as e:
        print(e)
        return False


def check_passports_field_validation(passports):
    '''Check passports,
    return number of valid passports'''
    valid_passports = 0

    for passport in passports:            
        fields = passport.split()
        field_number = len(fields)

        # cid is optional
        if 'cid:' not in passport: 
            field_number += 1

        valid = False
        if field_number >= 8:
            valid = True
            for i, field in enumerate(fields):
                if not check_field(field):
                    # red if field is invalid
                    fields[i] = field.split(':')[0] + ':' + Fore.RED + field + Style.RESET_ALL
                    valid = False
            if valid: 
                valid_passports += 1

        os.system(clear)
        print_result(valid, ' '.join(fields), valid_passports)
        time.sleep(0.4)

    os.system(clear)
    return valid_passports



check_passports_field_validation(INPUT)

with open('04.txt', 'r') as o:
    # split passports on blank lines
    passports = o.read().split('\n\n')

check_passports_field_validation(passports)
