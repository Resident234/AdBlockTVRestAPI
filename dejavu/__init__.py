from dejavu.database import get_database, Database
import multiprocessing
import os
import traceback
import sys
import logging
import datetime


class Dejavu(object):
    SONG_ID = "song_id"
    SONG_NAME = 'song_name'
    CONFIDENCE = 'confidence'
    MATCH_TIME = 'match_time'
    OFFSET = 'offset'
    OFFSET_SECS = 'offset_seconds'
    DEFAULT_FS = 44100
    DEFAULT_WINDOW_SIZE = 4096
    DEFAULT_OVERLAP_RATIO = 0.5

    def __init__(self, config):
        super(Dejavu, self).__init__()

        self.config = config

        # initialize db
        db_cls = get_database(config.get("database_type", None))

        self.db = db_cls(**config.get("database", {}))
        self.db.setup()

        # if we should limit seconds fingerprinted,
        # None|-1 means use entire track
        self.limit = self.config.get("fingerprint_limit", None)
        if self.limit == -1:  # for JSON compatibility
            self.limit = None

    def get_num_songs(self):
        return self.db.get_num_songs()

    def find_hashes(self, hashes):
        return self.db.return_matches(hashes)

    def align_matches(self, matches):
        """
            Finds hash matches that align in time with other matches and finds
            consensus about which hashes are "true" signal from the audio.

            Returns a dictionary with match information.
        """
        # align by diffs
        diff_counter = {}
        largest = 0
        largest_count = 0
        song_id = -1
        for tup in matches:
            sid, diff = tup
            if diff not in diff_counter:
                diff_counter[diff] = {}
            if sid not in diff_counter[diff]:
                diff_counter[diff][sid] = 0
            diff_counter[diff][sid] += 1

            if diff_counter[diff][sid] > largest_count:
                largest = diff
                largest_count = diff_counter[diff][sid]
                song_id = sid

        # extract idenfication
        song = self.db.get_song_by_id(song_id)
        if song:
            # TODO: Clarify what `get_song_by_id` should return.
            songname = song.get(Dejavu.SONG_NAME, None)
        else:
            return None

        # return match info
        nseconds = round(float(largest) / Dejavu.DEFAULT_FS *
                         Dejavu.DEFAULT_WINDOW_SIZE *
                         Dejavu.DEFAULT_OVERLAP_RATIO, 5)
        song = {
            Dejavu.SONG_ID: song_id,
            Dejavu.SONG_NAME: songname,
            Dejavu.CONFIDENCE: largest_count,
            Dejavu.OFFSET: int(largest),
            Dejavu.OFFSET_SECS: nseconds,
            Database.FIELD_FILE_SHA1: song.get(Database.FIELD_FILE_SHA1, None), }
        return song

    def find_hashes(self, hashes, *options, **kwoptions):
        r = recognizer(self)
        return r.recognize(*options, **kwoptions)

def chunkify(lst, n):
    """
    Splits a list into roughly n equal parts.
    http://stackoverflow.com/questions/2130016/splitting-a-list-of-arbitrary-size-into-only-roughly-n-equal-parts
    """
    return [lst[i::n] for i in xrange(n)]
