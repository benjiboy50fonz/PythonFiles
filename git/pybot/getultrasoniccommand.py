from wpilib.command.instantcommand import InstantCommand
import subsystems


class GetUltrasonicCommand(InstantCommand):

    def __init__(self):
        super().__init__('GetUltrasonic')
        self.setRunWhenDisabled(True)

    def initialize(self):
        print(subsystems.drivetrain.getFrontClearance())
