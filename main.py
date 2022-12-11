import unittest
from servo import Servo

class TestServo(unittest.TestCase):
    def setUp(self):
        # Set up the servo object with the GPIO pin that it is attached to
        self.servo = Servo(18)

    def test_set_angle(self):
        # Test that the servo can move to the correct angle
        self.servo.set_angle(90)
        self.assertEqual(self.servo.get_angle(), 90)

    def test_set_angle_out_of_range(self):
        # Test that the servo throws an error when an angle outside of its range is set
        with self.assertRaises(ValueError):
            self.servo.set_angle(180)

    def test_set_angle_invalid_type(self):
        # Test that the servo throws an error when an angle of an invalid type is set
        with self.assertRaises(TypeError):
            self.servo.set_angle("90")

    def tearDown(self):
        # Clean up the servo object
        del self.servo

if __name__ == '__main__':
    unittest.main()
