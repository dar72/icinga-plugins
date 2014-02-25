#!/usr/bin/python
# Requires 'pacman -Sy' in cron
import os, sys
updates_list = os.popen('pacman -Qu').read()
updates_list = updates_list.splitlines()
updates = len(updates_list)
updates_csv = ",".join(updates_list )

if updates == 0:
        print("OK - No updates available")
        sys.exit(0)
elif updates > 0:
        print("WARNING - {} updates available: {}".format(updates, updates_csv))
        sys.exit(1)
else:
        print("UNKNOWN - {} updates available: {}".format(updates, updates_csv))
        sys.exit(3)
