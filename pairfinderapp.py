#!/usr/bin/python3
""" aplication for find players that their height sums the integer of the input """

import requests
import json
import sys


def binary_search(dataset, desired_value):
    """ Function for implement binary search """

    # Edge case where dataset is empty
    if len(dataset) == 0:
        return None

    search_index = int(len(dataset) / 2)
    # edge case when the search doesnt find a pair player.
    if len(dataset) == 1 and int(dataset[0]['h_in']) != desired_value:
        return None

    # Structure of the binary search algorithm using recursion.
    if int(dataset[search_index]['h_in']) == desired_value:
        return ("{} {}".format(dataset[search_index]['first_name'], dataset[search_index]['last_name']))
    elif int(dataset[search_index]['h_in']) > desired_value:
        Name = binary_search(dataset[:search_index], desired_value)
    elif int(dataset[search_index]['h_in']) < desired_value:
        Name = binary_search(dataset[search_index:], desired_value)
    return Name


def heightaddsum(heights_sum):
    """ Function that find the pairs of players those height sum is equal to input """


    # 1. Request to the website for the data.
    data = requests.get("https://mach-eight.uc.r.appspot.com/")

    # 2. Using json library to get the dictionary from the data.
    data1 = json.loads(data.text)

    # 3. Implementing the built-in Tim sorting alghoritm to sort the data.
    datasorted = sorted(data1['values'], key= lambda x: int(x['h_in']))

    # 4. Defining the data structure to storage all the players pairs that we are searching.
    pair = {}

    for i in range(len(datasorted)):

        # 5. defining the heigh of the player and the full name.
        height_1 = int(datasorted[i]['h_in'])
        fullname = "{} {}".format(datasorted[i]['first_name'], datasorted[i]['last_name'])
        
        # 6. Calculus of the height to be find and using the binary search to find it.
        desired_value = heights_sum - height_1
        pairplayer = binary_search(datasorted, desired_value)

        # 7. Edge case where the pair is already find it in a past iteration.
        if fullname in pair.values() and pairplayer in pair.keys() and pair[pairplayer] == fullname or fullname == pairplayer:
            pairplayer = None
        
        # 8. Edge case where the pair is made with the same player.
        if fullname == pairplayer:
            pairplayer = None

        # 9. Adding the pair to the data structure and print the pair.
        if pairplayer != None:
            pair[fullname] = pairplayer
            print("{}     {}".format(fullname, pairplayer))

    # 10. Edge case where the search doesnt find any pair.
    if len(pair) == 0:
        print('No matches found')
    else:
        return pair
