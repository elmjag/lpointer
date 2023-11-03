extends MeshInstance3D

const TILT_SPEED = 0.15
const ROT_SPEED = 1.4

enum {
	NONE,
	TILT_POS,
	TILT_NEG,
	ROT_POS,
	ROT_NEG,
}

var _action = NONE

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func _process(time_delta):
	match _action:
		TILT_POS:
			rotate_z(TILT_SPEED * time_delta)
		TILT_NEG:
			rotate_z(-TILT_SPEED * time_delta)
		ROT_POS:
			rotate_y(ROT_SPEED * time_delta)
		ROT_NEG:
			rotate_y(-ROT_SPEED * time_delta)


func _input(event):
	if not event is InputEventKey:
		return

	if not event.pressed:
		_action = NONE
		return

	match event.keycode:
		KEY_A:
			_action = TILT_NEG
		KEY_D:
			_action = TILT_POS
		KEY_W:
			_action = ROT_POS
		KEY_S:
			_action = ROT_NEG

