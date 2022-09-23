#!/usr/bin/env python
from colorama import Back

space = '          \n' * 8


def attach(s, t):
    s = s.split('\n')
    t = t.split('\n')

    return '\n'.join(
        a + '   ' + b
        for a, b in zip(s, t)
    )


def make_side(color):
    return [
        [color] * 3
        for _ in range(3)
    ]


def side_string(side):
    line_sep = '+--+--+--+\n'
    lines = line_sep.join(
        '|%s|\n' % '|'.join(row)
        for row in side
    )
    return '%s%s%s' % (line_sep, lines, line_sep)


def rotate_square_clockwise(side):
    return [
        [side[2][0], side[1][0], side[0][0]],
        [side[2][1], side[1][1], side[0][1]],
        [side[2][2], side[1][2], side[0][2]],
    ]


def copy_cube(cube):
    return {
        key: list(list(line) for line in value)
        for key, value in cube.items()}


def rotate_right_clockwise(cube):
    result = copy_cube(cube)

    result['right'] = rotate_square_clockwise(cube['right'])

    result['up'][0][2] = cube['front'][0][2]
    result['up'][1][2] = cube['front'][1][2]
    result['up'][2][2] = cube['front'][2][2]

    result['back'][2][0] = cube['up'][0][2]
    result['back'][1][0] = cube['up'][1][2]
    result['back'][0][0] = cube['up'][2][2]

    result['down'][0][2] = cube['back'][2][0]
    result['down'][1][2] = cube['back'][1][0]
    result['down'][2][2] = cube['back'][0][0]

    result['front'][0][2] = cube['down'][0][2]
    result['front'][1][2] = cube['down'][1][2]
    result['front'][2][2] = cube['down'][2][2]

    return result


def rotate_down_clockwise(cube):
    result = copy_cube(cube)

    result['down'] = rotate_square_clockwise(cube['down'])

    result['right'][2][0] = cube['front'][2][0]
    result['right'][2][1] = cube['front'][2][1]
    result['right'][2][2] = cube['front'][2][2]

    result['back'][2][0] = cube['right'][2][0]
    result['back'][2][1] = cube['right'][2][1]
    result['back'][2][2] = cube['right'][2][2]

    result['left'][2][0] = cube['back'][2][0]
    result['left'][2][1] = cube['back'][2][1]
    result['left'][2][2] = cube['back'][2][2]

    result['front'][2][0] = cube['left'][2][0]
    result['front'][2][1] = cube['left'][2][1]
    result['front'][2][2] = cube['left'][2][2]

    return result


def print_cube(cube):
    cube = {key: side_string(value) for key, value in cube.items()}

    print(attach(space, cube['up']))
    middle_line = attach(cube['left'], cube['front'])
    middle_line = attach(middle_line, cube['right'])
    middle_line = attach(middle_line, cube['back'])
    print(middle_line)
    print(attach(space, cube['down']))


start_cube = {
    'up':    make_side(Back.BLUE + '  ' + Back.RESET),
    'left':  make_side(Back.CYAN + '  ' + Back.RESET),
    'front': make_side(Back.WHITE + '  ' + Back.RESET),
    'right': make_side(Back.RED + '  ' + Back.RESET),
    'back':  make_side(Back.YELLOW + '  ' + Back.RESET),
    'down':  make_side(Back.GREEN + '  ' + Back.RESET),
}


def test_prints():
    print('we begin here')
    print_cube(start_cube)
    next_cube = copy_cube(start_cube)

    print('we rotate right clockwise')
    next_cube = rotate_right_clockwise(next_cube)
    print_cube(next_cube)

    print('we rotate down clockwise')
    next_cube = rotate_down_clockwise(next_cube)
    print_cube(next_cube)

    print('we rotate right clockwise')
    next_cube = rotate_right_clockwise(next_cube)
    print_cube(next_cube)

    print('we rotate down clockwise')
    next_cube = rotate_down_clockwise(next_cube)
    print_cube(next_cube)


def count_steps():
    print('Starting')
    print_cube(start_cube)

    next_cube = copy_cube(start_cube)

    for i in range(1, 500):
        next_cube = rotate_right_clockwise(next_cube)
        next_cube = rotate_down_clockwise(next_cube)
        print('After %d rotates:' % i)
        print_cube(next_cube)

        if next_cube == start_cube:
            print('And we got to the start')
            break


count_steps()
# test_prints()
