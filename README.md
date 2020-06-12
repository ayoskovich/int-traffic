# int-traffic
Analyzing internet traffic.

# Main Questions
- How does my internet speed vary over time?
- Is there a lot of variance? little?
- Does time of day affect it?
- Does where the traffic is going matter?

# Ideas
- Timestamp `ping` and `traceroute` 
  - Merge on time stamp to control for different hops
    - Is there variability in traceroute hops?


---


# Dashboards

## Ping
- Histogram of all pings
- Autocorrelation (past X)
- Pings over time (raw, avg, median, std)

## Traceroute
- Histogram of all times
- Visualize route somehow?	
- Distribution of whereto address?
- Distribution of * records

