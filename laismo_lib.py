#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

words = ["la", "le", "lo"]


def allowed_user(user: str):
    users = os.getenv('LAISMO_USERS').split(",")

    return user in users


def check_laismo(msg: str):
    msg_list = map(lambda word: word.lower(), msg.split(" "))
    return set(msg_list).intersection(set(words))


def add_stats(author):
    stats_file = open("stats.json", "r")
    json_object = json.load(stats_file)
    stats_file.close()

    if author not in json_object:
        json_object[author] = 0
    json_object[author] = json_object[author] + 1

    stats_file = open("stats.json", "w")
    json.dump(json_object, stats_file)
    stats_file.close()


def show_stats():
    stats_file = open("stats.json", "r")
    json_object = json.load(stats_file)
    stats_file.close()

    return json_object
