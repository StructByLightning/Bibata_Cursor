#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clickgen import build_cursor_theme, build_win_cursor_theme, build_x11_cursor_theme

from .bundler import Bundler
from .config import ConfigProvider, delay, hotspots, sizes


class CursorBuilder:
    """
    Build Bibata Windows & X11 cursors 🚀.
    """

    def __init__(self, config: ConfigProvider) -> None:
        self.__name = config.name
        self.__bitmaps_dir = config.bitmaps_dir
        self.__bundler = Bundler(config)
        self.__tmpdir = config.tmpdir

    def build_x11_cursors(self) -> None:
        """ Build `x11` platform cursors. """
        print("🌈 Building %s Theme ..." % self.__name)
        build_x11_cursor_theme(
            name=self.__name,
            image_dir=self.__bitmaps_dir,
            cursor_sizes=sizes,
            hotspots=hotspots,
            out_path=self.__tmpdir,
            archive=False,
            delay=delay,
        )

        self.__bundler.x11_bundle()

    def build_win_cursors(self) -> None:
        """ Build `Windows` platform cursors. """
        print("🌈 Building %s Theme ..." % self.__name)
        build_win_cursor_theme(
            name=self.__name,
            image_dir=self.__bitmaps_dir,
            cursor_sizes=sizes,
            hotspots=hotspots,
            out_path=self.__tmpdir,
            archive=False,
            delay=delay,
        )

        self.__bundler.win_bundle()

    def build_cursors(self) -> None:
        """ Build `x11` & `Windows` platform cursors. """
        print("🌈 Building %s Theme ..." % self.__name)
        build_cursor_theme(
            name=self.__name,
            image_dir=self.__bitmaps_dir,
            cursor_sizes=sizes,
            hotspots=hotspots,
            out_path=self.__tmpdir,
            archive=False,
            delay=delay,
        )

        self.__bundler.bundle()
