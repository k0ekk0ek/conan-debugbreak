#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os
import re


class DebugbreakConan(ConanFile):
    name = "debugbreak"
    version = "16072017"
    description = "Break into the debugger programmatically"
    url = "https://github.com/k0ekk0ek/conan-debugbreak"
    homepage = "https://github.com/scottt/debugbreak"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ['include/*']
    source_subfolder = "source_subfolder"
    no_copy_source = True

    branch = "master"
    commit = "7ee9b29208c2c5aad8a935334062a87c738b6aa4"

    def source(self):
        self.run("git clone --branch={0} {1}.git {2}"
            .format(self.branch, self.homepage, self.source_subfolder))
        self.run("git -C {0} checkout {1}"
            .format(self.source_subfolder, self.commit))

    def package(self):
        self.copy(pattern='COPYING', dst='licenses', src=self.source_subfolder)
        self.copy(pattern='*/debugbreak.h', dst='include', keep_path=False)
        # FIXME: Not sure if this is the proper location. Automatic loading is
        #        probably out of the question, but maybe CMake integration can
        #        be done?
        self.copy(pattern='*/debugbreak-gdb.py', dst='share', keep_path=False)

