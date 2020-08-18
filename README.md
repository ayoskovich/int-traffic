# int-traffic
Code that accompanies a personal project on my website [here](https://anthonyyoskovich.com/project/internet-traffic/). Over the course of a month or so I logged the output from `ping` and `traceroute` to google.com in order to analyze internet traffic.

---

## About The Files

- `analyze_ping.ipynb`: Main notebook for analysis
- `*_helps.ipynb`: Notebooks containing functions and useful code I didn't want inside the main analysis notebook
- `/src`: Contains jupyter notebooks converted to python code to make diffs way easier to read
- `/dashboards`: Contains some jupyter notebooks and early exploratory work
- `/data`: Contains the raw text files created by `ping` and `traceroute`
- `/logging`: Contains the crontab file I used to schedule the logging, as well as the bash script used to automate `traceroute`
