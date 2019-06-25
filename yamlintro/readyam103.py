#!/usr/bin/python3

import yaml

def main():
#    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Aruthur Dent", "species": "Human"}]
    yammyfile = open("/home/student/mycode/yamlintro/myYAML.yml", "r")
    pyyammy = yaml.load(yammyfile)
    print (pyyammy)
main()
