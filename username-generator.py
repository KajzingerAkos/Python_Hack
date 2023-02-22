import argparse

parser = argparse.ArgumentParser(description='Username generator')
parser.add_argument('-f', '--file', help='Set the filename of the names')
parser.add_argument('-o', '--outfile', default="usernames-final.txt", help='Outfile')
parser.add_argument('-d', '--delimiter', type=str, default=' ', help='Set the username delimiter')
args = parser.parse_args()

usernames = []

def generate_usernames(forename,surname):
    usernames.append(surname.lower() + "." + forename.lower())
    usernames.append(surname.lower() + '_' + forename.lower())
    usernames.append(surname.capitalize() + "." + forename.capitalize())
    usernames.append(surname.capitalize() + "_" + forename.capitalize())
    usernames.append(forename.lower() + "." + surname.lower())
    usernames.append(forename.lower() + '_' + surname.lower())
    usernames.append(forename.capitalize() + "." + surname.capitalize())
    usernames.append(forename.capitalize() + "_" + surname.capitalize())
    usernames.append(forename.capitalize())
    usernames.append(forename.lower())
    usernames.append(surname.capitalize())
    usernames.append(surname.lower())

with open(args.file, 'r') as f:
    names = f.readlines()

for name in names:
    seperated = name.split(args.delimiter)
    generate_usernames(seperated[0].strip('\n'),seperated[1].strip('\n'))

with open(args.outfile, 'w') as f:
    for name in usernames:
        f.write(name+'\n')
