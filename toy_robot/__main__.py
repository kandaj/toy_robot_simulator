from .toy_robot import ToyRobot


def main():
    robot = ToyRobot()
    print("Enter commands for the toy robot (type 'EXIT' to quit):")
    try:
        while True:
            command = input().strip()
            if command == "EXIT":
                break
            robot.execute_command(command)
    except KeyboardInterrupt:
        print("\nExiting the toy robot simulator. Goodbye!")        


if __name__ == "__main__":
    main()