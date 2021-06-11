import csvuploader
import scriptmaker


def main():
    version = input("Please enter version :")
    appnames = csvuploader.uploadcsv(csvuploader.appnamefilepath)

    cmdlist = scriptmaker.gen_scriptlist(appnames, version)

    fullcommand = scriptmaker.listtocommand(cmdlist)

    scriptmaker.gen_scriptfile(fullcommand)


if __name__ == '__main__':
    main()
