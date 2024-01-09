#!/usr/bin/python3
# welcome to htmlconfig.py!

# change lines between """ to edit
# constant variables should be names clearly in ALL CAPS
# with the exception of TOP, it's suggested to keep a tab (4 spaces in python3) in front of each line

ROOT = "" 

TOP = """
<!DOCTYPE html>
<html lang="en">
"""

HEADERS = """
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta property="og:title" content="blltrx" />
    <meta property="og:image" content="/assets/things.webp" />
    <title>rose / bellatrix</title>
    <link rel="icon" type="image/x-icon" href="/assets/logos.webp">
    <script src=/main.js defer></script>
    <link rel="stylesheet" href="/style.css" />
"""

TOPBAR = """
    <div id="nav" class="center">
      <div id="nav-left">
        <a id="title" href="/">
        rose / bellatrix
        </a>
      </div>
      <div id="nav-right">
      <a href="/" id="nav-link-red">home</a>
      <span>/</span>
      <a href="/projects" id="nav-link-purple">projects</a>
      </div>
    </div>
    <hr>
"""

FOOTER = """

"""
