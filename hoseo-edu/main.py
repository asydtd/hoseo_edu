#!/usr/bin/python
# -*- coding: utf-8 -*-
print("module [app] loaded")
import os

from backend import app

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    #app.run("0.0.0.0", debug=False, port=port, threaded=False)
    app.run("0.0.0.0", debug=True, port=port, threaded=True)