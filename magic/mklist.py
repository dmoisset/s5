import sys
from typing import List, NamedTuple

import yaml


class Document(NamedTuple):
    filename: str
    name: str  # as declared in YAML
    title: str  # As described in markdown file
    level: int
    caster_class: List[str]


documents = []
for filename in sys.argv[1:]:
    # sys.stderr.write(f"Parsing {filename}\n")
    with open(filename, "r") as f:
        data = f.read()
    metadata = next(yaml.load_all(data))
    titles = [line for line in data.split("\n") if line.startswith("#")]
    title = titles[0]
    assert title.startswith("# ")
    title = title[len("# ") :].rstrip()
    for caster_class in metadata["classes"].split():
        documents.append(
            Document(filename, metadata["name"], title, metadata["level"], caster_class)
        )

documents.sort(key=lambda d: (d.caster_class, d.level, d.name))

output = sys.stdout

level_titles = [
    "Cantrips (0 Level)",
    "1st Level",
    "2nd Level",
    "3rd Level",
    "4th Level",
    "5th Level",
    "6th Level",
    "7th Level",
    None,
    "9th Level (special)",
]

current_class = None
current_level = None
for d in documents:
    if d.caster_class != current_class:
        current_class = d.caster_class
        current_level = None
        output.write(f"\n# {current_class.title()} Spells\n")
    if d.level != current_level:
        current_level = d.level
        output.write(f"\n## {level_titles[current_level]}\n\n")
    output.write(f"- [{d.title}]({d.filename})\n")
