import sys
from absl import app
from absl import flags
from typing import Any
from randomizer import ZoraRandomizer

flags.DEFINE_integer(name='seed', default=0, help='The seed number to initialize RNG with.')
flags.DEFINE_string(name='input_filename',
                    default='',
                    help='The filename of the vanilla ROM to randomize.')
flags.DEFINE_string(name='output_location',
                    default='',
                    help='The location to put the randomized ROM.')
flags.DEFINE_enum(
    'text_speed',
    'normal',
    ['very_fast', 'fast', 'normal', 'slow', 'very_slow', 'random'],
    'How fast the text speed will go. Fast speed is, well, fast, but slower speed allows for '
    'resetting door repair charges.',
)

# TODO: Turn this enum into a string with lambda validation.
flags.DEFINE_enum('level_text', 'level-',
                  ['level-', 'house-', 'block-', 'random', 'cage_-', 'home_-', 'castle'],
                  'What are the dungeons called? This is strictly for fun.')

FLAGS = flags.FLAGS


def main(unused_argv: Any) -> None:
  z1randomizer = ZoraRandomizer()
  z1randomizer.Settings(FLAGS.input_filename, FLAGS.output_location, FLAGS.seed)
  z1randomizer.Run()


if __name__ == '__main__':
  app.run(main)
