print("Starting")

import board

#import from kmk library
from kb import KMKKeyboard
from kmk.keys import KC
from kmk.hid import HIDModes
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())

keyboard = KMKKeyboard()

#knobssss
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.GP17, board.GP15, board.GP14,),
)

keyboard.keymap = [  # qwerty
        KC.ESC,    KC.N1,     KC.N2,     KC.N3,     KC.N4,     KC.N5,          KC.N6,     KC.N7,     KC.N8,     KC.N9,     KC.N0,     KC.MINS, KC.EQL, KC.BSPACE,
        KC.TAB,   KC.Q,      KC.W,      KC.E,      KC.R,      KC.T,           KC.Y,      KC.U,      KC.I,      KC.O,      KC.P,     KC.LBRC, KC.RBRC, KC.BSLS,
        KC.CAPS,    KC.A,      KC.S,      KC.D,      KC.F,      KC.G,           KC.H,      KC.J,      KC.K,      KC.L,      KC.SCLN,   KC.QUOT, KC.ENT,
        KC.LSFT,   KC.Z,      KC.X,      KC.C,      KC.V,      KC.B,           KC.N,      KC.M,      KC.COMM,   KC.DOT,    KC.SLSH,   KC.RSFT,          KC.UP,
        KC.HOME,   KC.LCTL,    KC.LALT,   KC.LCMD,   KC.SPACE,   KC.RCMD,        KC.RALT,                                                 KC.LEFT, KC.DOWN, KC.RIGHT,
    ],

encoder_handler.map = [
    (KC.VOLD, KC.VOLU, KC.MEDIA_PLAY_PAUSE),
],


if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE, ble_name='Rabbitboard')

