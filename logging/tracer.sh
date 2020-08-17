#!/bin/bash

while true; do
	(printf "start: "; date "+%D %T";
	 traceroute google.com;
	 printf "end: "; date "+%D %T"; printf "\n") >> ~/TRACE_LOG.TXT
done
