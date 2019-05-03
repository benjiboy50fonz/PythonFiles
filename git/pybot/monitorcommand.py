from wpilib.command import Command
from wpilib.timer import Timer
from networktables import NetworkTables

import math
import subsystems

class MonitorCommand(Command):
    '''Runs continually while the robot is powered on.'''

    def __init__(self):
        super().__init__('MonitorCommand')

        '''
        Required because this is the default command for the monitor subsystem.
        '''
        self.requires(subsystems.monitor)

        self.setInterruptible(False)
        self.setRunWhenDisabled(True)

        self.table = NetworkTables.getGlobalTable()
        self.lastCheck = None
        self.cubeChanged = 0


    def initialize(self):
        self.hasCube = subsystems.intake.isCubeInIntake()
        self.table.putBoolean('Intake/hasCube', self.hasCube)


    def execute(self):
        '''Implement watchers here.'''

        currentTime = math.floor(Timer.getFPGATimestamp())
        if currentTime != self.lastCheck:
            self.lastCheck = currentTime

            self.table.putString(
                'Elevator/label',
                subsystems.elevator.getLevelName()
            )
            self.table.putString(
                'Elevator/position',
                subsystems.elevator.getHeight()
            )

        if self.hasCube != subsystems.intake.isCubeInIntake():
            self.cubeChanged += 1
        else:
            self.cubeChanged = 0

        if self.cubeChanged >= 5:
            self.hasCube = not self.hasCube
            self.table.putBoolean('Intake/hasCube', self.hasCube)
