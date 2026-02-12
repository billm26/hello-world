#!/usr/bin/env python3
"""Dance, Clawd! A fun ASCII animation of Clawd dancing."""

import time
import os

FRAMES = [
    r"""
      ╔══════════════════╗
      ║   DANCE CLAWD!   ║
      ╚══════════════════╝

           \o/
            |
           / \
    """,
    r"""
      ╔══════════════════╗
      ║   DANCE CLAWD!   ║
      ╚══════════════════╝

          \o>
           |\
          / |
    """,
    r"""
      ╔══════════════════╗
      ║   DANCE CLAWD!   ║
      ╚══════════════════╝

           _o_
          / | \
            |
    """,
    r"""
      ╔══════════════════╗
      ║   DANCE CLAWD!   ║
      ╚══════════════════╝

          <o/
          /|
          | \
    """,
    r"""
      ╔══════════════════╗
      ║   DANCE CLAWD!   ║
      ╚══════════════════╝

           \o/
            |
           | |
    """,
    r"""
      ╔══════════════════╗
      ║   DANCE CLAWD!   ║
      ╚══════════════════╝

          >o<
           |
          / \
    """,
    r"""
      ╔══════════════════╗
      ║   DANCE CLAWD!   ║
      ╚══════════════════╝

           \o/
            |>
           / \
    """,
    r"""
      ╔══════════════════╗
      ║   DANCE CLAWD!   ║
      ╚══════════════════╝

          <o>
          <|
           / \
    """,
]

MOVES = [
    "~ the robot ~",
    "~ disco fever ~",
    "~ the wave ~",
    "~ funky chicken ~",
    "~ the shuffle ~",
    "~ jazz hands ~",
    "~ the spin ~",
    "~ moonwalk ~",
]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def dance(loops=3):
    """Make Clawd dance!"""
    print("\n  Clawd is warming up...\n")
    time.sleep(1)

    for loop in range(loops):
        for i, frame in enumerate(FRAMES):
            clear_screen()
            print(frame)
            print(f"        {MOVES[i]}")
            print(f"\n      [ Loop {loop + 1}/{loops} ]")
            time.sleep(0.4)

    clear_screen()
    print(
        r"""
      ╔══════════════════════════╗
      ║  CLAWD'S DANCE IS DONE  ║
      ╚══════════════════════════╝

             \o/
              |
             / \

          * * * * *
        *  BRAVO!  *
          * * * * *
    """
    )


if __name__ == "__main__":
    dance()
