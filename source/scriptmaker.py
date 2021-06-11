
version = ""
script1 = "wmic product 'where description='"
script2 = "' uninstall"
script3 = "&&"


def set_version(version):
    versionsuffix = "v" + version
    return versionsuffix


# Takes a list and generates string command through concatenation
def gen_scriptlist(appnames, version):
    newver = set_version(version)
    cmdlist = []
    for app in appnames[0]:
        if appnames[0].index(app) == len(appnames[0])-1:
            cmd = script1 + app + " " + newver + script2
        else:
            cmd = script1 + app + " " + newver + script2 + " " + script3 + " "
        cmdlist.append(cmd)

    return cmdlist

def listtocommand(cmdlist):
    fullcommand = ''.join(cmdlist)
    return fullcommand



def gen_scriptfile(fullcommand):
    with open("../scriptoutput/uninstallscript.txt", "w") as f:
        f.write(fullcommand)

