There is an Apache-style access log at /app/access.log. Parse it and write a
summary report to /app/report.json as a JSON object with these three keys:
total_requests, unique_ips, and top_path.

1. Produce a file at /app/report.json.
2. The file must be valid JSON containing:
   - total_requests: the total number of log lines, as an integer
   - unique_ips: the count of distinct client IP addresses, taken from the
     first field of each line, as an integer
   - top_path: the single most frequently requested path, extracted from the
     quoted request line (e.g. "GET /index.html HTTP/1.1" -> "/index.html").
     If there's a tie, any of the tied paths is acceptable.
