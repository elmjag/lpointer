extends Node

const PORT = 9000
var tcp_server := TCPServer.new()
var conn = null
var _base
var _mount

func _ready():
	_base = get_node("/root/root/base")
	_mount = get_node("/root/root/base/braket/mount")
	
	var res = tcp_server.listen(PORT, "0.0.0.0")
	if res != OK:
		print("Unable to start server.")
		set_process(false)


func _process(delta):
	while tcp_server.is_connection_available():
		conn = tcp_server.take_connection()
		print("GOT CONNECTION!", conn)
	
	if conn != null && conn.get_available_bytes() >= 4:
		var base_rot = conn.get_float()
		var mount_rot = conn.get_float()
		print("base ", base_rot, " mount ", mount_rot)
		
		_base.set_rotation_degrees(Vector3(0, base_rot, 0))
		_mount.set_rotation_degrees(Vector3(0, 0, mount_rot))
