#!/bin/bash

while true; do
	(printf "start: "; date +%T;
	 traceroute google.com;
	 printf "end: "; date +%T ; printf "\n") >> FT.TXT
done
