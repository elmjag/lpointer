extends MeshInstance3D

const SPEED = 0.8

enum {
	NONE,
	POS,
	NEG,
}

var _action = NONE

func _process(time_delta):
	match _action:
		POS:
			rotate_y(SPEED * time_delta)
		NEG:
			rotate_y(-SPEED * time_delta)
	

func _input(event):
	if not event is InputEventKey:
		return

	if not event.pressed:
		_action = NONE
		return

	match event.keycode:
		KEY_A:
			_action = NEG
		KEY_D:
			_action = POS

