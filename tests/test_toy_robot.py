import unittest
from toy_robot.toy_robot import ToyRobot
from toy_robot.direction import Direction
from toy_robot.position import Position


class TestToyRobot(unittest.TestCase):

    def setUp(self):
        self.robot = ToyRobot()

    def test_initialization(self):
        self.assertIsNone(self.robot.position)
        self.assertIsNone(self.robot.facing)

    def test_place_command(self):
        self.robot.place(0, 0, 'NORTH')
        self.assertEqual(self.robot.position, Position(0, 0))
        self.assertEqual(self.robot.facing, Direction.NORTH)

    def test_move_command(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.move()
        self.assertEqual(self.robot.position, Position(0, 1))

    def test_left_command(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.left()
        self.assertEqual(self.robot.facing, Direction.WEST)

    def test_right_command(self):
        self.robot.place(0, 0, 'NORTH')
        self.robot.right()
        self.assertEqual(self.robot.facing, Direction.EAST)

    def test_report_command(self):
        self.robot.place(0, 0, 'NORTH')
        self.assertEqual(self.robot.report(), "0,0,NORTH")

    def test_invalid_place_command(self):
        self.robot.execute_command("PLACE 0,0,NORTH")
        self.assertEqual(self.robot.position, Position(0, 0))
        self.assertEqual(self.robot.facing, Direction.NORTH)

        self.robot.execute_command("PLACE 5,5,NORTH")
        self.assertIsNone(self.robot.position)
        self.assertIsNone(self.robot.facing)

    def test_invalid_commands(self):
        self.robot.execute_command("INVALID")
        self.assertIsNone(self.robot.position)
        self.assertIsNone(self.robot.facing)


if __name__ == '__main__':
    unittest.main()