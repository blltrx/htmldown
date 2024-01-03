# welcome to htmlconfig.py!

# change lines between """ to edit
# when editing the createPageString function use f string syntax. surround variable name in {curly braces}
# constant variables should be names clearly in ALL CAPS
# with the exception of TOP, it's suggested to keep a tab (4 spaces in python3) in front of each line

ROOT = "C:/Users/rozec/Documents/code/mdweb framework/site"

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

# defines page structure, does not check css
def createPageString(contentstring:str) -> str:
    "outputs html page with parameters in 'htmlconfig.py', with content defined in an input string in html format"
    return f"""
{TOP}
<head>
{HEADERS}
</head>

<body>
{TOPBAR}
<div class="contentWrap">
{contentstring}
{FOOTER}
</div>
</body>
</html>
"""

def createPageStringExcludeExtraBody(contentstring:str) -> str:
    "outputs html page with parameters in 'htmlconfig.py', with content defined in an input string in html format. DOES NOT add a navigation 'TOPBAR' or 'FOOTER' to <body>"
    return f"""
{TOP}
<head>
{HEADERS}
</head>

<body>
<div class="contentWrap">
{contentstring}
</div>
</body>
</html>
"""
