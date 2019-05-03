from .movecommand import MoveCommand

import subsystems
from custom.config import Config

import math


class PivotCommand(MoveCommand):
    '''Allows autonomous turning using the drive base encoders.'''

    def __init__(self, degrees, reverse=False, name=None):
        if name is None:
            name = 'Pivot %f degrees' % degrees

        super().__init__(degrees, False, name)

        self.direction = 1

        # 0 = Left Side, 1 = Right Side
        self.pivotSide = 0
        if degrees < 0:
            self.pivotSide = 1

        if reverse:
            self.direction = -1
            self.pivotSide = abs(self.pivotSide - 1)


    def initialize(self):
        '''Calculates new positions by offsetting the current ones.'''

        offset = self._calculateDisplacement() * self.direction
        targetPositions = []
        for i, position in enumerate(subsystems.drivetrain.getPositions()):
            side = i % 2
            if self.pivotSide == side:
                position += offset

            targetPositions.append(position)

        subsystems.drivetrain.setPositions(targetPositions)


    def _calculateDisplacement(self):
        '''
        In order to avoid having a separate ticksPerDegree, we calculate it
        based on the width of the robot base.
        '''

        inchesPerDegree = math.pi * Config('DriveTrain/width') / 360
        totalDistanceInInches = self.distance * inchesPerDegree

        return totalDistanceInInches * Config('DriveTrain/ticksPerInch') * 2
