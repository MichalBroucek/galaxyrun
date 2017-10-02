#!/bin/bash

# buildozer target command

#buildozer android clean
#buildozer android update
#buildozer android deploy
#buildozer android debug
#buildozer android release

# or all in one (compile in debug, deploy on device)
buildozer android debug deploy

# set the default command if nothing set
#buildozer setdefault android debug deploy run
