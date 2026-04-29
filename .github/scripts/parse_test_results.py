#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: parse_test_results.py <results.xml>", file=sys.stderr)
        return 2

    xml_path = sys.argv[1]
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # The top-level <testsuite> may be the root, or wrapped in <testsuites>.
    suite = root if root.tag == "testsuite" else root.find("testsuite")
    if suite is None:
        print("0/0")
        return 0

    # Prefer score/max_score from testsuite-level properties (set by scoring plugin).
    score = None
    max_score = None
    props = suite.find("properties")
    if props is not None:
        prop_map = {p.attrib["name"]: p.attrib["value"] for p in props}
        if "score" in prop_map and "max_score" in prop_map:
            score = int(prop_map["score"])
            max_score = int(prop_map["max_score"])

    if score is not None and max_score is not None:
        print(f"{score}/{max_score}")
    else:
        # Fall back to raw pass/fail counts when the scoring plugin wasn't used.
        tests = int(suite.attrib.get("tests", 0))
        errors = int(suite.attrib.get("errors", 0))
        failures = int(suite.attrib.get("failures", 0))
        skipped = int(suite.attrib.get("skipped", 0))
        passed = tests - errors - failures - skipped
        print(f"{passed}/{tests}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
