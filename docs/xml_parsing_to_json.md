# XML Parsing to JSON

This document describes how `dsa/convert_sms_to_json.py` reads `dsa/modified_sms_v2-1.xml` and writes `dsa/sms_records.json`.

## Overview

The converter uses Python's standard-library `xml.etree.ElementTree` module to parse the XML. It creates one JSON object for each direct `<sms>` child of the XML root. Each object's properties are copied from that element's XML attributes without further interpretation or cleanup.

## Parsing flow

1. `main()` uses `Path(__file__).parent` to find the directory containing the script. This makes the input and output paths independent of the current working directory.
2. The input path is set to `modified_sms_v2-1.xml` in that directory.
3. `parse_sms_xml()` calls `ET.parse(xml_path).getroot()` to parse the document and get its root element (`<smses>` in this dataset).
4. It searches the root for direct children named `<sms>` using `root.findall("sms")`.
5. For each matching element, `dict(sms.attrib)` copies all its XML attributes into a Python dictionary. The resulting list of dictionaries is returned in document order.
6. `main()` opens `sms_records.json` in the same directory and writes the list as formatted JSON using `indent=2` and `ensure_ascii=False`.
7. It prints the number of parsed records and the output path.

## Output shape

The output is a JSON array. Each array item represents one `<sms>` element, and each key/value corresponds to one XML attribute. For example, the beginning of the first record is equivalent to:

```json
{
  "protocol": "0",
  "address": "M-Money",
  "date": "1715351458724",
  "type": "1",
  "subject": "null",
  "body": "You have received 2000 RWF from Jane Smith ..."
}
```

XML attributes are strings, so numeric-looking values such as `date`, `type`, and `read` are strings in JSON too. The text `"null"` is also preserved as a string; it is not converted to JSON `null`. The converter does not parse dates, inspect or transform message bodies, rename fields, filter records, or convert values to other types.

## Running the converter

From the repository root, run:

```bash
python3 dsa/convert_sms_to_json.py
```

The script writes or replaces `dsa/sms_records.json`. It expects the input XML to exist at the path beside the script. Invalid or missing XML raises an exception from `ElementTree` or file I/O; the script does not catch those errors.

## Record count note

The XML root has a `count="1693"` attribute, but the current file contains 1,691 direct `<sms>` elements. The converter does not read or validate the root's `count` attribute: it processes only elements returned by `root.findall("sms")`, and the printed count reflects the number of records it parsed.