from flask_src.camera import bp
from flask_src.camera.controller import camera_capture

@bp.route("/camera")
def initialize():
  camera_capture()
  return "camera iniciada"