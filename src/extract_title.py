def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            heading = line[1:].strip()
            return heading
    raise Exception("No header found")