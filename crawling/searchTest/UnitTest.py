# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os

if os.getuid() == 0:
    pass
else:
    print ''
    sys.exit(1)

version = raw_input('')
