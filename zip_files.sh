#!/bin/bash

cd "${1}"

zip -r "${1}.zip" *

mv "${1}.zip" ../
