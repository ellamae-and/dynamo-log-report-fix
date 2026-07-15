from pathlib import Path
import json
import re
from collections import Counter


def test_report_exists():
    """Criterion 1: the agent produced a report file at /app/report.json."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_values_correct():
    """Criterion 2: the report contains the correct total_requests, unique_ips, and top_path."""
    paths, ips, total = Counter(), set(), 0
    with open("/app/access.log") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            total += 1
            ips.add(line.split()[0])
            m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if m:
                paths[m.group(1)] += 1
    expected = {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0],
    }
    actual = json.loads(Path("/app/report.json").read_text())
    assert actual.get("total_requests") == expected["total_requests"]
    assert actual.get("unique_ips") == expected["unique_ips"]
    assert actual.get("top_path") == expected["top_path"]
