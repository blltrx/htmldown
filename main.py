import sys
import markdown as md
import htmlconfig as html

HELP_MESSAGE = """
python main.py <markdown path> <arguments>
    -o <output path> : uses stated output path instead of YAML frontmatter
    -v               : verbose, displaces [DEBUG] infomation
    -r <root path>   : uses stated root path for output instead of 'htmlconfig.py'
    --exclude-extra  : DOES NOT add a navigation 'TOPBAR' or 'FOOTER' to <body> in final output
requires htmlconfig.py createPageStringExcludeExtraBody() and createPageString() methods.
"""

DEBUG = False
EXCLUDE_EXTRA = False
path = ""
root = ""

# argument definitions
argvars = sys.argv[1:]
infile = argvars[0]
if "-v" in argvars:
    DEBUG = True
if "--exclude-extra" in argvars:
    EXCLUDE_EXTRA = True
if "-r" in argvars:
    root = argvars[argvars.index("-r")+1]
if "-o" in argvars:
    path = argvars[argvars.index("-o")+1]
if "-h" in argvars or "--help" in argvars:
    print(HELP_MESSAGE)
    sys.exit(0)

def seperate_yaml(filestring: str) -> tuple[dict[str,str],str]:
    "extracts YAML heading from filestring, and returns YAML as a dictionary and filestring with YAML header removed"
    startindex = filestring.find("---")
    endindex = filestring.find("---",5)
    yaml = ""
    body = ""
    if startindex != 0:
        return ({"":""}, filestring)
    yamlstring = filestring[startindex+4:endindex-1]
    yaml = dict(subString.split(": ") for subString in yamlstring.split("\n"))
    body = filestring[endindex+4:]
    return (yaml, body)

def convert(inputpath:str) -> tuple[dict[str,str],str]: # depends on seperate_yaml
    "takes a path to a plain text file in markdown, and outputs an html page based on 'htmlconfig.py'"
    with open(inputpath, "r") as f:
        filestring = f.read()
        f.close()
    if DEBUG: print(f"[DEBUG]: reading file {inputpath}")
    yaml, bodymd = seperate_yaml(filestring)
    html_content_string = md.markdown(bodymd)

    if DEBUG: print(f"[DEBUG]: extracted YAML heading {yaml}")
    if DEBUG: print(f"[DEBUG]: converted body to html")
    if EXCLUDE_EXTRA:
        pagestring = html.createPageStringExcludeExtraBody(html_content_string)
    else: pagestring = html.createPageString(html_content_string)
    return yaml, pagestring

def main() -> None:
    global path, root
    yaml, pagestring = convert(infile)

    if DEBUG: print(f"[DEBUG]: attempting to save file")
    try:
        if path == "":
            path = yaml['path']
        else:
            sys.exit("[ERROR]: 'path' not specified, please use -o <output path>")
        if root == "":
            root = html.ROOT
        outputpath = f"{root}/{path}"
        with open(outputpath, "w") as f:
            f.write(pagestring)
            f.close()
        print(f"output at '{outputpath}'")
    except FileNotFoundError as exception:
        if DEBUG:
            print(f"[DEBUG]: {exception}")
            sys.exit("[ERROR]: Directory path invalid. Check it exists, if not create it.")
        else:
            sys.exit("[ERROR]: Directory path invalid. Check it exists, if not create it. Run with -v for DEBUG infomation")

if __name__ == "__main__":
    main()