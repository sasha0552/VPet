#!/usr/bin/env python3

import json
import os
import sys

from PIL import Image

def main():
  # Load manifest
  with open(os.path.join("assets", "manifest.json"), "r") as file:
    manifest = json.load(file)

  # Create spritesheets directory
  os.makedirs(os.path.join("assets", "spritesheets"), exist_ok=True)

  # Iterate over keys
  for _group_name, _states in manifest.items():
    for _state_name, _animations in _states.items():
      # Dictionary of state animations
      animations = {}

      # Iterate over animations
      for _animation_name, _animation_path in _animations.items():
        # Check that directory exists
        if not os.path.exists(_animation_path):
          print(f"Directory for animation {_animation_name} does not exists ({_animation_path})", file=sys.stderr)
          continue

        # List of animation frames
        frames = []

        # Load frames
        for _frame_name in sorted(os.listdir(_animation_path)):
          # Frame path
          path = os.path.join(_animation_path, _frame_name)

          # Load image
          image = Image.open(path)

          # Get image width and height
          width, height = image.size

          # Ensure that image is 1000x1000
          if width != 1000 or height != 1000:
            print(f"Invalid image size: {width}x{height} ({path})", file=sys.stderr)

          # Append image
          frames.append(image)

        # Insert animation
        animations[int(_animation_name)] = frames

      # Number of max cols
      max_cols = 0

      # Number of max rows
      max_rows = 0

      # Create metadata
      for index, frames in animations.items():
        # Get count of columns
        cols = len(frames)

        # If higher that max_cols, then set new max_cols
        if cols > max_cols:
          max_cols = cols

        # Increment rows
        max_rows += 1

      # Create spritesheet
      spritesheet = Image.new("RGBA", (max_cols * 1000, max_rows * 1000))

      # Place frames on spritesheet
      for i in range(max_rows):
        for j in range(len(animations[i])):
          spritesheet.paste(animations[i][j], (j * 1000, i * 1000))

      # Save spritesheet
      spritesheet.save(os.path.join("assets", "spritesheets", f"{_group_name}-{_state_name}.png"))

if __name__ == "__main__":
  main()
