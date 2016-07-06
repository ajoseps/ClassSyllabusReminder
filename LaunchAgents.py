import os
from os.path import expanduser

home = expanduser("~")
plist = "com.class.syllabus.osx"
plist_path = "{0}/Library/LaunchAgents/{1}.plist".format(home,plist)

if __name__ == "__main__":
    if not os.path.isfile(plist_path):
        program = os.path.join(os.getcwd(), "class_parser.py")
        plist_contents = """ <?xml version="1.0" encoding="UTF-8"?>
                            <!DOCTYPE plist PUBLIC -//Apple Computer//DTD PLIST
                            1.0//EN http://www.apple.com/DTDs/PropertyList-1.0.
                            dtd >
                            <plist version="1.0">
                            <dict>
                            <key>Label</key>
                            <string>{0}</string>
                            <key>Program</key>
                            <string>{1}</string>
                            <key>KeepAlive</key>
                            <true/>
                            </dict>
                            </plist>""".format(plist, program)
        with open(plist_path, 'a+') as f:
            f.write(plist_contents)

    # run script