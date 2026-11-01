from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter
)

text = """
The detective entered the abandoned house just before the midnight. The rooms were silent, and the windows were covered with dust. On the table, he found a bloodstained letter that mentioned a secret meeting.

The man who did the crime was John. Nobody in the village trusted him, but he had disappeared three days before the murder. The detective immediately realized that John has left behind one important clue.

The next morning, the detective returned to the house. Behind a loose brick, he discovered a photograph John standing behind the victim. This finally connected John to the crime.
"""

# 1. Fixed-Size Chunking
fixed = CharacterTextSplitter(
    separator="",
    chunk_size=100,
    chunk_overlap=0
)

print("\n", "=" * 10, "FIXED SIZE", "=" * 10)

for i, chunk in enumerate(fixed.split_text(text), 1):
    print(f"\nChunk {i}:")
    print(chunk)
    print("=" * 50)


# 2. Paragraph Chunking
paragraph = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=100,
    chunk_overlap=0
)

print("\n", "=" * 10, "PARAGRAPH", "=" * 10)

for i, chunk in enumerate(paragraph.split_text(text), 1):
    print(f"\nChunk {i}:")
    print(chunk)
    print("=" * 50)


# 3. Recursive Chunking
recursive = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

print("\n", "=" * 10, "RECURSIVE", "=" * 10)

for i, chunk in enumerate(recursive.split_text(text), 1):
    print(f"\nChunk {i}:")
    print(chunk)
    print("=" * 50)
