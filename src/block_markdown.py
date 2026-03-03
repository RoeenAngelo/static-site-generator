def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []

    for block in blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            filtered_blocks.append(stripped_block)
    return filtered_blocks
