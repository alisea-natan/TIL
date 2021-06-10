#! /bin/bash

pict task.txt | jq -sR '[sub("\n$";"") | splits("\n") | sub("^ +";"") | [splits("\t")]] | .[0] as $header | .[1:] | [.[] | [. as $x | range($header | length) | {"key": $header[.], "value": $x[.]}] | from_entries]'