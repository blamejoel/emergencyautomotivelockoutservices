#!/bin/bash
# echo "polymer build --sources index.html src/ images/ manifest.json favicon.ico browserconfig.xml"
# polymer build --sources index.html src/ images/ manifest.json favicon.ico browserconfig.xml

echo "polymer build --sources index.html manifest.json favicon.ico browserconfig.xml"
polymer build --sources index.html manifest.json favicon.ico browserconfig.xml --name unbundled

echo "cp -R images/ build/bundled"
cp -R images/ build/bundled

echo "cp -R images/ build/unbundled"
cp -R images/ build/unbundled

echo "done!"
