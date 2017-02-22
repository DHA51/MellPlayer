#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Netease Music Player

Created on 2017-02-20
@author: Mellcap
'''

from .mpv import MPV
from .api import Netease

class Player(MPV):

    def __init__(self):
        self.category = None
        self.category_playlists = None
        self.playlist = None

    def init_playlist(self):
        self.loadlist('/Users/zhaoye/test_dir/test001.m3u')

    def start_or_pause(self):
        if self.pause:
            self._set_property('pause', False)
        else:
            self._set_property('pause', True)

    def switch_song(self, action='next'):
        '''
        action: next/prev
        '''
        if action == 'next':
            self.playlist_next()
        elif action == 'prev':
            self.playlist_prev()

    def switch_playlist(self):
        # find playlists
        # choose playlist != this
        # return
        pass

    def get_category_playlists(self):
        category = self.category
        if category:
            data = Netease.category_playlists(category=category)
            category_playlists = Netease.parse_info(data=data, parse_type='category_playlists')
            return category_playlists
        return False

    def get_playlist(self, category_playlists, playlist_index=0):
        playlist_id = category_playlists[playlist_index]['playlist_id']
        data = Netease.playlist_detail(playlist_id)
        playlist_detail = Netease.parse_info(data=data, parse_type='playlist_detail')
        return playlist_detail
        
            
            
