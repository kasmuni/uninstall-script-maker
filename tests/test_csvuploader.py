import source.csvuploader
import source.scriptmaker

def test_csvupload():
    appnamefilepath = './data/appnames.csv'
    expapplist = [['Microsoft Windows', ' Microsoft Office', ' Microsoft Excel']]
    actapplist = source.csvuploader.uploadcsv(appnamefilepath)
    assert expapplist == actapplist


def test_versionsetter():
    version = "5.6.103.1"
    setversion = source.scriptmaker.set_version(version)
    assert setversion == "v5.6.103.1"


def test_scriptmaker_genscript():
    appnames = [['Microsoft Windows', ' Microsoft Office', ' Microsoft Excel']]
    version = "7.6.103.1"
    actscript = source.scriptmaker.gen_scriptlist(appnames,version)
    expscript = ["wmic product 'where description='Microsoft Windows v7.6.103.1' uninstall && ", "wmic product 'where description=' Microsoft Office v7.6.103.1' uninstall && ", "wmic product 'where description=' Microsoft Excel v7.6.103.1' uninstall"]
    assert actscript == expscript


def test_listtocommand():
    cmdlist = ["wmic product 'where description='Microsoft Windows v7.6.103.1' uninstall && ", "wmic product 'where description=' Microsoft Office v7.6.103.1' uninstall && ", "wmic product 'where description=' Microsoft Excel v7.6.103.1' uninstall"]
    expcmd = "wmic product 'where description='Microsoft Windows v7.6.103.1' uninstall && wmic product 'where description=' Microsoft Office v7.6.103.1' uninstall && wmic product 'where description=' Microsoft Excel v7.6.103.1' uninstall"
    actcmd = source.scriptmaker.listtocommand(cmdlist)
    assert expcmd == actcmd


def test_gen_scriptfile():
    fullcommand = "wmic product 'where description='Microsoft Windows v7.6.103.1' uninstall && wmic product 'where description=' Microsoft Office v7.6.103.1' uninstall && wmic product 'where description=' Microsoft Excel v7.6.103.1' uninstall"
    source.scriptmaker.gen_scriptfile(fullcommand)



