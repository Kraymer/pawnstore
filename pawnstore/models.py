#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime as dt
import confuse
import sys

from os import path
from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    IntegerField,
    BooleanField,
    DateTimeField,
    FloatField,
)
from playhouse.shortcuts import model_to_dict

DB = None


def database_path():
    config = confuse.Configuration("pawnstore", __name__)
    dbname = "pawnstore.sqlite"
    return path.join(config.config_dir(), dbname)


def database():
    if "pytest" in sys.modules:
        return SqliteDatabase(":memory:")
    return SqliteDatabase(database_path())


class Game(Model):
    slug = CharField(unique=True)

    analysis = CharField(null=True)
    eco = CharField()
    eco_name = CharField(null=True)
    elo = IntegerField(null=True)
    moves = CharField()
    num_moves = IntegerField(null=True)
    opp_elo = IntegerField()
    opp_name = CharField()
    pgn = CharField(null=True)
    result = CharField(null=True)
    termination = CharField(null=True)
    speed = CharField()
    term = CharField(null=True)
    timestamp = DateTimeField()
    user = CharField()
    accuracy = FloatField(null=True)
    time_control = CharField()
    website = CharField()
    white = BooleanField()
    searchable_fields = ("eco", "opp_name", "website", "white")

    class Meta:
        database = database()
        indexes = (
            # create a unique on from/to/date
            (("slug", "website", "user"), True),
        )

    def as_dict(self):
        return model_to_dict(self)

    def __str__(self):
        if self.white:
            return f"{self.user} x {self.opp_name}"
        return f"{self.opp_name} x {self.user}"


# Initialize database
database().create_tables([Game])
