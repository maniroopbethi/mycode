#!/usr/bin/python3

import yaml

def main():
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name": "Aruthur Dent", "species": "Human"}]
    print(hitchhikers)

    #zfile = open("galaxyguide.yaml", "w")
    yamlstring = yaml.dump(hitchhikers)
    print (yamlstring)
main()
