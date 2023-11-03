extends Node

const HEIGHT = 4.0

const X = -2.0
const Y = -1.732

var x = X
var y = Y

const STEP = .8

enum {
	NONE,
	Y_MINUS,
	Y_PLUS,
	X_MINUS,
	X_PLUS,
}

var _action = NONE

var _base
var _mount

func _get_mount_rotation(x, y):
	var dist = sqrt(x*x + y*y)
	var ang = atan(dist/HEIGHT)
	if x < 0:
		return -ang
	return ang


func _get_base_rotation(x, y):
	if x == 0:
		return 0
	print("atan ", atan(y/x))
	return -atan(y/x)

func _ready():
	_base = get_node("/root/root/base")
	_mount = get_node("/root/root/base/braket/mount")
	
	_move_to(x, y)

func _move_to(x, y):
	var base_rot = _get_base_rotation(x, y)
	var mount_rot = _get_mount_rotation(x, y)
	print("x ", x , " y ", y, " base ", base_rot, " mount ", mount_rot)

	_base.set_rotation(Vector3(0, base_rot, 0))
	_mount.set_rotation(Vector3(0, 0, mount_rot))

func _process(time_delta):
	if _action == NONE:
		return
		
	match _action:
		X_MINUS:
			x -= time_delta * STEP
		X_PLUS:
			x += time_delta * STEP
		Y_MINUS:
			y -= time_delta * STEP
		Y_PLUS:
			y += time_delta * STEP
			
	_move_to(x, y)
	
func _input(event):
	if not event is InputEventKey:
		return

	if not event.pressed:
		_action = NONE
		return

	match event.keycode:
		KEY_UP:
			_action = Y_MINUS
		KEY_DOWN:
			_action = Y_PLUS
		KEY_LEFT:
			_action = X_MINUS
		KEY_RIGHT:
			_action = X_PLUS
