"""Registration for the separately installed EmbodiAgent Nero adapter."""
from embodiagent_coding.pyrualean.robot import NeroRobot

from .robots import RobotAdapter

ADAPTER = RobotAdapter(
    name="embodi_nero",
    robot_cls=NeroRobot,
    host="embodiagent_coding.pyrualean.host",
    knowledge="embodi_nero",
    blurb="a real Nero workcell observed through its chest camera",
    services="a point-prompt SAM3 segmentation service",
    services_novla="a point-prompt SAM3 segmentation service",
    show_examples="display(robo.image('chest_rgbd', snapshot_id=sid))",
)
