def display_box(word):
  num_dashes = 4 + len(word)
  print("-" * num_dashes)
  print(f"| {word} |")
  print("-" * num_dashes)